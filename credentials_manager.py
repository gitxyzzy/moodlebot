import os

from requests.cookies import RequestsCookieJar

_cookies: dict[str, str] = {
    'remember_user_token_iris_prod': os.environ['REMEMBER_USER_TOKEN_IRIS_PROD'],
    '_akshay_IRIS_session': os.environ['AKSHAY_IRIS_SESSION'],
}


def get_cookies() -> dict[str, str]:
    return _cookies


def set_cookies(cookies: RequestsCookieJar):
    for c in cookies:
        _cookies[c.name] = c.value


def get_discord_bot_token() -> str:
    return os.environ['DISCORD_BOT_TOKEN']
