import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="YOUTUBE-AGENT", layout="wide")
st.title(" RAG-AGENT: Chat with YouTube")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "current_video" not in st.session_state:
    st.session_state.current_video = None

# Sidebar
with st.sidebar:
    st.header(" Video Input")
    url = st.text_input(
        "Enter YouTube URL",
        placeholder="https://www.youtube.com/watch?v=...",
        help="Paste any YouTube video URL here"
    )
    
    # Show example videos
    with st.expander(" Try Example Videos"):
        st.markdown("""
        **Click to copy:**
        - `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
        - `https://youtu.be/dQw4w9WgXcQ`
        """)
    
    # Display current video if processed
    if st.session_state.current_video:
        st.info(f" Current Video: {st.session_state.current_video}")
    
    if st.button(" Process Video", use_container_width=True):
        # Validate URL not empty
        if not url or not url.strip():
            st.error("Please enter a valid YouTube URL")
        else:
            with st.spinner("Processing..."):
                try:
                    print(f"[Frontend] Processing URL: {url}")
                    res = requests.post(f"{API_URL}/process-video", json={"url": url})
                    if res.status_code == 200:
                        st.success(" Ready to Chat!")
                        st.session_state.messages = []
                        st.session_state.current_video = url
                        st.rerun()
                    else:
                        error_detail = res.json().get('detail', 'Unknown error')
                        st.error(f" {error_detail}")
                        st.info(
                            "**Tips:**\n"
                            "- Make sure the video has captions enabled\n"
                            "- Try a different video with auto-generated captions\n"
                            "- Check if transcripts are available in your region"
                        )
                except requests.exceptions.ConnectionError:
                    st.error(" Backend is not running. Start main.py first.")
                    st.info("Run `uvicorn backend.main:app --reload` in the backend folder")

# Main Chat Area
if not st.session_state.current_video:
    st.info(" Enter a YouTube URL in the sidebar to get started!")
    st.markdown("""
    ### How to use:
    1. Paste a YouTube video URL in the sidebar
    2. Click " Process Video"
    3. Wait for processing to complete
    4. Ask questions about the video content!
    
    **Note:** The video must have captions/transcripts enabled.
    """)
else:
    # Chat Interface
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if query := st.chat_input("Ask a question..."):
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    res = requests.post(f"{API_URL}/chat", json={"query": query})
                    if res.status_code == 200:
                        data = res.json()
                        st.markdown(data["answer"])
                        
                        if data.get("sources"):
                            with st.expander(" Sources"):
                                for src in data["sources"]:
                                    st.markdown(f"- [Jump to Video]({src['source']})")
                        
                        st.session_state.messages.append({"role": "assistant", "content": data["answer"]})
                    else:
                        st.error(f"Error: {res.json().get('detail')}")
                except Exception as e:
                    st.error(f"Connection Error: {e}")
