# Speech to Text – Multilingual Transcription Web Application

## Project Introduction

Speech to Text is a web-based application developed using Python and Flask that converts spoken audio into written text using the OpenAI Whisper speech recognition model.

The application allows users to record their voice through a web browser and convert the recorded audio into text. It supports multilingual speech recognition, including Hindi and English.

The application also provides a transcription history dashboard where users can view, edit, and delete their saved transcriptions.

## Features

- **Audio Recording:** Record voice directly through the web browser.
- **Speech-to-Text Conversion:** Convert recorded audio into text using OpenAI Whisper.
- **Multilingual Support:** Recognize speech in multiple languages, including Hindi and English.
- **Transcription History:** Store and display previous transcriptions.
- **Create:** Save new transcriptions in the database.
- **Read:** View saved transcription records.
- **Update:** Edit existing transcription text.
- **Delete:** Remove unwanted transcription records.
- **Audio File Cleanup:** Automatically delete temporary audio files after processing.
- **File Size Validation:** Restrict uploaded audio files to a maximum size of 25 MB.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| OpenAI Whisper | Speech recognition and transcription |
| SQLite | Relational database |
| HTML5 | Web page structure |
| CSS3 | Styling |
| Bootstrap 5 | Responsive user interface |
| JavaScript | Browser audio recording and API communication |
| FFmpeg | Audio processing |

## Project Structure

```text
speech-to-text/
│
├── app.py
├── database.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   ├── index.html
│   └── history.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── instance/
    └── speech.db
```

Note: The `instance/` folder and database file are generated automatically when the application runs.

## Installation Instructions

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd speech-to-text
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```powershell
venv\Scripts\activate
```

For Linux or macOS:

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Install FFmpeg

Whisper requires FFmpeg to process audio files.

Download FFmpeg from:

https://ffmpeg.org/download.html

Install it and add the FFmpeg `bin` directory to your system PATH.

Verify the installation:

```bash
ffmpeg -version
```

## How to Run the Application

Start the Flask application:

```bash
python app.py
```

Open your web browser and visit:

```text
http://127.0.0.1:5000/
```

You can now:

1. Start recording using your microphone.
2. Stop recording to submit the audio.
3. View the generated transcription.
4. Open transcription history.
5. Edit or delete saved records.

**Note:** Microphone access generally requires localhost or a secure HTTPS connection.

## Database

The application uses SQLite as its relational database.

The database contains a `transcriptions` table with the following fields:

| Field | Description |
|---|---|
| id | Unique transcription ID |
| text | Transcribed text |
| created_at | Date and time of creation |

The database table is created automatically when the application starts.

## Current Limitations

- The current implementation processes audio after the recording is stopped. It does not yet provide true continuous real-time streaming transcription.
- Transcription accuracy may vary depending on audio quality, background noise, and language.
- The current local setup uses SQLite. A production deployment may require a persistent database such as PostgreSQL.
- FFmpeg must be installed and accessible through the system PATH.
- The application currently does not include user authentication or role-based access control.

## Future Improvements

- Implement continuous real-time audio transcription.
- Add user authentication and authorization.
- Add PostgreSQL database support.
- Improve the user interface and mobile responsiveness.
- Deploy the application to a cloud hosting platform.

## Author

**Yahiya Shaikh**

GitHub: https://www.github.com/yahiyashaikh04

## License

This project is developed for learning and technical assessment purposes.
