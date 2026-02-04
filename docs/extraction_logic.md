# Extraction Logic

The extraction engine identifies sensitive entities commonly
used in scam conversations.

## Supported Entities

- UPI IDs (e.g. ram@ybl)
- Bank account numbers
- IFSC codes
- Phone numbers
- Phishing URLs and domains

## Approach

- Regex-based pattern matching
- Deduplication of results
- Normalization of text where required

The extraction module is designed to be lightweight,
fast, and independent of any ML model.
