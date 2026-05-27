# FVS_V2 — Face Verification System API

A production-oriented **Face Verification API** built using **FastAPI + ArcFace (InsightFace)** for comparing **KYC identity images** with **live captured images**.

The system extracts embeddings using ArcFace and computes similarity scores to determine whether two faces belong to the same person.

---

# Features

✅ ArcFace face embedding generation  
✅ Face similarity comparison using cosine similarity  
✅ Image quality assessment  
✅ FastAPI REST API  
✅ Swagger UI documentation  
✅ Modular service architecture  
✅ Deployable microservice

---

# Tech Stack

| Component | Technology |
|----------|-------------|
| Backend | FastAPI |
| Face Embeddings | ArcFace (InsightFace) |
| Image Processing | OpenCV |
| Similarity Metric | Cosine Similarity |
| Numerical Processing | NumPy |
| Model Runtime | ONNX Runtime |
| API Server | Uvicorn |

---

# System Architecture

```txt
                 ┌────────────────────┐
                 │   KYC Image        │
                 └────────┬───────────┘
                          │
                          ▼
                 ┌────────────────────┐
                 │ Read + Preprocess  │
                 └────────┬───────────┘
                          │
                          ▼
                 ┌────────────────────┐
                 │ ArcFace Embedding  │
                 └────────┬───────────┘
                          │
                          │
                          │
                          ▼
                 ┌────────────────────┐
                 │ Cosine Similarity  │
                 └────────┬───────────┘
                          ▲
                          │
                          │
                 ┌────────┴───────────┐
                 │ ArcFace Embedding  │
                 └────────┬───────────┘
                          ▲
                          │
                 ┌────────────────────┐
                 │ Live Image         │
                 └────────────────────┘


Final Output:

MATCH / NO MATCH
Similarity Score
Quality Score
Confidence
```

---

# Request Flow

```txt
Client
   │
   ▼
POST /verify-face
   │
   ▼
Read Images
   │
   ▼
Generate ArcFace Embeddings
   │
   ▼
Calculate Similarity
   │
   ▼
Evaluate Threshold
   │
   ▼
Return JSON Response
```

---

# Project Structure

```txt
FVS_V2/

│
├── main.py                  # FastAPI entrypoint
├── routes.py                # API routes
├── embedding_service.py     # ArcFace embedding extraction
├── similarity.py            # Similarity calculation
├── quality_service.py       # Image quality scoring
├── image_utils.py           # Image preprocessing
├── requirements.txt
│
└── utils/
    └── services/
```

---

# Installation

Clone repository:

```bash
git clone https://github.com/OMMNIT/FVS_V2.git

cd FVS_V2
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running API

Start server:

```bash
python -m uvicorn main:app --reload
```

API:

```txt
http://127.0.0.1:8000
```

Swagger:

```txt
http://127.0.0.1:8000/docs
```

OpenAPI:

```txt
http://127.0.0.1:8000/openapi.json
```

---

# API Endpoint

## Verify Face

Endpoint:

```http
POST /verify-face
```

Parameters:

| Parameter | Type | Description |
|-----------|------|-------------|
| kyc | File | Identity image |
| live | File | Live captured image |
| threshold | Float | Matching threshold |

---

Example Request:

```bash
curl -X POST \
"http://127.0.0.1:8000/verify-face" \
-F "kyc=@id.jpg" \
-F "live=@live.jpg"
```

---

Example Response:

```json
{
  "decision":"MATCH",
  "similarity":0.82,
  "threshold":0.5,
  "quality":0.73,
  "confidence":0.82
}
```

---

# Similarity Interpretation

| Score | Interpretation |
|-------|----------------|
| >0.80 | Strong Match |
| 0.60–0.80 | Possible Match |
| <0.60 | No Match |

Threshold can be tuned based on business requirements.

---

# Performance Considerations

Current implementation:

- CPU inference
- Single image verification
- No anti-spoofing
- No liveness detection

Future improvements:

- GPU inference
- Anti-spoofing integration
- Liveness detection
- Batch verification
- Docker deployment
- CI/CD pipeline

---

# Limitations

Current system does NOT detect:

❌ Phone screen replay attacks  
❌ Printed photos  
❌ Deepfake attacks  
❌ Mask attacks

Requires dedicated anti-spoof/liveness module.

---

# Future Roadmap

Planned:

- FaceTec integration
- CDCN++ anti-spoofing
- MiDaS depth estimation
- Blink detection
- Docker deployment
- Kubernetes deployment
- Monitoring + Logging

---

# Deployment

Run:

```bash
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

Production:

Use:

- Docker
- Nginx
- Gunicorn/Uvicorn Workers

---

# Author

**Shri Omm Das**

B.Tech Computer Science  
National Institute of Technology Rourkela

GitHub:

https://github.com/OMMNIT

---

# License

MIT License
