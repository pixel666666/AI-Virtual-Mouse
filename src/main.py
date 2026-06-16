import cv2

from hand_detector import HandDetector
from mouse_controller import MouseController

from config import (
    FRAME_REDUCTION,
    SMOOTHENING,
    CLICK_THRESHOLD,
    CURSOR_SIZE
)

cap = cv2.VideoCapture(0)

detector = HandDetector()

mouse = MouseController()

while True:

    success, img = cap.read()

    if not success:
        break

    img, landmarks, hand_label = detector.find_hands(img)

    if len(landmarks) >= 9:

        thumb_x = landmarks[4][1]
        thumb_y = landmarks[4][2]

        index_x = landmarks[8][1]
        index_y = landmarks[8][2]

        h, w, c = img.shape

        cv2.rectangle(
            img,
            (FRAME_REDUCTION, FRAME_REDUCTION),
            (w - FRAME_REDUCTION, h - FRAME_REDUCTION),
            (255, 0, 255),
            2
        )

        mouse.move_cursor(
            index_x,
            index_y,
            FRAME_REDUCTION,
            SMOOTHENING,
            w,
            h
        )

        distance = mouse.click(
            thumb_x,
            thumb_y,
            index_x,
            index_y,
            CLICK_THRESHOLD
        )

        cv2.circle(
            img,
            (index_x, index_y),
            CURSOR_SIZE,
            (0, 0, 255),
            cv2.FILLED
        )

        cv2.putText(
            img,
            f"Distance: {int(distance)}",
            (30, 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    cv2.imshow("AI Virtual Mouse", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()