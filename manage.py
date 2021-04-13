import sentry_sdk

from bot import start_bot
import settings

if not settings.DEBUG:
    sentry_sdk.init(
        settings.SENTRY_URL,
        traces_sample_rate=0
    )

if __name__ == '__main__':
    start_bot()
