from app.tools import process_issue


def run_agent(message: str):
    if not message or not message.strip():
        return {
            "status": "NEEDS_CLARIFICATION",
            "message": "Please describe the IT issue you're experiencing."
        }

    return process_issue(message)