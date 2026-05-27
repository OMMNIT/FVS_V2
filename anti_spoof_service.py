import os
import sys
import cv2
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SILENT_FACE_DIR = os.path.join(
    BASE_DIR,
    "Silent-Face-Anti-Spoofing"
)

sys.path.append(SILENT_FACE_DIR)

os.chdir(SILENT_FACE_DIR)


from src.anti_spoof_predict import AntiSpoofPredict
from src.generate_patches import CropImage
from src.utility import parse_model_name


MODEL_DIR = os.path.join(
    SILENT_FACE_DIR,
    "resources",
    "anti_spoof_models"
)


model_test = AntiSpoofPredict(
    device_id=0
)

image_cropper = CropImage()


def spoof_check(img):

    try:

        prediction = np.zeros((1,3))

        bbox = model_test.get_bbox(img)

        print("FACE =", bbox)


        for model_name in os.listdir(MODEL_DIR):

            model_path = os.path.join(
                MODEL_DIR,
                model_name
            )

            h_input, w_input, model_type, scale = (
                parse_model_name(model_name)
            )


            param = {

                "org_img": img,
                "bbox": bbox,

                "scale": scale,

                "out_w": w_input,
                "out_h": h_input,

                "crop": True

            }


            img_crop = image_cropper.crop(
                **param
            )


            pred = model_test.predict(
                img_crop,
                model_path
            )


            print(model_name)
            print(pred)

            prediction += pred


        print("\nFINAL")
        print(prediction)


        label = np.argmax(prediction)

        score = prediction[0][label]


        live_score = float(prediction[0][1])
        spoof_score = float(prediction[0][0])


        return {

            "label": int(label),

            "live_score": live_score,

            "spoof_score": spoof_score,

            "raw": prediction.tolist()

        }


    except Exception as e:

        print(e)

        return {

            "label":0,
            "live_score":0,
            "spoof_score":1,

            "error":str(e)

        }