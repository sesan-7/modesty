import React, { useRef, useState } from "react";
import Webcam from "react-webcam";
import axios from "axios";
import "./styles/camera.css";

const Camera = () => {
  const webcamRef = useRef(null);
  const [imageSrc, setImageSrc] = useState(null);
  const [prediction, setPrediction] = useState("");
  const [error, setError] = useState("");
  const [blurredImage, setBlurredImage] = useState(null);
  const [output, setoutput] = useState("");

  const capture = async () => {
    const image = webcamRef.current.getScreenshot();
    setImageSrc(image);
    setPrediction("");
    setError("");
    setoutput("");
    setBlurredImage(null);

    if (image) {
      const blob = await fetch(image).then((res) => res.blob());
      const formData = new FormData();
      formData.append("image", blob, "captured-image.jpg");
      try {
        const response = await axios.post(
          "http://127.0.0.1:5001/image_prediction",
          formData,
          {
            headers: { "Content-Type": "multipart/form-data" },
          }
        );
        // console.log(response)
        if (response.data.prediction === "Nudity detected") {
          setPrediction("Nudity detected");
          setoutput(
            "This image cannot be saved because it contain violated content"
          );
          setBlurredImage("data:image/jpeg;base64," + response.data.image);
        } else {
          setPrediction("No nudity detected");
          const date = new Date();
          // console.log(date)
          const link = document.createElement("a");
          link.href = imageSrc;
          link.download = `${date}.jpg`;
          link.click();
        }
      } catch (err) {
        setError("An error occurred: " + err.message);
        console.log(err);
      }
    } else {
      setError("Failed to capture the image. Please try again.");
    }
  };

  return (
    <div style={{ textAlign: "center" }}>
      <h1>Camera App - Violation Checker</h1>
      <Webcam
        audio={false}
        ref={webcamRef}
        screenshotFormat="image/jpeg"
        width={400}
      />
      <div style={{ marginTop: "20px" }}>
        <button
          onClick={capture}
          style={{ padding: "10px 20px", fontSize: "16px", cursor: "pointer" }}
        >
          Capture and Check
        </button>
      </div>
      <div
        style={{
          marginTop: "20px",
          color: "red",
          display: "flex",
          flexDirection: "column",
        }}
      >
        {output}
        {prediction == "No Nudity detected" && imageSrc && (
          <img src={imageSrc} alt="Captured" width={400} />
        )}
        {prediction == "Nudity detected" && blurredImage && (
          <img src={blurredImage} alt="Blurred Image" width={400} />
        )}
        {/* {prediction && <h2>{prediction}</h2>} */}
        {error && <h3 style={{ color: "red" }}>{error}</h3>}
      </div>
    </div>
  );
};

export default Camera;
