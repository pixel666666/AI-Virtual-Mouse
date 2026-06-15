import cv2

from hand_detector import HandDetector
from gesture_classifier import classify_gesture


cap = cv2.VideoCapture(0)

detector = HandDetector()

while True:
    success, img = cap.read()

    if not success:
        print("Camera Error")
        break

    img, landmarks,hand_label = detector.find_hands(img)

    gesture = classify_gesture(landmarks,hand_label)

    cv2.putText(
        img,
        hand_label,
        (30, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )
    cv2.putText(
        img,
        gesture,
        (30, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )



    cv2.imshow("Gesture Control System", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()