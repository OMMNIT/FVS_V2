from insightface.app import FaceAnalysis

app = FaceAnalysis()
app.prepare(
    ctx_id=0,
    det_size=(640,640)
)


def get_embedding(img):

    faces = app.get(img)

    if len(faces) == 0:
        return None

    embedding = faces[0].embedding

    return embedding