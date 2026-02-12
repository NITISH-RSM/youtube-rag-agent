import sys
import os

# Ensure src modules can be imported
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from src.ingest import extract_video_id, get_transcript_chunks
from src.vector_store import create_vector_db
from src.rag import SimpleRAGChain

load_dotenv()

app = FastAPI()

# In-memory storage (Global State)
app_state = {"rag_chain": None}

class VideoRequest(BaseModel):
    url: str

class ChatRequest(BaseModel):
    query: str

@app.post("/process-video")
async def process_video(request: VideoRequest):
    video_id = extract_video_id(request.url)
    if not video_id:
        raise HTTPException(
            status_code=400, 
            detail="Invalid YouTube URL. Make sure it's a valid YouTube video link (youtube.com/watch?v=... or youtu.be/...)"
        )

    chunks = get_transcript_chunks(video_id)
    if not chunks:
        raise HTTPException(
            status_code=404, 
            detail="❌ Transcript not found for this video. Possible reasons:\n\n"
                   "1. **Transcripts disabled** - Creator disabled captions\n"
                   "2. **No auto-generated captions** - Video too short or language not supported\n"
                   "3. **Unsupported language** - Try videos in English, Spanish, or major languages\n"
                   "4. **Live stream/Short video** - These don't have transcripts\n\n"
                   "💡 Try testing with: https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        )

    vector_store = create_vector_db(chunks)
    app_state["rag_chain"] = SimpleRAGChain(vector_store)
    
    return {"message": "Video processed successfully"}

@app.post("/chat")
async def chat(request: ChatRequest):
    if not app_state["rag_chain"]:
        raise HTTPException(status_code=400, detail="No video processed")
    
    response = app_state["rag_chain"].invoke(request.query)
    
    # Format sources for JSON response
    sources = [
        {"source": doc.metadata.get("source"), "content": doc.page_content} 
        for doc in response["source_documents"]
    ]
    
    return {"answer": response["result"], "sources": sources}