import json
import cv2 as cv
import numpy as np


class ColorExtractor:
    def __init__(self) -> None:
        self.image = None
    
    def load(self, image_path):
        self.image = cv.imread(image_path)
        return self
    
    def extract(self, n_colors):
        if (self.image.shape == 2):
            self.image = cv.cvtColor(self.image, cv.COLOR_GRAY2BGR)

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

        predominant_colors = []
        for color in pred_colors:
            hex_color = f'#{color[0]}{color[1]}{color[2]}'
            predominant_colors.append(hex_color)

        return json.dumps({"palette": predominant_colors}, indent=2)
