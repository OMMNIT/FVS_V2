import cv2
import base64
from insightface.app import FaceAnalysis

# Initialize ArcFace
app = FaceAnalysis()
app.prepare(
    ctx_id=0,   # Use -1 for CPU only
    det_size=(640, 640)
)


def image_to_base64(img):
    """
    Convert OpenCV image to Base64 string
    """
    _, buffer = cv2.imencode(".jpg", img)
    return base64.b64encode(buffer).decode("utf-8")


def get_embedding(img):
    """
    Extract face embedding and cropped face image
    """

    faces = app.get(img)

    if len(faces) == 0:
        return None, None

    face = faces[0]

    # Get embedding
    embedding = face.embedding

    # Face bounding box
    bbox = face.bbox.astype(int)
    x1, y1, x2, y2 = bbox

    # Crop detected face
    face_crop = img[y1:y2, x1:x2]

    # Convert cropped face to Base64
    face_base64 = image_to_base64(face_crop)

    return embedding, face_base64