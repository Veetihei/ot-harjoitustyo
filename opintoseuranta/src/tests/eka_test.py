import unittest
from build import build


def pytest_configure():
    build()
