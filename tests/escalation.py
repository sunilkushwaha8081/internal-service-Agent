from app.tools import detect_risk


def test_hacked_account():

    assert detect_risk(
        "I think someone hacked my account"
    )


def test_phishing():

    assert detect_risk(
        "I clicked a phishing link"
    )


def test_disable_mfa():

    assert detect_risk(
        "Please disable MFA"
    )


def test_normal_issue():

    assert not detect_risk(
        "My VPN is not working"
    )