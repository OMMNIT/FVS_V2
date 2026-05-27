import cv2
import numpy as np


def image_quality_score(img):

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    blur = cv2.Laplacian(
        gray,
        cv2.CV_64F
    ).var()


    brightness = np.mean(gray)


    quality = (
        min(blur / 100, 1)
        +
        min(brightness / 255, 1)
    ) / 2


    return float(quality)