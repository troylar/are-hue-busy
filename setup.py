# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('arehuebusy/arehuebusy.py').read(),
    re.M
    ).group(1)


with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "cmdline-arehuebusy",
    packages = ["arehuebusy"],
    entry_points = {
        "console_scripts": ['arehuebusy = arehuebusy.arehuebusy:main']
        },
    version = version,
    description = "Simple script to set busy status with Philips Hue color bulb",
    long_description = long_descr,
    author = "Troy Larson",
    author_email = "troylar@gmail.com",
    url = "https://github.com/troylar/are-hue-busy",
    install_requires = ['phue','pyYaml']
    )
