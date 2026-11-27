
let recorder;
let audioChunks = [];

const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");

const statusText = document.getElementById("status");
const resultBox = document.getElementById("result");


startBtn.addEventListener("click", async function () {

    try {

        const stream = await navigator.mediaDevices.getUserMedia({
            audio: true
        });

        recorder = new MediaRecorder(stream);

        audioChunks = [];

        recorder.ondataavailable = function (event) {
            if (event.data.size > 0) {
                audioChunks.push(event.data);
            }
        };

        recorder.onstop = async function () {

            statusText.innerText = "Converting speech to text...";

            const audioBlob = new Blob(audioChunks, {
                type: recorder.mimeType
            });

            const formData = new FormData();

            formData.append("audio", audioBlob, "recording.webm");

            try {

                const response = await fetch("/transcribe", {
                    method: "POST",
                    body: formData
                });

                const data = await response.json();

                if (!response.ok) {
                    throw new Error(data.error || "Transcription failed");
                }

                resultBox.innerText = data.text;

                statusText.innerText = "Transcription completed!";

            } catch (error) {

                statusText.innerText = error.message;

            } finally {

                stream.getTracks().forEach(track => track.stop());

            }
        };

        recorder.start();

        startBtn.disabled = true;
        stopBtn.disabled = false;

        statusText.innerText = "Recording... Speak now";

    } catch (error) {

        statusText.innerText = "Microphone access denied";

    }

});


stopBtn.addEventListener("click", function () {

    if (recorder && recorder.state === "recording") {

        recorder.stop();

        startBtn.disabled = false;
        stopBtn.disabled = true;

        statusText.innerText = "Processing audio...";

    }

});
