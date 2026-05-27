from fastapi import APIRouter, UploadFile, File, Form
from image_utils import read_image
from embedding_service import get_embedding
from similarity import cosine_similarity
from quality_service import image_quality_score

router = APIRouter()


@router.post("/verify-face")
async def verify_face(
    kyc: UploadFile = File(...),
    live: UploadFile = File(...),
    threshold: float = Form(0.5)
):

    # Read images correctly
    kyc_img = read_image(kyc)
    live_img = read_image(live)


    kyc_embedding = get_embedding(
        kyc_img
    )

    live_embedding = get_embedding(
        live_img
    )


    similarity = cosine_similarity(
        kyc_embedding,
        live_embedding
    )


    quality = image_quality_score(
        live_img
    )


    decision = (
        "MATCH"
        if similarity >= threshold
        else "NO MATCH"
    )


    return {

        "decision":
            decision,

        "similarity":
            similarity,

        "threshold":
            threshold,

        "quality":
            quality,

        "confidence":
            similarity

    }