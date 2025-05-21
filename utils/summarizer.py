from transformers import pipeline
import re

# Load the Hugging Face summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_chunk_length=1000):
    # Split text into smaller chunks to avoid model token limits
    chunks = []
    while len(text) > max_chunk_length:
        split_at = text[:max_chunk_length].rfind(".")
        if split_at == -1:
            split_at = max_chunk_length
        chunks.append(text[:split_at+1])
        text = text[split_at+1:]
    chunks.append(text)

    # Summarize each chunk
    final_summary = ""
    for chunk in chunks:
        summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        final_summary += summary[0]['summary_text'] + " "

    return format_as_notes(final_summary.strip())

def format_as_notes(text):
    # Remove filler like [music], [applause], etc.
    text = re.sub(r"\[.*?\]", "", text)

    # Split into sentences
    sentences = re.split(r'(?<=[.!?]) +', text)

    # Format into clean bullet points
    bullets = []
    for s in sentences:
        s = s.strip()
        if not s:
            continue
        # Capitalize the first letter
        if s[0].islower():
            s = s[0].upper() + s[1:]
        # Ensure sentence ends with punctuation
        if s[-1] not in ".!?":
            s += "."
        bullets.append(f"• {s}")

    return "\n\n".join(bullets)
