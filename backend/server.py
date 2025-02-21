

# from nudenet import NudeDetector
# from PIL import Image, ImageFilter
# import io
# from moviepy import VideoFileClip, concatenate_videoclips
# from werkzeug.utils import secure_filename
# import logging
# import base64
# import os
# from flask import Flask, request, jsonify, send_file
# import cv2
# from flask_cors import CORS
# import numpy as np
# import subprocess

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png'}

# def blur_entire_image(img):
#     return img.filter(ImageFilter.GaussianBlur(20))  # Apply heavy blur to entire image

# app = Flask(__name__)
# # CORS(app)
# CORS(app, supports_credentials=True)
# CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins
# UPLOAD_FOLDER = "uploads"
# PROCESSED_FOLDER = "processed"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(PROCESSED_FOLDER, exist_ok=True)
# logging.basicConfig(level=logging.INFO)
# detector = NudeDetector()

# @app.route('/process_video', methods=['POST'])



# def process_video():
#     config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB
#     video_base64 = request.form.get('video')
#     if not video_base64:
#         return jsonify({"error": "No video provided"}), 400
#     logging.info(f"Received video data, length: {len(video_base64)} characters")
#     try:
#         if video_base64.startswith('data:video/webm;base64,'):
#             video_base64 = video_base64[len('data:video/webm;base64,'):]
#         video_data = base64.b64decode(video_base64)
#         input_path = os.path.join(UPLOAD_FOLDER, 'uploaded_video.webm')
#         with open(input_path, 'wb') as f:
#             f.write(video_data)
#         logging.info(f"Video saved to {input_path}")
#         processed_path = os.path.join(PROCESSED_FOLDER, 'processed_video.webm')
#         nudity_detected = censor_video(input_path, processed_path)
#         if nudity_detected:
#             logging.info(f"Processed video saved to {processed_path}")
#             return send_file(processed_path, as_attachment=True)
#         else:
#             logging.info("No nudity detected in the video.")
#             return jsonify({"message": "No nudity detected"}), 200
#     except Exception as e:
#         logging.error(f"Error during video processing: {str(e)}")
#         return jsonify({"error": f"Error processing video: {str(e)}"}), 500

# # @app.after_request
# def add_cors_headers(response):
#     response.headers["Access-Control-Allow-Origin"] = "*"
#     response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
#     response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
#     return response


# @app.route('/image_prediction', methods=['POST'])
# def image_prediction():
#     if 'image' not in request.files:
#         return jsonify({'error': 'No file part'}), 400
#     file = request.files['image']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400

#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         img_bytes = file.read()
#         img = Image.open(io.BytesIO(img_bytes))
#         img.save('temp_image.jpg')
#         result = detector.detect('temp_image.jpg')
#         os.remove('temp_image.jpg')

#         if result:
#             filtered_result = [item for item in result if item['class'] not in ['FACE_FEMALE', 'FACE_MALE', 'ARMPIT']]
#             if filtered_result:
#                 img = blur_entire_image(img)  # Blur the entire image if nudity is detected
#                 img_bytes = io.BytesIO()
#                 img.save(img_bytes, format='JPEG')
#                 img_bytes.seek(0)
#                 img_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')
#                 return jsonify({'prediction': 'Nudity detected', 'image': img_base64, 'result': filtered_result})
#             else:
#                 return jsonify({'prediction': 'No nudity detected'})
#         else:
#             return jsonify({'prediction': 'Error in detection'})
#     return jsonify({'error': 'Invalid file type'}), 400

# if __name__ == '__main__':
#     app.run(debug=True)



# # #checccccccc
# from nudenet import NudeDetector
# from PIL import Image, ImageFilter
# import io
# from moviepy import VideoFileClip, concatenate_videoclips
# from werkzeug.utils import secure_filename
# import logging
# import base64
# import os
# from flask import Flask, request, jsonify, send_file
# import cv2
# from flask_cors import CORS
# import numpy as np
# import subprocess


# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png'}

# def blur_entire_image(img):
#     return img.filter(ImageFilter.GaussianBlur(20))  # Apply heavy blur to entire image

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}) # Restrict CORS to frontend origin
# # CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "http://localhost:3001"]}})
# CORS(app) 
# UPLOAD_FOLDER = "uploads"
# PROCESSED_FOLDER = "processed"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(PROCESSED_FOLDER, exist_ok=True)
# logging.basicConfig(level=logging.INFO)
# detector = NudeDetector()

# # @app.route('/process_video', methods=['POST'])
# # def process_video():
# #     app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB
# #     video_base64 = request.form.get('video')
# #     if not video_base64:
# #         return jsonify({"error": "No video provided"}), 400
# #     logging.info(f"Received video data, length: {len(video_base64)} characters")
# #     try:
# #         if video_base64.startswith('data:video/webm;base64,'):
# #             video_base64 = video_base64[len('data:video/webm;base64,'):]
# #         video_data = base64.b64decode(video_base64)
# #         input_path = os.path.join(UPLOAD_FOLDER, 'uploaded_video.webm')
# #         with open(input_path, 'wb') as f:
# #             f.write(video_data)
# #         logging.info(f"Video saved to {input_path}")
# #         processed_path = os.path.join(PROCESSED_FOLDER, 'processed_video.webm')
# #         nudity_detected = censor_video(input_path, processed_path)
# #         if nudity_detected:
# #             logging.info(f"Processed video saved to {processed_path}")
# #             return send_file(processed_path, as_attachment=True)
# #         else:
# #             logging.info("No nudity detected in the video.")
# #             return jsonify({"message": "No nudity detected"}), 200
# #     except Exception as e:
# #         logging.error(f"Error during video processing: {str(e)}")
# #         return jsonify({"error": f"Error processing video: {str(e)}"}), 500





# # @app.route('/process_video', methods=['POST'])
# # def process_video():
# #     app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB

# #     if 'video' not in request.files:
# #         return jsonify({"error": "No video file provided"}), 400

# #     video_file = request.files['video']
# #     if video_file.filename == '':
# #         return jsonify({"error": "No selected file"}), 400

# #     input_path = os.path.join(UPLOAD_FOLDER, 'uploaded_video.webm')
# #     video_file.save(input_path)
# #     logging.info(f"Video saved to {input_path}")

# #     processed_path = os.path.join(PROCESSED_FOLDER, 'processed_video.webm')
# #     nudity_detected = censor_video(input_path, processed_path)

# #     if nudity_detected:
# #         logging.info(f"Processed video saved to {processed_path}")
# #         return send_file(processed_path, as_attachment=True)
# #     else:
# #         logging.info("No nudity detected in the video.")
# #         return jsonify({"message": "No nudity detected"}), 200



# logging.basicConfig(level=logging.INFO)

# def censor_video(input_path, output_path):
#     """
#     Dummy function to detect and censor nudity in a video.
#     Replace this with actual AI-based nudity detection and blurring.
#     """
#     nudity_detected = True  # Simulated detection

#     if nudity_detected:
#         os.system(f"cp {input_path} {output_path}")  # Replace with actual blurring logic
#         return True

#     return False





# # need 
# # @app.route('/process_video', methods=['POST'])
# # def process_video():
# #     try:
# #         if 'video' not in request.files:
# #             return jsonify({"error": "No video file provided"}), 400

# #         video_file = request.files['video']
# #         if video_file.filename == '':
# #             return jsonify({"error": "No selected file"}), 400

# #         input_path = os.path.join(UPLOAD_FOLDER, 'uploaded_video.webm')
# #         video_file.save(input_path)
# #         logging.info(f"Video saved to {input_path}")

# #         processed_path = os.path.join(PROCESSED_FOLDER, 'processed_video.webm')
# #         nudity_detected = censor_video(input_path, processed_path)

# #         if nudity_detected:
# #             logging.info(f"Nudity detected! Sending processed video.")
# #             return send_file(processed_path, as_attachment=True, mimetype="video/webm")

# #         logging.info("No nudity detected in the video.")
# #         return jsonify({"message": "No nudity detected"}), 200

# #     except Exception as e:
# #         logging.error(f"Error processing video: {str(e)}")
# #         return jsonify({"error": str(e)}), 500



# @app.route("/process_video", methods=["POST"])
# def process_video():
#     if "video" not in request.files:
#         return jsonify({"error": "No video file provided"}), 400

#     video_file = request.files["video"]
#     if video_file.filename == "":
#         return jsonify({"error": "No selected file"}), 400

#     # Save video file (optional)
#     video_file.save("uploaded_video.webm")

#     return jsonify({"message": "✅ Video received and processed!"})

# @app.after_request
# # def add_cors_headers(response):
# #     response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
# #     response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
# #     response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
# #     return response


# @app.after_request
# def add_cors_headers(response):
#     response.headers["Access-Control-Allow-Origin"] = request.headers.get("Origin") or "*"
#     response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
#     response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
#     return response


# @app.route('/image_prediction', methods=['POST'])
# def image_prediction():
#     if 'image' not in request.files:
#         return jsonify({'error': 'No file part'}), 400
#     file = request.files['image']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400

#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         img_bytes = file.read()
#         img = Image.open(io.BytesIO(img_bytes))
#         img.save('temp_image.jpg')
#         result = detector.detect('temp_image.jpg')
#         os.remove('temp_image.jpg')

#         if result:
#             filtered_result = [item for item in result if item['class'] not in ['FACE_FEMALE', 'FACE_MALE', 'ARMPIT']]
#             if filtered_result:
#                 img = blur_entire_image(img)  # Blur the entire image if nudity is detected
#                 img_bytes = io.BytesIO()
#                 img.save(img_bytes, format='JPEG')
#                 img_bytes.seek(0)
#                 img_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')
#                 return jsonify({'prediction': 'Nudity detected', 'image': img_base64, 'result': filtered_result})
#             else:
#                 return jsonify({'prediction': 'No nudity detected'})
#         else:
#             return jsonify({'prediction': 'Error in detection'})
#     return jsonify({'error': 'Invalid file type'}), 400

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)



from nudenet import NudeDetector
from PIL import Image, ImageFilter
import io
import cv2
import os
import base64
import logging
import numpy as np
import tempfile
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})  # Restrict CORS to frontend
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)

UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)
logging.basicConfig(level=logging.INFO)

detector = NudeDetector()

def allowed_file(filename):
    """Check if file type is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png'}

def blur_entire_image(img):
    """Apply heavy blur to entire image"""
    return img.filter(ImageFilter.GaussianBlur(20))

def extract_frames(video_path, frame_rate=10):
    """Extracts frames from video at specified frame intervals."""
    cap = cv2.VideoCapture(video_path)
    frames = []
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % frame_rate == 0:  # Extract every 10th frame
            frames.append(frame)
        frame_count += 1

    cap.release()
    return frames



# Load nudity detection model
nudity_detector = NudeDetector()

# def detect_nudity_in_frame(frame):
#     """Detects nudity in a single frame and blurs it if necessary."""
#     results = nudity_detector.detect(frame)

#     # Ignore non-explicit labels
#     filtered_results = [item for item in results if item["class"] not in ["FACE_FEMALE", "FACE_MALE", "ARMPIT"]]

#     if filtered_results:
#         frame = blur_entire_image(frame)  # Blur the entire frame if nudity is detected
#         return frame, True
#     return frame, False




def detect_nudity_in_frame(frame):
    """Detects nudity in a single frame and blurs it if necessary."""
    results = nudity_detector.detect(frame)

    # Ignore non-explicit labels
    filtered_results = [item for item in results if item["class"] not in ["FACE_FEMALE", "FACE_MALE", "ARMPIT"]]

    if filtered_results:
        # Convert OpenCV frame to PIL Image
        pil_image = Image.fromarray(frame)
        pil_image = blur_entire_image(pil_image)  # Apply blur
        frame = np.array(pil_image)  # Convert back to OpenCV format
        return frame, True

    return frame, False


# def blur_entire_image(frame):
#     """Applies Gaussian blur to the entire image (frame)."""
#     return cv2.GaussianBlur(frame, (51, 51), 30)




# def process_video(video_path):
#     """Reads video, detects nudity in frames, applies blurring if needed, and saves processed video."""
#     temp_output_path = os.path.join(tempfile.gettempdir(), "processed_video.mp4")

#     cap = cv2.VideoCapture(video_path)
#     fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Codec for saving video
#     fps = int(cap.get(cv2.CAP_PROP_FPS))
#     frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#     out = cv2.VideoWriter(temp_output_path, fourcc, fps, (frame_width, frame_height))

#     nudity_detected = False

#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break

#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         processed_frame, detected = detect_nudity_in_frame(frame_rgb)

#         if detected:
#             nudity_detected = True

#         out.write(cv2.cvtColor(processed_frame, cv2.COLOR_RGB2BGR))

#     cap.release()
#     out.release()

#     return temp_output_path, nudity_detected



def process_video(video_path):
    """Reads video, detects nudity in frames, applies blurring if needed, and saves processed video."""
    temp_output_path = os.path.join(tempfile.gettempdir(), "processed_video.mp4")

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return None, False  # Return None if the video cannot be opened

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out = cv2.VideoWriter(temp_output_path, fourcc, fps, (frame_width, frame_height))

    nudity_detected = False

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        try:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            processed_frame, detected = detect_nudity_in_frame(frame_rgb)

            if detected:
                nudity_detected = True

            out.write(cv2.cvtColor(processed_frame, cv2.COLOR_RGB2BGR))

        except Exception as e:
            print(f"Error processing frame: {e}")
            continue  # Skip bad frames instead of crashing

    cap.release()
    out.release()

    return temp_output_path if nudity_detected else None, nudity_detected



@app.route("/process_video", methods=["POST"])
# def process_video_endpoint():
#     """Handles video upload and detects nudity in frames"""
#     if "video" not in request.files:
#         return jsonify({"error": "No video file provided"}), 400

#     video_file = request.files["video"]
#     if video_file.filename == "":
#         return jsonify({"error": "No selected file"}), 400

#     # Save uploaded video temporarily
#     temp_video_path = os.path.join(tempfile.gettempdir(), "uploaded_video.webm")
#     video_file.save(temp_video_path)

#     # Process the video
#     processed_video_path, nudity_detected = process_video(temp_video_path)

#     # Remove temporary input video
#     os.remove(temp_video_path)

#     if nudity_detected:
#         return send_file(
#             processed_video_path,
#             mimetype="video/mp4",
#             as_attachment=True,
#             download_name="processed_video.mp4",
#         )
#     else:
#         return jsonify({"message": "✅ No nudity detected in the video."})




@app.route("/process_video", methods=["POST"])
def process_video_endpoint():
    """Handles video upload and detects nudity in frames"""
    if "video" not in request.files:
        return jsonify({"error": "No video file provided"}), 400

    video_file = request.files["video"]
    if video_file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    temp_video_path = os.path.join(tempfile.gettempdir(), "uploaded_video.webm")
    video_file.save(temp_video_path)

    # Process the video
    processed_video_path, nudity_detected = process_video(temp_video_path)

    os.remove(temp_video_path)  # Remove original video

    if not processed_video_path:
        return jsonify({"message": "✅ No nudity detected in the video."})

    try:
        return send_file(
            processed_video_path,
            mimetype="video/mp4",
            as_attachment=True,
            download_name="processed_video.mp4",
        )
    except Exception as e:
        return jsonify({"error": f"Error sending processed video: {str(e)}"}), 500


@app.route('/image_prediction', methods=['POST'])
def image_prediction():
    """Handles image upload and detects nudity"""
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes))
        img.save('temp_image.jpg')

        result = detector.detect('temp_image.jpg')
        os.remove('temp_image.jpg')

        if result:
            filtered_result = [item for item in result if item['class'] not in ['FACE_FEMALE', 'FACE_MALE', 'ARMPIT']]
            if filtered_result:
                img = blur_entire_image(img)  # Blur the entire image if nudity is detected
                img_bytes = io.BytesIO()
                img.save(img_bytes, format='JPEG')
                img_bytes.seek(0)
                img_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')
                return jsonify({'prediction': 'Nudity detected', 'image': img_base64, 'result': filtered_result})
            else:
                return jsonify({'prediction': 'No nudity detected'})
        else:
            return jsonify({'prediction': 'Error in detection'})

    return jsonify({'error': 'Invalid file type'}), 400

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)


app.run(host="0.0.0.0", port=5001, debug=True)
