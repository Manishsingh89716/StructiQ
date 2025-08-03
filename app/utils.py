#classify question into one of the five categories
def classify_category(question: str) -> str:
    q = question.lower()
    if "price" in q or "cost" in q:
        return "pricing"
    elif "api" in q or "endpoint" in q:
        return "api"
    elif "secure" in q or "compliance" in q:
        return "security"
    elif "support" in q or "faq" in q:
        return "support"
    return "other"

#estimate confidence score (0.0 to 1.0) based on similarity
def compute_confidence(score: float, max_score: float) -> float:
    if max_score == 0:
        return 0.0
    normalized = score / max_score
    return round(min(1.0, max(0.5, normalized)), 2)

#create a natural-language answer from sources
def build_answer(sources: list) -> str:
    if not sources:
        return "Sorry, I couldn't find a relevant answer."
    return "\n\n".join(
        f"From {src['doc']}: {src['snippet'].strip()}" for src in sources
    )
