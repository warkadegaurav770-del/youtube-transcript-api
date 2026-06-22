@app.route("/transcript")
def transcript():
    video_id = request.args.get("videoId")

    try:
        ytt_api = YouTubeTranscriptApi()
        transcript = ytt_api.fetch(video_id)

        text = " ".join([x.text for x in transcript])

        return jsonify({
            "success": True,
            "transcript": text
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })
