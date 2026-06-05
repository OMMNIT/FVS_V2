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

    # Read uploaded images
    kyc_img = read_image(kyc)
    live_img = read_image(live)

    # Extract embedding + base64
    kyc_embedding, kyc_face_base64 = get_embedding(
        kyc_img
    )

    live_embedding, live_face_base64 = get_embedding(
        live_img
    )

    # Face detection validation
    if kyc_embedding is None:
        return {
            "status": "FAILED",
            "message": "No face detected in KYC image"
        }

    if live_embedding is None:
        return {
            "status": "FAILED",
            "message": "No face detected in Live image"
        }

    # Similarity calculation
    similarity = cosine_similarity(
        kyc_embedding,
        live_embedding
    )

    # Image quality
    quality = image_quality_score(
        live_img
    )

    # Match decision
    decision = (
        "MATCH"
        if similarity >= threshold
        else "NO MATCH"
    )

    # Response
    return {

        "decision": decision,

        "similarity": round(float(similarity), 4),

        "threshold": threshold,

        "quality": round(float(quality), 4),

        "confidence": round(float(similarity), 4),

        "kyc_face_base64": kyc_face_base64

       
    }