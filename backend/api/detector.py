# detector.py

SCAM_KEYWORDS = [
    "send money",
    "urgent",
    "upi",
    "account blocked",
    "verify",
    "click link",
]

def detect_scam(text: str, extracted: dict) -> bool:
    text = text.lower()

    for keyword in SCAM_KEYWORDS:
        if keyword in text:
            return True

    if extracted.get("upi_ids") or extracted.get("phishing_links"):
        return True

    return False
