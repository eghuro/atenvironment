#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `atenvironment` package."""


import unittest
import os
import random
import string

from atenvironment.atenvironment import environment


class TestAtenvironment(unittest.TestCase):
    """Tests for `atenvironment` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_decorator(self):
        """Test decorator."""
        key = next(iter(os.environ.keys()))

        @environment(key)
        def test(key):
            return key

        self.assertEqual(test(), os.environ[key])

    def test_noKey(self):
        """Test decorator with no key in environment."""
        for _ in range(7):
            key = ''.join(random.choices(string.ascii_uppercase, k=random.randrange(42)))
            if key not in os.environ:
                break

        self.assertFalse(key in os.environ)

        @environment(key)
        def test(key):
            return key

        self.assertRaises(KeyError, test)
