import React, { useRef, useState } from "react";
import Webcam from "react-webcam";

const Video = () => {
  const [isRecording, setIsRecording] = useState(false);
  const [status, setStatus] = useState("");
  const [processedVideoUrl, setProcessedVideoUrl] = useState(null);
  const webcamRef = useRef(null);
  const mediaRecorderRef = useRef(null);
  const chunks = useRef([]);

  const handleStartRecording = () => {
    const stream = webcamRef.current.video.srcObject;
    mediaRecorderRef.current = new MediaRecorder(stream, {
      mimeType: "video/webm",
    });

    mediaRecorderRef.current.ondataavailable = (event) => {
      if (event.data.size > 0) {
        chunks.current.push(event.data);
      }
    };

    mediaRecorderRef.current.onstop = sendVideoToBackend;
    mediaRecorderRef.current.start();
    setIsRecording(true);
    setStatus("Recording started...");
  };

  const handleStopRecording = () => {
    mediaRecorderRef.current.stop();
    setIsRecording(false);
    setStatus("Recording stopped. Processing...");
  };

  async function sendVideoToBackend() {
    if (chunks.current.length === 0) {
      setStatus("No video recorded to process.");
      return;
    }

    const videoBlob = new Blob(chunks.current, { type: "video/webm" });
    chunks.current = []; // Clear recorded chunks

    const formData = new FormData();
    formData.append("video", videoBlob, "recorded_video.webm");

    try {
      const response = await fetch("http://127.0.0.1:5001/process_video", {
        method: "POST",
        body: formData,
        headers: {
          Accept: "application/json",
        },
        mode: "cors", // Ensure CORS issues are handled
      });

      if (!response.ok) {
        throw new Error(
          `Server Error: ${response.status} ${response.statusText}`
        );
      }

      const contentType = response.headers.get("content-type");

      if (contentType && contentType.includes("application/json")) {
        // If backend sends a message (no nudity found)
        const jsonResponse = await response.json();
        setStatus(jsonResponse.message);
        setProcessedVideoUrl(null);
      } else if (contentType && contentType.includes("video")) {
        // If backend returns a processed (censored) video
        const videoBlob = await response.blob();
        const videoUrl = URL.createObjectURL(videoBlob);
        setProcessedVideoUrl(videoUrl);
        setStatus("Processed video with censorship applied.");
      } else {
        setStatus("Unexpected response format.");
      }
    } catch (error) {
      console.error("Fetch Error:", error);
      setStatus("Error while sending video to backend.");
    }
  }

  return (
    <div style={{ textAlign: "center" }}>
      <Webcam
        ref={webcamRef}
        audio={true}
        videoConstraints={{ facingMode: "user" }}
        style={{ transform: "scaleX(-1)" }}
      />
      <div>
        {!isRecording ? (
          <button onClick={handleStartRecording}>Start Recording</button>
        ) : (
          <button onClick={handleStopRecording}>Stop Recording</button>
        )}
      </div>
      <p>{status}</p>

      {processedVideoUrl && (
        <div>
          <h3>Processed Video:</h3>
          <video controls src={processedVideoUrl} style={{ width: "80%" }} />
        </div>
      )}
    </div>
  );
};

export default Video;
