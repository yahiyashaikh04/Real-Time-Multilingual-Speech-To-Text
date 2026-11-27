
from flask import (
    Flask, render_template, request,
    redirect, url_for, jsonify
)

import whisper
import os
import tempfile
import logging

from database import (
    create_table,
    save_transcription,
    get_transcriptions,
    update_transcription,
    delete_transcription
)

app = Flask(__name__)

# Upload size limit: 25 MB
app.config["MAX_CONTENT_LENGTH"] = 25 * 1024 * 1024

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load Whisper model
model = whisper.load_model("base")

# Create database table
create_table()


@app.errorhandler(413)
def file_too_large(error):
    return jsonify({
        "error": "Audio file is too large. Maximum size is 25 MB."
    }), 413


@app.route("/")
def index():
    records = get_transcriptions()
    return render_template("index.html", records=records)


@app.route("/transcribe", methods=["POST"])
def transcribe():

    if "audio" not in request.files:
        return jsonify({"error": "Audio file not found"}), 400

    audio = request.files["audio"]

    if not audio.filename:
        return jsonify({"error": "Empty audio file"}), 400

    if audio.mimetype not in [
        "audio/webm",
        "video/webm",
        "audio/wav",
        "audio/ogg",
        "audio/mpeg"
    ]:
        return jsonify({"error": "Unsupported audio format"}), 400

    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(
            suffix=".webm",
            delete=False
        ) as temp_file:

            temp_path = temp_file.name
            audio.save(temp_path)

        if os.path.getsize(temp_path) == 0:
            return jsonify({"error": "Audio file is empty"}), 400

        result = model.transcribe(
            temp_path,
            task="transcribe",
            fp16=False
        )

        text = result["text"].strip()

        if not text:
            return jsonify({
                "error": "No speech detected"
            }), 400

        save_transcription(text)

        return jsonify({
            "success": True,
            "text": text
        })

    except Exception:
        logger.exception("Transcription failed")

        return jsonify({
            "error": "Transcription failed. Please try again."
        }), 500

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)


@app.route("/history")
def history():
    records = get_transcriptions()
    return render_template("history.html", records=records)


@app.route("/edit/<int:record_id>", methods=["POST"])
def edit(record_id):

    text = request.form.get("text", "").strip()

    if not text:
        return "Text cannot be empty", 400

    update_transcription(record_id, text)

    return redirect(url_for("history"))


@app.route("/delete/<int:record_id>", methods=["POST"])
def delete(record_id):

    delete_transcription(record_id)

    return redirect(url_for("history"))


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
