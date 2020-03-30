from datetime import date, datetime
from decimal import Decimal,getcontext
import math
import unittest
from unittest.mock import patch


from verizon.code_generator import CodeGenerator


class TestCodeGenerator(unittest.TestCase):

    @patch('verizon.code_generator.date')
    def test_calculate_n1(self, mock_date):
        mock_date.today.return_value = date(2016, 1, 10)
        assert CodeGenerator.calculate_n1() == 27

        mock_date.today.return_value = date(2017, 1, 10)
        assert CodeGenerator.calculate_n1() == 28

    @patch('verizon.code_generator.datetime')
    def test_calculate_n2(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2020, 3, 29, 16, 33, 44, 646978)
        assert CodeGenerator.calculate_n2() == 93

    def test_sum_digits_number(self):
        self.assertEqual(CodeGenerator.sum_digits_number(150), 6)
        self.assertEqual(CodeGenerator.sum_digits_number(0), 0)

    @patch('verizon.code_generator.datetime')
    def test_calculate_n3(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2020, 3, 29, 16, 33, 44, 646978)
        cg = CodeGenerator()
        self.assertEqual(cg.calculate_n3(), 33)

    def test_calculate_n4(self):
        self.assertEqual(CodeGenerator.calculate_n4(30, 14, 23), 4)

    def test_get_nth_digit(self):
        pi = Decimal(math.pi)
        self.assertEqual(CodeGenerator.get_nth_digit(pi, 3), 1)
        self.assertEqual(CodeGenerator.get_nth_digit(pi, 4), 5)

    def test_get_pi_value(self):
        getcontext().prec = 7
        pi = Decimal('3.141593')
        self.assertEqual(CodeGenerator.get_pi_value(3, 4, 5, 6), pi)

    @patch('verizon.code_generator.CodeGenerator.calculate_n4',return_value=6)
    @patch('verizon.code_generator.CodeGenerator.calculate_n3',return_value=5)
    @patch('verizon.code_generator.CodeGenerator.calculate_n2',return_value=4)
    @patch('verizon.code_generator.CodeGenerator.calculate_n1', return_value=3)
    def test_generate_random_number(self, calculate_n1_function, calculate_n2_function, calculate_n3_function, calculate_n4_function):
        cg = CodeGenerator()
        self.assertEqual(cg.generate_random_number(), 3951)


if __name__ == '__main__':
    unittest.main()
