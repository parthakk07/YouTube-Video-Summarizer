import re

import google.genai as genai
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url):
    patterns = [
        r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})",
        r"youtube\.com/shorts/([a-zA-Z0-9_-]{11})",
        r"youtube\.com/embed/([a-zA-Z0-9_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    raise ValueError(f"Could not extract video ID from: {url}")


def get_transcript(video_id):
    transcript = YouTubeTranscriptApi().fetch(video_id)
    return " ".join(snippet.text for snippet in transcript.snippets)


def summarize_transcript(transcript):
    client = genai.Client(api_key="AIzaSyAsWNw6hQ4iptE8SS72MXlDmZMMUbrVqF8")
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=f"Summarize the following YouTube video transcript in a clear, concise way:\n\n{transcript}",
    )
    return response.text


def main():
    url = input("Enter the url :")

    video_id = extract_video_id(url)
    transcript = get_transcript(video_id)

    summary = summarize_transcript(transcript)
    print(f"\nSummary:\n{summary}")
    with open("summary.txt", "w") as f:
        f.write(summary)


if __name__ == "__main__":
    main()
