# FVS_V2 — Face Verification Service (UAT)

## Overview

FVS_V2 is a REST API service for **face verification between KYC identity images and live images** using **ArcFace embeddings** and **cosine similarity scoring**.

The service is intended for:

- KYC verification
- Identity matching
- User onboarding workflows
- Authentication support systems

---

# Architecture

## High Level Flow

```txt
                         ┌──────────────┐
                         │ Client/API   │
                         └──────┬───────┘
                                │
                                ▼
                     ┌────────────────────┐
                     │ FastAPI Endpoint   │
                     │ POST /verify-face  │
                     └─────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │                             │
                ▼                             ▼
       ┌────────────────┐             ┌────────────────┐
       │ KYC Image      │             │ Live Image     │
       └──────┬─────────┘             └──────┬─────────┘
              │                              │
              ▼                              ▼
       ┌──────────────────────────────────────────┐
       │ Image Processing (OpenCV)               │
       └──────────────────────────────────────────┘
                              │
                              ▼
               ┌──────────────────────────┐
               │ ArcFace Embedding Model  │
               └──────────────┬───────────┘
                              │
                              ▼
               ┌──────────────────────────┐
               │ Cosine Similarity Score  │
               └──────────────┬───────────┘
                              │
                              ▼
               ┌──────────────────────────┐
               │ Threshold Evaluation     │
               └──────────────┬───────────┘
                              │
                              ▼
               ┌──────────────────────────┐
               │ MATCH / NO MATCH         │
               └──────────────────────────┘
```

---

# Components

| Module | Purpose |
|--------|----------|
| main.py | FastAPI startup |
| routes.py | API endpoints |
| embedding_service.py | ArcFace embedding extraction |
| similarity.py | Similarity calculation |
| quality_service.py | Image quality scoring |
| image_utils.py | Image preprocessing |

---

# Technology Stack

Backend:

- FastAPI
- Uvicorn

ML:

- ArcFace (InsightFace)
- ONNX Runtime

Processing:

- OpenCV
- NumPy

---

# API Specification

## Endpoint

### Verify Face

```http
POST /verify-face
```

Request:

Content-Type:

```txt
multipart/form-data
```

Parameters:

| Name | Type | Required |
|------|------|----------|
| kyc | image | Yes |
| live | image | Yes |
| threshold | float | Optional |

---

Response:

Success:

```json
{
  "decision":"MATCH",
  "similarity":0.84,
  "quality":0.78,
  "confidence":0.84
}
```

Failure:

```json
{
   "decision":"NO MATCH"
}
```

---

# Installation

Clone:

```bash
git clone https://github.com/OMMNIT/FVS_V2.git

cd FVS_V2
```

Create venv:

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Install:

```bash
pip install -r requirements.txt
```

---

# Run Locally

```bash
python -m uvicorn main:app --reload
```

Swagger:

```txt
http://localhost:8000/docs
```

---

# UAT Deployment

## Start Service

Use:

```bash
uvicorn main:app \
--host 0.0.0.0 \
--port 8000 \
--workers 4
```

Recommended:

Reverse proxy:

```txt
Nginx
```

Application:

```txt
FastAPI + Uvicorn
```

---

# Environment Requirements

Python:

```txt
Python 3.11+
```

Memory:

```txt
Minimum:
4 GB RAM

Recommended:
8+ GB
```

CPU:

```txt
4 cores+
```

---

# Health Check

Endpoint:

```http
GET /
```

Response:

```json
{
 "message":
 "Face Verification API Running"
}
```

---

# Logging

Recommended:

Capture:

- Request IDs
- Similarity scores
- Errors
- Response times

Do NOT log:

- Face images
- Embeddings
- Sensitive user data

---

# Limitations

Current version DOES NOT include:

- Anti-spoofing
- Liveness detection
- Replay attack detection
- Deepfake detection

---

# Security Notes

Images must be:

- Deleted after processing
- Never persisted
- Transmitted via HTTPS only

---

# Future Enhancements

Planned:

- Anti-spoofing
- FaceTec integration
- Depth estimation
- Dockerization
- Kubernetes deployment
- Monitoring dashboards

---

# Rollback Plan

Rollback:

Deploy previous stable container/version.

Verify:

```txt
GET /
```

before routing traffic.

---

# Author

Shri Omm Das

NIT Rourkela