from django import forms
from . import utils
from .widgets import TurnstileWidget


class TurnstileField(forms.Field):
    widget = TurnstileWidget

    def validate(self, value):
        super().validate(value)

        if not utils.verify_turnstile_response(value):
            raise forms.ValidationError("Turnstile validation failed.")
