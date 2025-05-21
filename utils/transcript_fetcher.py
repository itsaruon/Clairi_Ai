import os
import tempfile
import whisper
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled

def get_transcript(video_id):
    try:
        # Try YouTube captions first
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return ' '.join([t['text'] for t in transcript])
    except (NoTranscriptFound, TranscriptsDisabled):
        # Fall back to Whisper if no captions
        return get_transcript_with_whisper(video_id)
    except Exception as e:
        return f"❌ Error fetching transcript: {str(e)}"

def get_transcript_with_whisper(video_id):
    try:
        yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
        stream = yt.streams.filter(only_audio=True).first()

        with tempfile.TemporaryDirectory() as tmpdir:
            audio_path = os.path.join(tmpdir, "audio.mp4")
            stream.download(output_path=tmpdir, filename="audio.mp4")

            model = whisper.load_model("base")
            result = model.transcribe(audio_path)
            return result["text"]
    except Exception as e:
        return f"❌ Whisper failed: {str(e)}"
