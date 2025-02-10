import unittest
from script import add

class TestAddition(unittest.TestCase):
    def test_sum_equals_10(self):
        test_cases = [
            (5, 5),
            (3, 7),
            (0, 10),
            (-2, 12)
        ]
        
        for a, b in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(add(a, b), 10, f"{a} + {b} должно быть равно 10")

if __name__ == '__main__':
    unittest.main()

