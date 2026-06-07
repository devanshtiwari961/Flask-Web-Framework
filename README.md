# Project 2 — Live Face Recognition with Flask

A Flask web application that performs real-time face recognition using your webcam. The app identifies known faces (Krish and Devansh) and streams the annotated video feed to the browser. This project is part of the Krish Naik Data Science Flask Web Framework course.

## Overview

Project 2 combines Flask with OpenCV and the `face_recognition` library to build a live face recognition system accessible through a web browser. It also includes standalone scripts for local webcam demos and Haar cascade-based detection.

| File | Description |
|------|-------------|
| `app.py` | Main Flask app — live face recognition web stream |
| `Video/app.py` | Haar cascade face and eye detection web stream |
| `test.py` | Utility / test script |

## Features

### `app.py` — Web-Based Face Recognition (Main Application)
- Captures live video from the default webcam
- Recognizes known faces: **Krish** and **Devansh**
- Labels unknown faces as **Unknown**
- Draws bounding boxes and name labels on detected faces
- Streams video to the browser via MJPEG (`/video_feed`)
- Performance optimizations:
  - Processes every 5th frame for face detection
  - Downscales frames to 20% size for faster recognition
  - Uses HOG model for face location detection

### `Video/app.py` — Haar Cascade Detection
- Detects faces and eyes using OpenCV Haar cascades
- Displays a live count of faces detected
- Streams annotated video to the browser

## Screenshots

### Real-Time Face Recognition
![Face Recognition](Project%202/screenshots/face_recognition.png)
*Live detection identifying Devansh*

### Face and Eye Detection
![Face and Eye Detection](Project%202/screenshots/face_eye_detection.png)
*Live detection highlighting both faces and eyes*

## Project Structure

```
Project 2/
├── app.py                  # Main face recognition Flask app
├── test.py                 # Test script
├── requirements.txt        # Python dependencies
├── Krish/
│   └── krish.JPG           # Known face — Krish
├── Devansh/
│   └── devansh.jpg         # Known face — Devansh
├── templates/
│   ├── index.html          # Live video feed page
│   └── result.html         # Result template
└── Video/
    ├── app.py              # Haar cascade detection app
    ├── requirements.txt
    ├── Haarcascades/       # Cascade classifier XML files
    └── templates/
        └── index.html
```

## Routes (`app.py`)

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Displays the live face recognition video feed |
| `/video_feed` | GET | MJPEG stream with face detection and labels |

## How It Works

1. On startup, the app loads reference images from `Krish/krish.JPG` and `Devansh/devansh.JPG`.
2. Face encodings are computed for each known person.
3. The webcam captures frames continuously.
4. Every 5th frame is processed: faces are located, encoded, and compared against known encodings.
5. Matching faces are labeled with names; non-matches are labeled **Unknown**.
6. Annotated frames are streamed to the browser as JPEG images.

## Prerequisites

- Python 3.7+ (Python 3.10 recommended)
- A working webcam
- **CMake** — Required to build `dlib` (face recognition dependency)
- **Visual Studio Build Tools** (Windows) — Required for compiling native extensions

> **Note:** Installing `dlib` and `face-recognition` on Windows can be challenging. Ensure CMake and C++ build tools are installed before running `pip install`.

## Installation

1. Navigate to the project directory:

```bash
cd "Project 2"
```

2. (Recommended) Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate        # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

If `dlib` fails to install, try installing it separately first:

```bash
pip install cmake
pip install dlib
pip install face-recognition
```

## Running the Application

### Main Face Recognition App

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

### HaarCascade Detection App

```bash
cd Video
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## Adding New Known Faces

1. Create a folder with the person's name (e.g., `John/`).
2. Add a clear, front-facing photo (e.g., `John/john.jpg`).
3. Update `app.py`:

```python
john_img = face_recognition.load_image_file("John/john.jpg")

known_face_encodings = [
    face_recognition.face_encodings(krish_img)[0],
    face_recognition.face_encodings(devansh_img)[0],
    face_recognition.face_encodings(john_img)[0],
]

known_face_names = ["Krish", "Devansh", "John"]
```

## Dependencies

| Package | Purpose |
|---------|---------|
| Flask | Web framework |
| opencv-python | Webcam capture and image processing |
| face-recognition | Face detection and recognition |
| dlib | Machine learning backend for face recognition |
| numpy | Numerical operations |
| Pillow | Image handling |

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Webcam not opening | Ensure no other app is using the camera. On Windows, `cv2.CAP_DSHOW` is used for compatibility. |
| `dlib` install fails | Install CMake and Visual Studio Build Tools, then retry. |
| Face not recognized | Use a clear, well-lit reference photo. Adjust `tolerance` in `compare_faces()` (default: 0.5). |
| Slow performance | The app already skips frames and downscales images. Close other heavy applications. |
| Wrong image path | Ensure file names match exactly (e.g., `krish.JPG` vs `krish.jpg`). |

## Learning Objectives

- Stream live webcam video through a Flask web application
- Use the `face_recognition` library for real-time identification
- Optimize video processing for performance (frame skipping, downscaling)
- Serve MJPEG video streams with Flask `Response`
- Compare Haar cascade detection vs. deep learning-based recognition

## Notes

- Debug mode is enabled (`debug=True`) for development. Disable it in production.
- The webcam is initialized at 640×480 resolution in `app.py`.
- Reference images must contain exactly one detectable face each.
- The `.conda/` folder in this directory is a local Python environment and can be ignored when setting up your own virtual environment.
