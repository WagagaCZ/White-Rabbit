# Built-in
from os import environ
# 3rd-party
from dotenv import dotenv_values
from rabbit import WHITE_RABBIT_DIR

ENV_FILE = WHITE_RABBIT_DIR / ".env"

DEFAULTS = {
    "WHITE_RABBIT_TOKEN": "",
    "WHITE_RABBIT_LANGUAGE": "en",
    "WHITE_RABBIT_DEBUG": False,
    "WHITE_RABBIT_USE_LOCAL_IMAGES": False,
    "WHITE_RABBIT_PLAYSET": "base",
    "WHITE_RABBIT_STATS": True,
    "WHITE_RABBIT_PLAY_MUSIC": False,
}


def get_env_var(key: str):
    try:
        var = environ.get(key) or dotenv_values(ENV_FILE)[key]
        if not var:
            raise KeyError
        var = var.strip()
        if var.lower() == "true":
            return True
        if var.lower() == "false":
            return False

        return var
    except KeyError:
        return DEFAULTS.get(key)


TOKEN = get_env_var("WHITE_RABBIT_TOKEN")
LANGUAGE = get_env_var("WHITE_RABBIT_LANGUAGE")
DEBUG = get_env_var("WHITE_RABBIT_DEBUG")
USE_LOCAL_IMAGES = get_env_var("WHITE_RABBIT_USE_LOCAL_IMAGES")
PLAYSET = get_env_var("WHITE_RABBIT_PLAYSET")
TELEMETRY = get_env_var("WHITE_RABBIT_STATS")
MUSIC = get_env_var("WHITE_RABBIT_PLAY_MUSIC")
