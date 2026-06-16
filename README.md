# AI Virtual Mouse

A real-time virtual mouse system built with Python, OpenCV, MediaPipe, and PyAutoGUI.

The system tracks hand landmarks using a webcam and allows users to control the mouse cursor with their index finger. A pinch gesture between the thumb and index finger is used to perform mouse clicks.

## Features

* Real-time hand tracking
* Cursor control using index finger movement
* Pinch-to-click interaction
* Cursor smoothing for stable movement
* Adjustable tracking area
* Modular project structure

## Technologies

* Python
* OpenCV
* MediaPipe
* NumPy
* PyAutoGUI

## Project Structure

```text
src/
├── main.py
├── hand_detector.py
├── mouse_controller.py
└── config.py
```

## Controls

| Gesture              | Action      |
| -------------------- | ----------- |
| Index Finger         | Move Cursor |
| Thumb + Index Finger | Left Click  |

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

## Future Improvements

* Right-click gesture support
* Scroll control
* Dynamic cursor smoothing
* Multi-monitor support
* Custom gesture mapping
* Gesture-based drag and drop

## Author

Wenzhuo Huang
