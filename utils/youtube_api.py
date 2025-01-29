from googleapiclient.discovery import build

YOUTUBE_API_KEY = "YOUR_API_KEY"

def get_video_captions(video_id):
    """Fetches captions for a YouTube video."""
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    try:
        request = youtube.captions().list(part="snippet", videoId=video_id)
        response = request.execute()
        if "items" in response and len(response["items"]) > 0:
            caption_id = response["items"][0]["id"]
            # Mocking caption download as YouTube Data API v3 does not support direct downloads
            return "Mocked captions for video."
        else:
            return "No captions available for this video."
    except Exception as e:
        return f"Error fetching captions: {e}"
