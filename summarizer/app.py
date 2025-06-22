from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from summarizer import run_summarizer
import os

app = Flask(__name__)
CORS(app)

@app.route("/summarize", methods=["POST"])
def summarize():
    if 'video' not in request.files:
        return jsonify({"error": "No video uploaded"}), 400

    video = request.files['video']
    video_path = "temp_video.mp4"
    video.save(video_path)

    try:
        result = run_summarizer(video_path)
        response_data = {
            "summary": result["summary"],              # ✅ include 3–5 line summary
            "transcript": result["transcript"],
            "visual_summary": result["visual_summary"]
        }
        return jsonify(response_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if os.path.exists(video_path):
            os.remove(video_path)

@app.route("/download-pdf", methods=["GET"])
def download_pdf():
    path = os.path.join(os.path.dirname(__file__), "video_summary.pdf")
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    else:
        return jsonify({"error": "PDF not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
