#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# Modern, safe dependency list
requirements = [
    "requests>=2.25.0",
    "whois",
    "scapy",
    "pycryptodomex",
    "duckduckgo-search",
    # GeoIP libraries are deprecated; leaving optional
]

setup(
    name="ufonet-remastered",
    version="1.0.0",
    description="Modernized UFONet-style research toolkit (safe, updated, no sudo magic)",
    author="Shane",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "ufonet=ufonet.main:main",
        ]
    },
    python_requires=">=3.8",
)
