# DocChat

# 🧠 DocChat Backend

DocChat is an AI-powered document chat backend that enables users to upload files (PDFs, text), chat with the content using LLMs (e.g., GPT-4o), and gain insights. This is the backend for the DocChat platform, built using FastAPI, FAISS, Firebase, and LangChain.

---

## 🚀 Features

- Upload documents (PDF, TXT)
- Extract and chunk text
- Store in FAISS vector DB
- Query documents using OpenAI GPT
- Firebase Authentication
- Chat analytics & logging
- Cloud Run compatible

---

## 🛠️ Setup Instructions

### 🔧 Local Development

1. **Clone the repo**
   ```bash
   git clone https://github.com/sanskargupta1808/docchat-backend.git
   cd docchat-backend

	2.	Create a virtual environment

python3 -m venv env
source env/bin/activate


	3.	Install dependencies

pip install --upgrade pip
pip install -r requirements.txt


	4.	Create a .env file

OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4o
FIREBASE_CREDENTIAL_PATH=firebase-service-account.json


	5.	Add your firebase-service-account.json to the project root.
	6.	Run the server

uvicorn main:app --host 0.0.0.0 --port 8080


	7.	Access via:

http://localhost:8080/



⸻

#☁️ Google Cloud Run Deployment

Prerequisites: GCP account, gcloud CLI, billing enabled

	1.	Login & set project

gcloud auth login
gcloud config set project <your-project-id>


	2.	Enable required services

gcloud services enable run.googleapis.com cloudbuild.googleapis.com


	3.	Deploy

gcloud run deploy docchat-backend \
  --source . \
  --platform managed \
  --region asia-south1 \
  --allow-unauthenticated \
  --port 8080



⸻

#🧱 Architecture Overview

User
 │
 ├─ Upload Document (/files/upload)
 │    └─ PDF/Text → TextExtractor → Chunker → FAISS Vector Store
 │
 ├─ Ask Question (/chat/ask)
 │    └─ Question + Doc ID → Embed + Search → LangChain → GPT Response
 │
 └─ Firebase Auth → Secured Endpoints

Core Components:
	•	FastAPI: REST API layer
	•	FAISS: Local vector similarity DB
	•	OpenAI: GPT for answer generation
	•	LangChain: Chain & memory management
	•	Firebase: Authentication and user control
	•	SQLAlchemy + SQLite: Data logging

⸻

#📡 API Usage Guidelines

🔐 Authentication (Firebase)

All requests must be authenticated using a Firebase Bearer Token in headers:

Authorization: Bearer <token>


⸻

📁 /files

Upload File

POST /files/upload
	•	FormData: file (PDF/TXT)

Response:

{
  "message": "File uploaded and processed",
  "document_id": "abc123"
}


⸻

💬 /chat

Ask Question

POST /chat/ask

Body:

{
  "document_id": "abc123",
  "question": "What are the main ideas?"
}

Response:

{
  "response": "The main ideas are..."
}


⸻

📈 /analytics

GET /analytics/queries
	•	Get query logs per user/document

⸻

👥 /users

GET /users/me
	•	Get authenticated user details from Firebase

⸻

🔥 /test-firebase

GET /test-firebase
	•	Debug Firebase integration

⸻

📂 Project Structure

docchat-backend/
├── routes/
├── services/
├── models/
├── data/
├── uploads/
├── main.py
├── requirements.txt
├── firebase-service-account.json (NOT INCLUDED IN DEPLOY)
├── .env (NOT INCLUDED IN DEPLOY)


⸻

👨‍💻 Maintainer

Sanskar Gupta
GitHub: @sanskargupta1808

⸻

📄 License

MIT License
