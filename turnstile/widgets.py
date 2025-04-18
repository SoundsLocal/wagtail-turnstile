from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.forms import widgets


class TurnstileWidget(widgets.Widget):
    template_name = "turnstile/turnstile_widget.html"

    def get_context(self, name, value, attrs):
        if not hasattr(settings, "TURNSTILE_SITE_KEY"):
            raise ImproperlyConfigured(
                "Missing required setting 'TURNSTILE_SITE_KEY'"
            )

        return {
            **super().get_context(name, value, attrs),
            "site_key": settings.TURNSTILE_SITE_KEY
        }
