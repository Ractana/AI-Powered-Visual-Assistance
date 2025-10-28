# For simplicity, all modules (speech, detection, OCR, control) are implemented here.
# In a production version, these can be modularized into separate scripts.
# Import required libraries
import cv2, time, requests, numpy as np, pyttsx3, pytesseract, sounddevice as sd, vosk, json
from ultralytics import YOLO

# Convert text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

# Capture a single command using microphone and Vosk STT
def listen(model_path='vosk-model-small-en-us-0.15', duration=4):
    model = vosk.Model(model_path)
    rec = vosk.KaldiRecognizer(model, 16000)
    def callback(indata, frames, time_, status):
        rec.AcceptWaveform(indata.tobytes())
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1, callback=callback):
        sd.sleep(int(duration * 1000))
    res = json.loads(rec.FinalResult())
    return res.get('text', '').lower().strip()

# Capture image from webcam
def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    return frame if ret else None

# Perform object detection using YOLOv8
def detect_objects(frame, model):
    results = model.predict(source=frame, conf=0.3, verbose=False)
    detections = []
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = r.names[cls]
            conf = float(box.conf[0])
            xyxy = [int(x) for x in box.xyxy[0]]
            detections.append({'label': label, 'conf': conf, 'bbox': xyxy})
    return detections

# Generate a simple spoken description of detected objects
def describe(detections):
    if not detections:
        return "No objects detected."
    labels = [d['label'] for d in detections]
    return "Detected objects are: " + ", ".join(labels)

# Main execution flow
def main():
    model = YOLO('yolov8n.pt')
    vosk_model = 'vosk-model-small-en-us-0.15'
    speak("Drishti Mithra is ready. Say capture to start or stop to exit.")

    while True:
        command = listen(vosk_model)
        print("Command:", command)
        if 'capture' in command:
            frame = capture_image()
            if frame is None:
                speak("Camera not detected.")
                continue
            detections = detect_objects(frame, model)
            desc = describe(detections)
            print(desc)
            speak(desc)
            cv2.imshow("Output", frame)
            cv2.waitKey(2000)
            cv2.destroyAllWindows()
        elif 'stop' in command or 'exit' in command:
            speak("Thank you for using Drishti Mithra. Goodbye!")
            break
        else:
            time.sleep(1)

if __name__ == "__main__":
    main()

