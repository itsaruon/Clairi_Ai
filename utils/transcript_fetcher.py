import os
import tempfile
import whisper
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled

def get_transcript(video_id):
    try:
        print(f"Attempting to get transcript for video ID: {video_id}")
        # Try YouTube captions first
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        print(f"Successfully retrieved transcript with {len(transcript)} segments")
        return ' '.join([t['text'] for t in transcript])
    except (NoTranscriptFound, TranscriptsDisabled) as e:
        print(f"No transcript found, falling back to Whisper: {str(e)}")
        # Fall back to Whisper if no captions
        return get_transcript_with_whisper(video_id)
    except Exception as e:
        print(f"Exception in get_transcript: {type(e).__name__}: {str(e)}")
        return f"❌ Error fetching transcript: {str(e)}"

def get_transcript_with_whisper(video_id):
    try:
        print(f"Attempting to download video with ID: {video_id} using pytube")
        yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
        print(f"Video title: {yt.title}")
        stream = yt.streams.filter(only_audio=True).first()
        print(f"Selected audio stream: {stream}")

        with tempfile.TemporaryDirectory() as tmpdir:
            audio_path = os.path.join(tmpdir, "audio.mp4")
            print(f"Downloading audio to: {audio_path}")
            stream.download(output_path=tmpdir, filename="audio.mp4")
            print(f"Download complete, file size: {os.path.getsize(audio_path)} bytes")

            print("Loading Whisper model...")
            model = whisper.load_model("base")
            print("Transcribing audio...")
            result = model.transcribe(audio_path)
            print("Transcription complete")
            return result["text"]
    except Exception as e:
        print(f"Exception in get_transcript_with_whisper: {type(e).__name__}: {str(e)}")
        return f"❌ Whisper failed: {str(e)}"
