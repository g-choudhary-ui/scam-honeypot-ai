from typing import List
from backend.api.schemas import ConversationItem, FinalResponse, ExtractedData
from backend.extraction.extractor import extract_entities
from backend.api.detector import detect_scam
from backend.api.gemini_client import generate_reply


class HoneypotController:
    def __init__(self, persona: str, goal: str):
        self.persona_used = persona
        self.goal = goal

        self.conversation: List[ConversationItem] = []
        self.extracted = ExtractedData()
        self.is_scam = False
        self.stop_chat = False

    def process_message(self, scammer_message: str) -> str:

        self.conversation.append(
            ConversationItem(role="scammer", message=scammer_message)
        )

        # ✅ USE YOUR extractor (pure function)
        extracted_dict = extract_entities(scammer_message)

        # sync dict → pydantic model
        self.extracted = ExtractedData(**extracted_dict)

        # detect scam
        self.is_scam = detect_scam(scammer_message, extracted_dict)

        # auto-stop logic
        if self.extracted.upi_ids and not self.stop_chat:
            self.stop_chat = True

            final_reply = (
                "Achha beta… ruk jaiye. "
                "Main likh raha hoon sab details. "
                "Thodi der mein baat karta hoon."
            )

            self.conversation.append(
                ConversationItem(role="honeypot", message=final_reply)
            )

            return final_reply

        reply_text = generate_reply(
            self.persona_used,
            self.goal,
            scammer_message
        )

        self.conversation.append(
            ConversationItem(role="honeypot", message=reply_text)
        )

        return reply_text

    def finalize(self) -> FinalResponse:
        return FinalResponse(
            is_scam=self.is_scam,
            persona_used=self.persona_used,
            conversation=self.conversation,
            extracted_data=self.extracted,
        )
