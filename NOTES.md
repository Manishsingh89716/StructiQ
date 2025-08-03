```md
#Architecture & Notes

This API accepts a question and returns a structured answer using local markdown documents.

---

##🧱Components

- `main.py`:- `/ask` endpoint
- `retriever.py`:- TF-IDF search over markdowns
- `utils.py`:- Category, confidence, and answer logic
- `schema.py`:- Strict output schema (Pydantic)
- `loader.py`:- Loads docs from /data

---

##⚙️Key Design Choices

- **TF-IDF + cosine** for fast local search
- **Keyword-based categorization** (simple & explainable)
- **Confidence score** = normalized similarity
- Response matches `answer_schema.json` exactly

---

##⚖️Trade-Offs

| Decision     | Why                       |
|--------------|----------------------------|
| No LLM       | Fast, local, cost-free     |
| No vector DB | Simpler for small corpus   |
| Rule-based   | Transparent & testable     |

---

##🔮Possible Improvements

- Use FAISS/vector DB
- Add LLM for richer answers
- Train classifier for category
- Add eval loop with `eval_questions.jsonl`