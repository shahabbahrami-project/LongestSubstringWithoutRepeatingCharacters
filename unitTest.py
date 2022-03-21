import unittest
from main import LongestSubstring

class TestLongestSubstring(unittest.TestCase):

    def test_random_array(self):
        s1 = 'abgasdfsdfbcbddbacdef'
        s2 = 'abc'
        s3 = 'aaaa'
        s4 = 'abababa'
        self.assertEqual(LongestSubstring(s1), 6)
        self.assertEqual(LongestSubstring(s2), 3)
        self.assertEqual(LongestSubstring(s3), 1)
        self.assertEqual(LongestSubstring(s4), 2)

    def test_empty_array(self):
        self.assertEqual(LongestSubstring(''),0)


if __name__ == '__main__':
    unittest.main()
