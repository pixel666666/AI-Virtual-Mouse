import cv2
import mediapipe as mp


class HandDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

    def find_hands(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(img_rgb)

        hand_label = "Unknown"

        if results.multi_handedness:

            for hand in results.multi_handedness:

                hand_label = hand.classification[0].label

        landmarks = []

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(
                    img,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS
                )

                h, w, c = img.shape

                for idx, lm in enumerate(hand_landmarks.landmark):
                    cx = int(lm.x * w)
                    cy = int(lm.y * h)
                    landmarks.append((idx, cx, cy))

        return img, landmarks, hand_label