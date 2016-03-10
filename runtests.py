#!/usr/bin/env python
"""
Module to run test suite.
"""

import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner


def main():
    """
    Function to house main logic of running tests.
    """
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'
    django.setup()
    testrunner = get_runner(settings)
    test_runner = testrunner()
    failures = test_runner.run_tests(["tests"])
    sys.exit(bool(failures))


if __name__ == "__main__":
    main()
