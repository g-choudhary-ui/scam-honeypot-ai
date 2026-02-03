# schemas.py

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import List, Optional


class InputMessage(BaseModel):
    type: str
    content: str


class ConversationItem(BaseModel):
    role: str
    message: str


class ExtractedData(BaseModel):
    upi_ids: List[str] = Field(default_factory=list)
    bank_accounts: List[str] = Field(default_factory=list)
    ifsc_codes: List[str] = Field(default_factory=list)
    phone_numbers: List[str] = Field(default_factory=list)
    phishing_links: List[str] = Field(default_factory=list)

class FinalResponse(BaseModel):
    is_scam: bool
    persona_used: Optional[str] = None
    conversation: List[ConversationItem] = Field(default_factory=list)
    extracted_data: ExtractedData