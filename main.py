from utils.transcript_fetcher import get_transcript
from utils.summarizer import summarize_text

def extract_video_id(youtube_url):
    # Supports full URL or short share links
    import re
    match = re.search(r"(?:v=|youtu\.be/)([\w-]{11})", youtube_url)
    return match.group(1) if match else None

# === Paste YouTube URL Here ===
youtube_url = "https://www.youtube.com/watch?v=jNQXAC9IVRw"  # 'Me at the zoo' - the first YouTube video ever
video_id = extract_video_id(youtube_url)

if video_id:
    print("Fetching transcript...")
    transcript = get_transcript(video_id)

    if "Error" not in transcript:
        print("Summarizing...")
        summary = summarize_text(transcript)

        with open("outputs/summary.txt", "w", encoding="utf-8") as f:
            f.write(summary)

        print("\n--- SUMMARY ---\n")
        print(summary)
    else:
        print(transcript)
else:
    print("Invalid YouTube URL.")
