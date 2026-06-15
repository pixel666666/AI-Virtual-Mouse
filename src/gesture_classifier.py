def classify_gesture(landmarks,hand_label):
    if len(landmarks) == 0:
        return "No Hand"

    points = {idx: (x, y) for idx, x, y in landmarks}

    fingers = []
    if hand_label == "Right":
        thumb_open = points[4][0] > points[2][0]
    else:
        thumb_open = points[4][0] < points[2][0]
    # Thumb
    if points[4][0] > points[2][0]:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers
    finger_tips = [8, 12, 16, 20]
    finger_pips = [6, 10, 14, 18]

    for tip, pip in zip(finger_tips, finger_pips):
        if points[tip][1] < points[pip][1]:
            fingers.append(1)
        else:
            fingers.append(0)

    if fingers == [0, 0, 0, 0, 0]:
        return "Fist"

    if fingers == [1, 1, 1, 1, 1]:
        return "Open Hand"

    if fingers == [0, 1, 1, 0, 0]:
        return "Peace"

    if fingers == [1, 0, 0, 0, 0]:
        return "Thumb"

    return "Unknown"