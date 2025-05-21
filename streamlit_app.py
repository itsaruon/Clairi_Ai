import streamlit as st
from utils.transcript_fetcher import get_transcript
from utils.summarizer import summarize_text
import re

def extract_video_id(url):
    match = re.search(r"(?:v=|youtu\.be/)([\w-]{11})", url)
    return match.group(1) if match else None

# Set page config
st.set_page_config(page_title="ClairiAI", layout="centered")

# App title and intro
st.title("🎬 ClairiAI")
st.write("Paste a YouTube link below and we'll summarize the video for you using AI!")

# Input field
youtube_url = st.text_input("📎 YouTube Video URL:")

# Button to trigger summarization
if st.button("✨ Summarize Video") and youtube_url:
    video_id = extract_video_id(youtube_url)

    if not video_id:
        st.error("❌ Invalid YouTube URL. Please check and try again.")
    else:
        with st.spinner("⏳ Fetching transcript..."):
            transcript = get_transcript(video_id)

        if "Error" in transcript:
            st.error(transcript)
        else:
            with st.spinner("🤖 Summarizing..."):
                summary = summarize_text(transcript)

            st.subheader("📄 Video Summary:")
            st.success(summary)
