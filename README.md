# YouTube Video Summarizer

A Python script that extracts transcripts from YouTube videos and generates AI-powered summaries using Google Gemini.

## Setup

1. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your Google Gemini API key:**
   ```bash
   export GEMINI_API_KEY="your-api-key"
   ```

## Usage

Run the script and paste a YouTube URL when prompted:

```bash
python main.py
```

Enter a URL in any of these formats:
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/shorts/VIDEO_ID`

The summary will be printed to the console and saved to `summary.txt`.

## Requirements

- `google-genai` - Google Gemini AI client
- `YouTubeTranscriptApi` - Fetch YouTube transcripts
- `regex` - URL parsing
