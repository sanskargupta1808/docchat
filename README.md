# 🧠 DocChat AI

DocChat AI is a full-stack intelligent documentation assistant powered by GPT and RAG (Retrieval-Augmented Generation). It allows users to upload documents (PDF/Text), query them through a chat interface, and receive context-aware answers. It includes a secure admin dashboard and multi-method authentication (Email, Google, Phone).

---

## 📁 Project Structure

docchat/
├── backend/                  # FastAPI Backend (Deployed on Cloud Run)
│   ├── main.py
│   ├── routes/
│   ├── services/
│   ├── models/
│   ├── firebase-service-account.json (excluded from GitHub)
│   ├── .env                  # Stores secrets (excluded from GitHub)
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/                 # Frontend (Hosted via Firebase or GitHub Pages)
│   ├── index.html
│   ├── user-login.html
│   ├── admin-login.html
│   ├── user.html
│   ├── admin.html
│   └── assets/ (if any)

---

## 🚀 Live Demo

- 🌐 **Frontend:** [your-frontend-link]
- ⚙️ **Backend (API):** [your-cloud-run-endpoint]

---

## 🛠️ Setup Instructions

### Backend (FastAPI + RAG)

#### 1. Clone the Repo

```bash


git clone https://github.com/your-username/docchat-ai.git
cd docchat-ai/backend

2. Create Virtual Environment

python3 -m venv env
source env/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Add Required Files
	•	.env:

OPENAI_API_KEY=your-key
FIREBASE_PROJECT_ID=your-firebase-id

	•	firebase-service-account.json: Download from Firebase Console → Project Settings → Service Accounts.

5. Run Backend

uvicorn main:app --host 0.0.0.0 --port 8080

6. Deploy on Google Cloud Run

gcloud run deploy docchat-backend \
  --source . \
  --platform managed \
  --region asia-south1 \
  --allow-unauthenticated \
  --port 8080


⸻

Frontend (HTML + Firebase)

1. Open frontend/ folder

Make sure you’ve configured Firebase Hosting:

firebase login
firebase init hosting
firebase deploy

You can also deploy on GitHub Pages or Netlify.

⸻

⚙️ Architecture Overview

[User/Admin] ⇄ [Frontend (HTML/CSS/JS)] ⇄ [FastAPI Backend] ⇄ [RAG Engine + GPT-4]
                                                          ⇓
                                             [PDF/Text Document Indexing via FAISS]
                                                          ⇓
                                              [Firebase for Auth + Storage + Logs]


⸻

📌 Core Features
	•	📤 Document upload (PDFs/Text)
	•	🔍 Semantic search with FAISS & sentence-transformers
	•	🤖 GPT-4 powered chat with context-based document retrieval
	•	🔐 Firebase Auth: Email, Google, Phone, Anonymous
	•	📊 Admin dashboard with analytics & user monitoring
	•	🎨 Simple and intuitive chat UI (user.html)

⸻

📡 API Usage Guidelines

GET /

Check server status.

{
  "message": "DocChat Backend is Live!"
}


⸻

POST /files/upload

Upload a document (PDF or Text).

Form data: file: File

⸻

POST /chat/query

Send a query to the document chat assistant.

{
  "query": "What is the refund policy?",
  "doc_id": "document_xyz"
}


⸻

GET /analytics/queries

Get all queries for a specific document/user.

⸻

📦 Dependencies

From requirements.txt:
	•	fastapi, uvicorn, pydantic, python-dotenv, firebase-admin
	•	openai, faiss-cpu, sentence-transformers, langchain
	•	PyPDF2, PyMuPDF, aiofiles, requests, SQLAlchemy, tqdm, etc.

⸻

🔒 Security
	•	.env and firebase-service-account.json are excluded from GitHub.
	•	Environment variables used to manage secrets on deployment.

⸻

🧠 Powered By
	•	OpenAI GPT-4
	•	LangChain
	•	Firebase
	•	Google Cloud Run

⸻

📬 Contact

For any queries or contributions, reach out to:

Sanskar Gupta
📧 sanskarsg38@gmail.com
🌐 https://sanskarsgupta.netlify.app
https://github.com/sanskargupta1808
⸻
