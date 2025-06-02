"""
Tests for the Kafka Mirror Kit CLI.

This module contains tests for the CLI interface defined in kmk.py.
"""

import os
import sys
import unittest

from click.testing import CliRunner

# Import the CLI module directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.cli.kmk import cli


class TestCLI(unittest.TestCase):
    """Test cases for the Kafka Mirror Kit CLI."""

    def setUp(self):
        """Set up test fixtures."""
        self.runner = CliRunner()

    def test_cli_help(self):
        """Test that the CLI help command works."""
        result = self.runner.invoke(cli, ['--help'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Kafka Mirror Kit CLI', result.output)

    def test_deploy_command(self):
        """Test that the deploy command works."""
        result = self.runner.invoke(cli, ['deploy'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Deploying Kafka clusters and MirrorMaker 2', result.output)

    def test_produce_command(self):
        """Test that the produce command works."""
        result = self.runner.invoke(cli, ['produce', '--topic', 'test-topic', '--messages', '5'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Producing 5 messages to topic \'test-topic\'', result.output)
        self.assertIn('on cluster \'primary\'', result.output)

    def test_consume_command(self):
        """Test that the consume command works."""
        result = self.runner.invoke(cli, ['consume', '--topic', 'test-topic', '--messages', '5'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Consuming 5 messages from topic \'test-topic\'', result.output)
        self.assertIn('on cluster \'secondary\'', result.output)

    def test_status_command(self):
        """Test that the status command works."""
        result = self.runner.invoke(cli, ['status'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Checking status of Kafka clusters and MirrorMaker 2', result.output)

    def test_destroy_command(self):
        """Test that the destroy command works."""
        result = self.runner.invoke(cli, ['destroy'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Destroying Kafka clusters and MirrorMaker 2', result.output)


if __name__ == '__main__':
    unittest.main()
