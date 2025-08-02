# test_futurenarrative.py
"""
Tests for FutureNarrative module.
"""

import unittest
from futurenarrative import FutureNarrative

class TestFutureNarrative(unittest.TestCase):
    """Test cases for FutureNarrative class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FutureNarrative()
        self.assertIsInstance(instance, FutureNarrative)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FutureNarrative()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
