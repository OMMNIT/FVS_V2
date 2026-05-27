import cv2
import numpy as np


def read_image(file):

    contents = file.file.read()

    nparr = np.frombuffer(
        contents,
        np.uint8
    )

    img = cv2.imdecode(
        nparr,
        cv2.IMREAD_COLOR
    )

    return img