from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route("/")
def home():
    return "API Running"

@app.route("/transcript")
def transcript():
    video_id = request.args.get("videoId")

    if not video_id:
        return jsonify({
            "success": False,
            "error": "Video ID missing"
        })

    try:
        api = YouTubeTranscriptApi()
        fetched_transcript = api.fetch(video_id)

        text = " ".join([item.text for item in fetched_transcript])

        return jsonify({
            "success": True,
            "transcript": text
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })

if __name__ == "__main__":
    app.run()
