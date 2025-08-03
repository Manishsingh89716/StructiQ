from pydantic import BaseModel, Field
from typing import List, Optional, Literal

#format for each source used in the answer
class Source(BaseModel):
    #filename of the document
    doc: str
    #relevant text snippet
    snippet: Optional[str] = None

#full structured response format that match answer_schema.json
class AnswerResponse(BaseModel):
    answer: str
    category: Literal["api", "security", "pricing", "support", "other"]
    confidence: float = Field(..., ge=0.0, le=1.0)
    sources: List[Source] = []
