# Structured Response AI API

A FastAPI-based service that answers questions using a local markdown knowledge base, and returns structured JSON matching a predefined schema.

---

## 🚀 Run Instructions

```bash
#Clone the project
cd StructiQ/

#Create a virtual environment
python -m venv venv && source venv/bin/activate

#Install dependencies
pip install -r requirements.txt

#Start the server
uvicorn app.main:app --reload

#Visit the port(for local environment testing)
http://127.0.0.1:8000/docs

#Visit the deployed link(for live demo)
https://structured-ai-api.onrender.com/docs

#Example
Request:- {"question": "What are the API rate limits?"}

Response:- {
  "answer": "...",
  "category": "api",
  "confidence": 0.85,
  "sources": [
    { "doc": "policy_api.md", "snippet": "Free: 20 req/min..." }
  ]
}
