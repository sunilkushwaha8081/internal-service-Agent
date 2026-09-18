from app.knowledge_base import search_knowledge_base


def test_vpn_search():

    results = search_knowledge_base(
        "VPN authentication problem"
    )

    assert len(results) > 0


def test_password_search():

    results = search_knowledge_base(
        "forgot password"
    )

    assert len(results) > 0