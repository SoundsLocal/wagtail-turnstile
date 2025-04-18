from setuptools import setup, find_packages


setup(
    name="wagtail-turnstile",
    version="0.1.0",
    description="Cloudflare Turnstile integration for Wagtail forms",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Mark Steadman",
    url="https://github.com/SoundsLocal/wagtail-turnstile",
    packages=find_packages(
        exclude=[
            "tests",
            "tests.*",
            "testproject"
        ]
    ),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Wagtail",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "Django>=3.2",
        "wagtail>=3.0",
        "requests>=2.0",
    ],
    python_requires=">=3.8"
)
