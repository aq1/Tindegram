from pathlib import Path

import environ


ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent


env = environ.Env()
environ.Env.read_env(env.str('ENV_PATH', '.env'))


MONGO_HOST = env('MONGO_HOST')
MONGO_PORT = env('MONGO_PORT')
MONGO_DB = env('MONGO_DB')
MONGO_USER = env('MONGO_USER')
MONGO_PASSWORD = env('MONGO_PASSWORD')

TELEGRAM_TOKEN = env('TELEGRAM_TOKEN')
TELEGRAM_ADMINS = [
    int(_id)
    for _id in env.list('TELEGRAM_ADMINS')
    if _id.isdigit()
]


SENTRY_URL = env('SENTRY_URL')
