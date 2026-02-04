# System Architecture

The Scam Honeypot AI system is divided into clear modules so that
each component can be developed and tested independently.

## High-level Flow

1. Incoming scam message is received (API or CLI demo)
2. Message is passed to the Honeypot Controller
3. Controller:
   - extracts entities (UPI, links, accounts)
   - checks scam indicators
   - generates a delayed honeypot reply
4. If high-risk data is detected, the system auto-stops
5. Final evidence is collected for review

## Main Components

- backend/extraction  
  Responsible for regex-based entity extraction

- backend/api  
  Orchestrates honeypot logic and optional FastAPI layer

- demo  
  CLI-based demo for judges

The architecture is modular to allow parallel development
and easy extension.
