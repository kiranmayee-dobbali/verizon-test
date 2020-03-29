import unittest
from verizon import code_generator as cg


class MyTestCase(unittest.TestCase):
    def test_something(self):
        obj1 = cg.CodeGenerator()
        result = obj1.sum_digits_number(00000)
        self.assertEqual(0, result)


if __name__ == '__main__':
    unittest.main()

