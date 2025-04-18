from django import forms
from django.test import TestCase, override_settings
from turnstile.forms import TurnstileField
from unittest.mock import patch


class DummyForm(forms.Form):
    turnstile = TurnstileField()


class TurnstileFieldTests(TestCase):
    @patch("turnstile.utils.verify_turnstile_response", return_value=True)
    @override_settings(TURNSTILE_SITE_KEY="test_site")
    @override_settings(TURNSTILE_SECRET_KEY="test_secret")
    def test_valid_token_passes_validation(self, mock_verify):
        form = DummyForm(
            data={
                "turnstile": "valid_token"
            }
        )

        self.assertTrue(form.is_valid())
        mock_verify.assert_called_once_with("valid_token")

    @patch("turnstile.utils.verify_turnstile_response", return_value=False)
    @override_settings(TURNSTILE_SITE_KEY="test_site")
    @override_settings(TURNSTILE_SECRET_KEY="test_secret")
    def test_invalid_token_fails_validation(self, mock_verify):
        form = DummyForm(data={"turnstile": "invalid_token"})
        self.assertFalse(form.is_valid())
        self.assertIn("turnstile", form.errors)

    @override_settings(TURNSTILE_SITE_KEY="test_site")
    @override_settings(TURNSTILE_SECRET_KEY="test_secret")
    def test_missing_token_fails_validation(self):
        form = DummyForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("turnstile", form.errors)
