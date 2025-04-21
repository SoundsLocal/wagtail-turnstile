from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.forms import widgets


class TurnstileWidget(widgets.Widget):
    template_name = "turnstile/turnstile_widget.html"

    def __init__(self, *args, **kwargs):
        self.appearance = kwargs.pop("appearance", "always")

        if self.appearance not in ("always", "execute", "interaction-only"):
            raise ImproperlyConfigured(
                "Widget appearance must be set to "
                "'always', 'exeucte', or 'interaction-only'."
            )

        super().__init__(*args, **kwargs)

    @property
    def is_hidden(self):
        return self.appearance == "interaction-only"

    def get_context(self, name, value, attrs):
        if not hasattr(settings, "TURNSTILE_SITE_KEY"):
            raise ImproperlyConfigured(
                "Missing required setting 'TURNSTILE_SITE_KEY'"
            )

        return {
            **super().get_context(name, value, attrs),
            "appearance": self.appearance,
            "site_key": settings.TURNSTILE_SITE_KEY
        }
