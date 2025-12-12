# tests/test_utils.py
"""
Unit tests for utility functions.
"""

import unittest
from src.pynote import utils


class TestUtils(unittest.TestCase):
    """Test cases for utility functions."""
    
    def test_count_words(self):
        """Test word counting."""
        self.assertEqual(utils.count_words("hello world"), 2)
        self.assertEqual(utils.count_words(""), 0)
        self.assertEqual(utils.count_words("one"), 1)
        self.assertEqual(utils.count_words("one two three"), 3)
    
    def test_count_chars(self):
        """Test character counting."""
        self.assertEqual(utils.count_chars("hello"), 5)
        self.assertEqual(utils.count_chars(""), 0)
        self.assertEqual(utils.count_chars("hello\n"), 5)  # Trailing newline removed
        self.assertEqual(utils.count_chars("hello\nworld"), 11)
    
    def test_get_config_dir(self):
        """Test config directory creation."""
        config_dir = utils.get_config_dir()
        self.assertTrue(config_dir.exists())
        self.assertTrue(config_dir.is_dir())
    
    def test_load_settings_default(self):
        """Test loading default settings."""
        settings = utils.load_settings()
        self.assertIn('theme', settings)
        self.assertIn('autosave', settings)
        self.assertIn('tab_size', settings)
        self.assertEqual(settings['theme'], 'light')


if __name__ == '__main__':
    unittest.main()

