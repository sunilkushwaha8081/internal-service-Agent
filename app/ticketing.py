import json
import uuid
from datetime import datetime
from pathlib import Path


TICKET_DIR = Path("tickets")
TICKET_DIR.mkdir(exist_ok=True)


def create_ticket(
    category: str,
    issue: str,
    priority: str,
    reason: str,
    source: str | None = None
):
    ticket_id = f"IT-{datetime.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:6].upper()}"

    ticket = {
        "ticket_id": ticket_id,
        "created_at": datetime.now().isoformat(),
        "category": category,
        "issue": issue,
        "priority": priority,
        "escalation_reason": reason,
        "source": source,
        "status": "OPEN"
    }

    file_path = TICKET_DIR / f"{ticket_id}.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(ticket, file, indent=2)

    return ticket