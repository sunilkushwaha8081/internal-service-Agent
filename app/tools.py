from app.knowledge_base import search_knowledge_base
from app.ticketing import create_ticket
from app.audit import log_event


RISK_KEYWORDS = [
    "hacked",
    "compromised",
    "stolen",
    "phishing",
    "malware",
    "ransomware",
    "disable mfa",
    "bypass security",
    "admin password",
    "administrator password"
]


def detect_risk(message: str) -> bool:
    message_lower = message.lower()

    return any(
        keyword in message_lower
        for keyword in RISK_KEYWORDS
    )


def needs_password_escalation(message: str) -> bool:
    message_lower = message.lower()

    password_terms = [
        "forgot my password",
        "forgot password",
        "can't reset",
        "cannot reset",
        "unable to reset",
        "can't complete the password reset",
        "cannot complete the password reset",
        "unable to complete the password reset",
        "reset is not working",
        "password reset is not working"
    ]

    return any(
        term in message_lower
        for term in password_terms
    )


def categorize_issue(message: str) -> str:
    message_lower = message.lower()

    if "vpn" in message_lower:
        return "VPN"

    if "password" in message_lower:
        return "PASSWORD"

    if "wifi" in message_lower or "internet" in message_lower:
        return "NETWORK"

    if "email" in message_lower or "outlook" in message_lower:
        return "EMAIL"

    if "printer" in message_lower:
        return "PRINTER"

    if "laptop" in message_lower or "computer" in message_lower:
        return "HARDWARE"

    if "software" in message_lower or "install" in message_lower:
        return "SOFTWARE"

    if "access" in message_lower:
        return "ACCESS"

    return "GENERAL"


def process_issue(message: str):
    category = categorize_issue(message)

    # -----------------------------------------
    # 1. High-risk / security-sensitive request
    # -----------------------------------------
    if detect_risk(message):
        ticket = create_ticket(
            category=category,
            issue=message,
            priority="HIGH",
            reason="Potential security-sensitive or risky request"
        )

        log_event(
            employee_message=message,
            category=category,
            action="ESCALATE",
            result="High-risk issue escalated",
            ticket_id=ticket["ticket_id"]
        )

        return {
            "status": "ESCALATED",
            "category": category,
            "message": (
                "This request requires human IT/security support. "
                "I have created a high-priority ticket."
            ),
            "ticket_id": ticket["ticket_id"],
            "ticket": ticket
        }

    # -----------------------------------------
    # 2. Password reset escalation
    # -----------------------------------------
    if needs_password_escalation(message):
        ticket = create_ticket(
            category=category,
            issue=message,
            priority="MEDIUM",
            reason="Employee unable to complete password reset"
        )

        log_event(
            employee_message=message,
            category=category,
            action="ESCALATE",
            result="Password reset issue escalated to IT",
            ticket_id=ticket["ticket_id"]
        )

        return {
            "status": "ESCALATED",
            "category": category,
            "message": (
                "I couldn't complete the password reset request. "
                "I have escalated it to IT support and created a ticket."
            ),
            "ticket_id": ticket["ticket_id"],
            "ticket": ticket
        }

    # -----------------------------------------
    # 3. Search approved knowledge base
    # -----------------------------------------
    results = search_knowledge_base(message)

    # -----------------------------------------
    # 4. No approved solution found
    # -----------------------------------------
    if not results:
        ticket = create_ticket(
            category=category,
            issue=message,
            priority="MEDIUM",
            reason="No approved internal resolution found"
        )

        log_event(
            employee_message=message,
            category=category,
            action="ESCALATE",
            result="No approved knowledge-base article found",
            ticket_id=ticket["ticket_id"]
        )

        return {
            "status": "ESCALATED",
            "category": category,
            "message": (
                "I couldn't find an approved internal procedure "
                "for this issue, so I've escalated it to IT."
            ),
            "ticket_id": ticket["ticket_id"],
            "ticket": ticket
        }

    # -----------------------------------------
    # 5. Approved policy/resolution found
    # -----------------------------------------
    best_match = results[0]

    log_event(
        employee_message=message,
        category=category,
        action="SEARCH_KNOWLEDGE_BASE",
        result="Relevant policy found",
        source=best_match["name"]
    )

    return {
        "status": "RESOLVED_GUIDANCE",
        "category": category,
        "source": best_match["name"],
        "source_path": best_match["path"],
        "resolution": best_match["content"]
    }