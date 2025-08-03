from fastapi import FastAPI
from pydantic import BaseModel
from app.retriever import Retriever
from app.schema import AnswerResponse
from app.utils import classify_category, compute_confidence, build_answer

#FastAPI app initialization
app = FastAPI()

#load documents and setup TF-IDF model on app startup
retriever = Retriever()

#input format for /ask endpoint
class QuestionRequest(BaseModel):
    question: str

#/ask endpoint:- accepts a question and returns structured JSON
@app.post("/ask", response_model=AnswerResponse)
def ask_question(req: QuestionRequest):
    #retrieve top matching documents
    results = retriever.get_top_docs(req.question)

    #classify question into a category
    category = classify_category(req.question)

    #format source documents (doc + snippet)
    sources = [{"doc": r["doc"], "snippet": r["snippet"]} for r in results]

    #build answer string from sources
    answer = build_answer(sources)

    #estimate confidence using similarity score
    confidence = compute_confidence(results[0]["score"], results[0]["max_score"]) if results else 0.0

    #return the structured response
    return AnswerResponse(answer=answer, category=category, confidence=confidence, sources=sources)
