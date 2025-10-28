# AI-Powered Visual Assistance for the Blind

## Overview
A wearable AI-powered assistant that provides real-time scene understanding and voice feedback to visually impaired users.  
The system integrates **computer vision, spatial reasoning, and natural language processing** to describe the user's surroundings in real time using **YOLOv8s**, **rule-based spatial relationships**, **Phi-2 LLM**, and **espeak** for speech output.  
Deployed entirely on a **Raspberry Pi 5**, the system operates offline, ensuring low latency and privacy.

---

## Features
- Real-time object detection using YOLOv8s  
- Spatial awareness using rule-based relational mapping  
- Scene description generation using Phi-2 language model  
- Voice feedback via eSpeak text-to-speech engine  
- Voice command activation using Vosk (offline speech-to-text)  
- Fully functional offline operation on Raspberry Pi 5  
- Modular and scalable design for future enhancements  

---

## Tech Stack

| Component | Technology |
|------------|-------------|
| Hardware | Raspberry Pi 5, ESP32-CAM, Wired Headset |
| Software | Python, PyTorch |
| Models | YOLOv8s (Object Detection), Phi-2 (Natural Language Generation) |
| Libraries | OpenCV, Tesseract OCR, pyttsx3, transformers, Vosk, espeak |
| Platform | Raspberry Pi OS |

---

## System Architecture
```mermaid
flowchart TD
    A[Voice Command via Vosk] --> B[ESP32-CAM Image Capture]
    B --> C[YOLOv8s Object Detection]
    C --> D[Rule-Based Spatial Relationship Analysis]
    D --> E[Phi-2 LLM for Scene Description]
    E --> F[Text-to-Speech Conversion via espeak]
    F --> G[User Audio Feedback through Headset]
