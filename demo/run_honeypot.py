# run_honeypot.py
import sys
import os

# allow imports from project root
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from backend.api.controller import HoneypotController


PERSONA = """You are a 65-year-old Indian retired man.
You are polite, soft-spoken, and slightly confused with smartphones and online payments.
You understand basic Hindi and English but speak mainly in Hinglish (Hindi in English letters).

Your behavior rules:
- Always reply in Hinglish (Hindi written in English letters)
- Speak slowly and politely like an elderly person
- Get confused by technical terms like UPI, links, OTP, apps
- Ask the other person to repeat things slowly
- Never say you are an AI or chatbot
- Never sound confident about technology
- Never refuse directly
- Do not introduce unrelated stories unless it helps delay the conversation

You are not trying to stop the scam.
Your goal is only to understand what the other person is saying.
"""

GOAL = "Make the other person repeat the UPI ID slowly."

controller = HoneypotController(PERSONA, GOAL)

print("\n--- HCL HONEYPOT LIVE (CLI DEMO) ---")
print("Type 'exit' to stop manually.\n")

while True:
    scammer_msg = input("Scammer: ").strip()

    if scammer_msg.lower() == "exit":
        print("\n[SESSION TERMINATED BY USER]")
        break

    reply = controller.process_message(scammer_msg)
    print(f"\nHoneypot: {reply}\n")

    if controller.stop_chat:
        print("\n[HONEYPOT AUTO-STOP — DATA CAPTURED]")
        break


# ===== FINAL SUMMARY FOR JUDGES =====
final = controller.finalize()

print("\n====== FINAL OUTPUT (JUDGE VIEW) ======")
print(f"Is Scam Detected: {final.is_scam}")
print(f"Persona Used: {final.persona_used}\n")

print("Conversation:")
for item in final.conversation:
    print(f"{item.role.upper()}: {item.message}")

print("\nExtracted Evidence:")
extracted = final.extracted_data
print(f"UPI IDs: {extracted.upi_ids}")
print(f"Bank Accounts: {extracted.bank_accounts}")
print(f"IFSC Codes: {getattr(extracted, 'ifsc_codes', [])}")
print(f"Phone Numbers: {getattr(extracted, 'phone_numbers', [])}")
print(f"Phishing Links: {extracted.phishing_links}")
