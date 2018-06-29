import unittest
import cap


class TestCap(unittest.TestCase):
    def test_one_word(self):
        result = cap.cap_text("python")
        self.assertEqual(result, "Python")

    def test_multiple_word(self):
        result = cap.cap_text("hello python")
        self.assertEqual(result, "Hello Python")


if __name__ == "__main__":
    unittest.main()
