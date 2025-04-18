from django.db import models
from wagtail.contrib.forms.forms import FormBuilder
from wagtail.contrib.forms.models import AbstractFormField, FORM_FIELD_CHOICES
from .forms import TurnstileField


class TurnstileAbstractFormField(AbstractFormField):
    field_type = models.CharField(
        verbose_name='field type',
        max_length=16,
        choices=FORM_FIELD_CHOICES + (
            ("turnstile", "Captcha"),
        )
    )


class TurnstileFormBuilder(FormBuilder):
    def create_turnstile_field(self, field, options):
        return TurnstileField(**options)
