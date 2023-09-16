from sparkdesk.completion import Authentication


def test_authorization_url():
    _authorization_url = Authentication(
        api_key="fake-key", api_secret="fake-secret"
    ).get_authorization_url()
    assert len(_authorization_url) > 50
