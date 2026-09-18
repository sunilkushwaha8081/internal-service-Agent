from app.ticketing import create_ticket


def test_ticket_creation():

    ticket = create_ticket(
        category="VPN",
        issue="VPN authentication failed",
        priority="MEDIUM",
        reason="Authentication failure"
    )

    assert ticket["ticket_id"].startswith("IT-")
    assert ticket["status"] == "OPEN"