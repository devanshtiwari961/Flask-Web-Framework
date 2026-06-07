from flask import Flask, render_template, Response
import cv2
import face_recognition
import numpy as np

app = Flask(__name__)

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

krish_img = face_recognition.load_image_file("Krish/krish.JPG")
devansh_img = face_recognition.load_image_file("Devansh/devansh.JPG")

known_face_encodings = [
    face_recognition.face_encodings(krish_img)[0],
    face_recognition.face_encodings(devansh_img)[0]
]

known_face_names = ["Krish", "Devansh"]

face_locations = []
face_names = []
frame_count = 0

def gen_frames():
    global frame_count, face_locations, face_names

    while True:
        success, frame = camera.read()

        if not success:
            continue

        frame = cv2.flip(frame, 1)
        frame_count += 1

        if frame_count % 5 == 0:
            small_frame = cv2.resize(frame, (0, 0), fx=0.2, fy=0.2)
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

            face_locations = face_recognition.face_locations(
                rgb_small_frame,
                model="hog"
            )

            face_encodings = face_recognition.face_encodings(
                rgb_small_frame,
                face_locations
            )

            face_names = []

            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(
                    known_face_encodings,
                    face_encoding,
                    tolerance=0.5
                )

                name = "Unknown"

                face_distances = face_recognition.face_distance(
                    known_face_encodings,
                    face_encoding
                )

                best_match = np.argmin(face_distances)

                if matches[best_match]:
                    name = known_face_names[best_match]

                face_names.append(name)

        for (top, right, bottom, left), name in zip(face_locations, face_names):

            top *= 5
            right *= 5
            bottom *= 5
            left *= 5

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom),
                          (0, 255, 0), cv2.FILLED)

            cv2.putText(
                frame,
                name,
                (left + 6, bottom - 8),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 255),
                2
            )

        _, buffer = cv2.imencode(
            ".jpg",
            frame,
            [cv2.IMWRITE_JPEG_QUALITY, 70]
        )

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' +
            buffer.tobytes() +
            b'\r\n'
        )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(
        gen_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

if __name__ == "__main__":
    app.run(debug=True)