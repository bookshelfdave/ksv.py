#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `ksv` package."""


import unittest
from click.testing import CliRunner

from ksv import ksv
from ksv import cli

ENCODED_SECRET = """
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque
data:
  username: YWRtaW4=
  password: MWYyZDFlMmU2N2Rm
"""

DECODED_SECRET = """
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque
data:
  username: admin
  password: 1f2d1e2e67df
"""


class TestKsv(unittest.TestCase):
    """Tests for `ksv` package."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert 'Show this message and exit.' in help_result.output

    def test_decode(self):
        """Test decode."""
        runner = CliRunner()
        decode_result = runner.invoke(cli.main, input=ENCODED_SECRET)
        assert decode_result.exit_code == 0
        assert 'admin' in decode_result.output

    def test_encode(self):
        """Test encode."""
        runner = CliRunner()
        encode_result = runner.invoke(
            cli.main, ['--encode'], input=DECODED_SECRET)
        assert encode_result.exit_code == 0
        assert 'MWYyZDFlMmU2N2Rm' in encode_result.output
