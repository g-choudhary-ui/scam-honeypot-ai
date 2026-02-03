import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from backend.extraction.extractor import extract_entities
from backend.extraction.risk_score import calculate_risk_score

print("=== Scam Honeypot AI Demo ===\n")

sample_text = """
Madam aapka KYC pending hai
UPI id ram @ ybl pe payment karein
Account XXXX96321478
IFSC sbin0001234
Visit secure-kyc-update.in/login
"""

print("📩 Incoming Scammer Message:")
print(sample_text)

entities = extract_entities(sample_text)
risk = calculate_risk_score(entities)

print("\n🔍 Extracted Evidence:")
for key, value in entities.items():
    print(f"{key}: {value}")

print("\n⚠️ Risk Assessment:")
print(f"Risk Level: {risk['risk_level']}")
print(f"Risk Score: {risk['risk_score']}")
