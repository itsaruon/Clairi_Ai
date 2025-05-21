from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_chunk_length=1000):
    chunks = []
    while len(text) > max_chunk_length:
        split_at = text[:max_chunk_length].rfind(".")
        if split_at == -1:
            split_at = max_chunk_length
        chunks.append(text[:split_at+1])
        text = text[split_at+1:]
    chunks.append(text)

    final_summary = ""
    for chunk in chunks:
        summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        final_summary += summary[0]['summary_text'] + " "

    return format_as_notes(final_summary.strip())

def format_as_notes(text):
    # Turn sentences into bullet points
    lines = text.split(". ")
    bullets = [f"• {line.strip().capitalize()}." for line in lines if line]
    return "\n".join(bullets)
