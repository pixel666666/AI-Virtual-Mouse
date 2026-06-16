import pyautogui
import numpy as np
import math


class MouseController:

    def __init__(self):

        self.screen_w, self.screen_h = pyautogui.size()

        self.prev_x = 0
        self.prev_y = 0

        self.pinch_active = False

    def move_cursor(
        self,
        x,
        y,
        frame_reduction,
        smoothening,
        frame_w,
        frame_h
    ):

        screen_x = np.interp(
            x,
            (frame_reduction, frame_w - frame_reduction),
            (self.screen_w, 0)
        )

        screen_y = np.interp(
            y,
            (frame_reduction, frame_h - frame_reduction),
            (0, self.screen_h)
        )

        screen_x = max(0, min(self.screen_w, screen_x))
        screen_y = max(0, min(self.screen_h, screen_y))

        curr_x = screen_x
        curr_y = screen_y

        screen_x = self.prev_x + (
            curr_x - self.prev_x
        ) / smoothening

        screen_y = self.prev_y + (
            curr_y - self.prev_y
        ) / smoothening

        self.prev_x = screen_x
        self.prev_y = screen_y

        pyautogui.moveTo(screen_x, screen_y)

    def click(
        self,
        thumb_x,
        thumb_y,
        index_x,
        index_y,
        threshold
    ):

        distance = math.sqrt(
            (thumb_x - index_x) ** 2 +
            (thumb_y - index_y) ** 2
        )

        if distance < threshold:

            if not self.pinch_active:

                pyautogui.click()

                self.pinch_active = True

        else:

            self.pinch_active = False

        return distance