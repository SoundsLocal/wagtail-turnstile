from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
import requests


CHALLENGE_URL = "https://challenges.cloudflare.com/turnstile/v0/siteverify"


def verify_turnstile_response(token):
    if not hasattr(settings, "TURNSTILE_SECRET_KEY"):
        raise ImproperlyConfigured(
            "Missing required setting 'TURNSTILE_SECRET_KEY'"
        )

    secret_key = settings.TURNSTILE_SECRET_KEY
    data = {
        "secret": secret_key,
        "response": token
    }

    response = requests.post(CHALLENGE_URL, data=data)
    response = response.json()
    print(response)

    return response.get("success", False)
