import os
from typing import Optional

from requests.cookies import RequestsCookieJar

_user_cookies = {}


def is_user_registered(user: str) -> bool:
    return user in _user_cookies


def get_cookies_for_user(user: str) -> Optional[dict[str, str]]:
    return _user_cookies.get(user, None)


def set_cookies_for_user(user: str, cookies: RequestsCookieJar):
    for c in cookies:
        _user_cookies[user][c.name] = c.value


def register_user(user: str, remember_user_token_iris_prod: str, akshay_iris_session: str):
    _user_cookies[user] = {
        "remember_user_token_iris_prod": remember_user_token_iris_prod,
        "_akshay_IRIS_session": akshay_iris_session,
    }


def get_discord_bot_token() -> str:
    return os.environ["DISCORD_BOT_TOKEN"]
