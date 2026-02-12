import re
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from langchain_text_splitters import RecursiveCharacterTextSplitter

def extract_video_id(url):
    """
    Robust extraction of YouTube Video ID.
    Handles:
    - standard: youtube.com/watch?v=VIDEO_ID
    - short: youtu.be/VIDEO_ID
    - embed: youtube.com/embed/VIDEO_ID
    - shorts: youtube.com/shorts/VIDEO_ID
    """
    pattern = r"(?:v=|\/|youtu\.be\/|embed\/|shorts\/)([0-9A-Za-z_-]{11})"
    match = re.search(pattern, url)
    return match.group(1) if match else None

def get_transcript_chunks(video_id):
    """
    Fetches transcript (trying multiple languages/auto-gen) and splits it.
    """
    try:
        # 0. Validate video ID
        print(f"\n{'='*60}")
        print(f"Processing video ID: {video_id}")
        print(f"{'='*60}")
        
        # 1. Instantiate the API and get transcript list
        print(f"Fetching transcript...")
        api = YouTubeTranscriptApi()
        transcript_list = api.list(video_id)
        
        # 2. Try to find a suitable transcript
        transcript = None
        
        # Try to find English or Hindi transcript (manual or generated)
        for t in transcript_list:
            if t.language_code in ['en', 'hi', 'es', 'fr', 'de']:
                transcript = t
                print(f"✓ Found transcript in language: {t.language} ({t.language_code})")
                break
        
        # If no preferred language found, use the first available
        if not transcript:
            for t in transcript_list:
                transcript = t
                print(f"✓ Using transcript in language: {t.language} ({t.language_code})")
                break
        
        if not transcript:
            print(f"✗ No transcript available for video {video_id}")
            return None

        # 3. Fetch the actual transcript data
        transcript_data = transcript.fetch()
        print(f"Processing {len(transcript_data)} transcript segments...")
        
        # 4. Format text with timestamps
        text_parts = []
        for item in transcript_data:
            start = int(item.start)  # Access as attribute, not dict key
            text = item.text         # Access as attribute, not dict key
            # Create a string with the timestamp embedded
            text_parts.append(f"[START:{start}] {text}")

        full_text = " ".join(text_parts)

        # 3. Split text into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100
        )
        chunks = text_splitter.create_documents([full_text])

        # 4. Add metadata to chunks for the RAG source
        for chunk in chunks:
            # Find the first timestamp in this chunk
            match = re.search(r"\[START:(\d+)\]", chunk.page_content)
            if match:
                timestamp = match.group(1)
                chunk.metadata["source"] = f"https://youtu.be/{video_id}?t={timestamp}s"
            else:
                chunk.metadata["source"] = f"https://youtu.be/{video_id}"
        
        print(f"✓ Successfully created {len(chunks)} chunks from transcript")
        return chunks

    except TranscriptsDisabled:
        print(f"✗ Transcripts are disabled for video {video_id}")
        return None
    except NoTranscriptFound:
        print(f"✗ No transcript available for video {video_id}")
        return None
    except Exception as e:
        print(f"✗ Error fetching transcript for {video_id}: {type(e).__name__} - {str(e)}")
        import traceback
        traceback.print_exc()
        return None