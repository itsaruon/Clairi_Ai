from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return ' '.join([t['text'] for t in transcript])
    except Exception as e:
        return f"Error fetching transcript: {str(e)}"
