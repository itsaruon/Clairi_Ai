import streamlit as st
from utils.transcript_fetcher import get_transcript
from utils.summarizer import summarize_text
import re
import requests
from pytube import YouTube
from bs4 import BeautifulSoup

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
            # Get video title - try multiple methods silently
            video_title = None
            
            # Method 1: Try pytube
            try:
                yt = YouTube(youtube_url)
                video_title = yt.title
            except Exception:
                pass
                
            # Method 2: Try web scraping if pytube failed
            if not video_title:
                try:
                    response = requests.get(youtube_url)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, 'html.parser')
                        title_tag = soup.find('title')
                        if title_tag and ' - YouTube' in title_tag.text:
                            video_title = title_tag.text.replace(' - YouTube', '')
                except Exception:
                    pass
            
            with st.spinner("🤖 Summarizing..."):
                summary = summarize_text(transcript)

            # Display summary with title if available
            if video_title:
                st.subheader(f"📄 Summary of: {video_title}")
            else:
                st.subheader("📄 Video Summary:")
                
            st.success(summary)
            
            # Display embedded video
            st.subheader("📺 Watch Video:")
            st.video(youtube_url)
