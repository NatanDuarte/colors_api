import cv2 as cv
import numpy as np

from collections import Counter


class ColorExtractor:
    def __init__(self) -> None:
        self.image = None

    def load(self, image_path):
        self.image = cv.imread(image_path)
        return self

    def extract(self, n_colors):
        if (self.image.shape == 2):
            self.image = cv.cvtColor(self.image, cv.COLOR_GRAY2BGR)
        elif self.image.shape[2] == 4:
            self.image = cv.cvtColor(self.image, cv.COLOR_BGRA2BGR)

        self.image = cv.cvtColor(self.image, cv.COLOR_BGR2RGB)


        self._resize_input()

        pixels = self.image.reshape(-1, 3)

        criteria = (
            cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER,
            100,
            0.2
        )

        _, labels, pred_colors = cv.kmeans(
            pixels.astype(np.float32),
            n_colors,
            None, criteria, 10, cv.KMEANS_RANDOM_CENTERS
        )

        color_counts = Counter(labels.flatten())
        predominant_colors_rgb = \
            [pred_colors[i] for i, _ in color_counts.most_common(n_colors)]

        predominant_colors_hex = []
        for color in predominant_colors_rgb:
            hex_color = self._format_hex(color)
            predominant_colors_hex.append(hex_color)

        return {"palette": predominant_colors_hex}

    def _resize_input(self):
        height, width = self.image.shape[:2]
        new_width = int(width * 0.75)
        new_height = int(height * 0.75)
        self.image = cv.resize(
            self.image, 
            (new_width, new_height), 
            interpolation=cv.INTER_LINEAR
        )

    def _format_hex(self, color):
        return f'#{int(color[0]):02x}{int(color[1]):02x}{int(color[2]):02x}'
