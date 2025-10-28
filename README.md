# AI-Powered Visual Assistance Sling Bag

## Overview
A wearable vision device designed to assist visually impaired users through real-time obstacle detection, text reading, and voice-based navigation feedback.  
The system uses an on-board Raspberry Pi 5 integrated with a camera and the YOLOv8n model for object detection, and the Phi-2 LLM for contextual guidance.

---

## Features
- Real-time object and obstacle detection using YOLOv8n  
- Text-to-speech feedback for environmental awareness and text reading  
- Integration of Phi-2 LLM for contextual voice guidance  
- Compact design implemented within a portable sling bag  
- Audio output via Bluetooth or wired earphones for user convenience  

---

## Tech Stack

| Component | Technology |
|------------|-------------|
| Hardware | Raspberry Pi 5, Camera Module, Bluetooth Earphones |
| Software | Python, PyTorch, Flask |
| Models | YOLOv8n (object detection), Phi-2 LLM (language response) |
| Libraries | OpenCV, pyttsx3, Tesseract OCR, torch, transformers |
| Platform | Raspberry Pi OS |

---

## System Architecture
```mermaid
flowchart TD
    A[Camera Module] --> B[YOLOv8n Object Detection]
    A --> C[OCR Text Extraction]
    B --> D[Context Analysis via Phi-2 LLM]
    C --> D
    D --> E[Speech Synthesis Output]
    E --> F[User (Audio Feedback)]
