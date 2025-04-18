# Wagtail Turnstile

A lightweight Cloudflare Turnstile integration for Wagtail form pages.  
Drop-in support with minimal configuration — and no Google reCAPTCHA required.

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/wagtail-turnstile)
![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)

---

## Features

- Adds a Turnstile field type to Wagtail’s form builder
- Validates Turnstile submissions server-side

---

## Installation

```bash
pip install wagtail-turnstile
```

Then add it to your Django settings:

```python
INSTALLED_APPS = [
    ...
    "turnstile",
]
```

Add your Cloudflare Turnstile site and secret keys to your settings.py:

```python
TURNSTILE_SITE_KEY = "your-site-key"
TURNSTILE_SECRET_KEY = "your-secret-key"
```

## Usage

Here's a sample contact form page and field. Subclassing
`TurnstileAbstractFormField` will add a new form field type,
labelled to the user as "Captcha". This will handle the challenge
and validation flow with Turnstile.

```python
from turnstile.models import TurnstileAbstractFormField, TurnstileFormBuilder

class FormField(TurnstileAbstractFormField):
    page = ParentalKey(
        "ContactPage",
        on_delete=models.CASCADE,
        related_name="form_fields"
    )

class ContactPage(AbstractEmailForm):
    form_builder = TurnstileFormBuilder
```

## Todo

Quite a lot, I would assume. It probably needs to be more
customisable, and we don't need to store the Turnstile token.

## Got any suggestions?

Feel free to raise an issue, and if you have a fix, submit a merge
request and I'll be glad to take a look.
