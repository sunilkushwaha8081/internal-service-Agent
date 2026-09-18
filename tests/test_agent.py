from app.agent import run_agent


def test_empty_message():

    result = run_agent("")

    assert result["status"] == "NEEDS_CLARIFICATION"


def test_security_escalation():

    result = run_agent(
        "Someone hacked my account"
    )

    assert result["status"] == "ESCALATED"
    assert "ticket_id" in result