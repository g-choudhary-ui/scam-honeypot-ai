from backend.extraction.risk_score import calculate_risk

def detect_scam(message: str, extracted: dict) -> dict:
    return calculate_risk(extracted, message)
