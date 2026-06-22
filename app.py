from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route("/")
def home():
    return "API Running"

@app.route("/transcript")
def transcript():
    video_id = request.args.get("videoId")

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([x["text"] for x in transcript])

        return jsonify({
            "success": True,
            "transcript": text
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })
