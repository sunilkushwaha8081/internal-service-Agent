import json
from datetime import datetime
from pathlib import Path


AUDIT_DIR = Path("audit_logs")
AUDIT_DIR.mkdir(exist_ok=True)

AUDIT_FILE = AUDIT_DIR / "audit.jsonl"


def log_event(
    employee_message: str,
    category: str,
    action: str,
    result: str,
    source: str | None = None,
    ticket_id: str | None = None
):
    event = {
        "timestamp": datetime.now().isoformat(),
        "employee_message": employee_message,
        "category": category,
        "action": action,
        "result": result,
        "source": source,
        "ticket_id": ticket_id
    }

    with open(AUDIT_FILE, "a", encoding="utf-8") as file:
        file.write(json.dumps(event) + "\n")