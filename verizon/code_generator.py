from datetime import date, datetime
from decimal import Decimal, getcontext
from math import factorial
import logging

logging.basicConfig(filename='output.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


class CodeGenerator:
    """This a class to generate a 4 digit random code number."""

    def calculate_n1(self):
        """Calculate sum of day,month and year and set n_1"""

        today = date.today()
        logging.debug("Today's date:", today)

        year = today.strftime("%Y")
        month = today.strftime("%m")
        day = today.strftime("%d")
        n_1 = int(day) + int(month) + int(year[-2:])

        logging.debug("sum of YY+MM+DD : ", n_1)

        #self.n_values_list.append(n_1)
        return n_1

    def calculate_n2(self):
        """Calculate sum of hour, minute and seconds and set n_2"""

        now = datetime.now()
        current_hour = now.strftime("%H")
        current_minute = now.strftime("%M")
        current_second = now.strftime("%S")
        logging.debug("Current Time =", current_hour, ":", current_minute, ":", current_second)
        n_2 = int(current_hour) + int(current_minute) + int(current_second)
        logging.debug("sum of time: ", n_2)

        #self.n_values_list.append(n_2)
        return n_2

    @staticmethod
    def sum_digits_number(number):
        """Calculate sum of digits in a number and return the total"""
        total = 0
        while number > 0:
            total = total + int(number % 10)
            number = int(number / 10)

        return total

    def calculate_n3(self):
        """Calculate sum of rounded 5 digits in decimal part of seconds value"""

        now = datetime.now()
        current_second = now.strftime("%S.%f")
        logging.debug("current second", current_second)
        current_second = round(float(current_second), 5)
        decimal_part = str(current_second)
        decimal_part = decimal_part.split(".")
        decimal_part = int(decimal_part[-1])
        n_3 = self.sum_digits_number(decimal_part)
        logging.debug("sum of rounded 5 digits: ", n_3)

        #self.n_values_list.append(total)
        return n_3

    def calculate_n4(self, n_1, n_2, n_3):
        """calculate n_4 using n_1+n_2+n3 mod 7 formula"""

        n_4 = sum(n_1, n_2, n_3) % 7
        logging.debug("n_4 :", n_4)
        #self.n_values_list.append(n_4)
        return n_4

    @staticmethod
    def get_nth_digit(pi, position):
        """Get the digit in the decimal part of pi value at given position"""

        pi = str(pi)
        decimal = pi.split(".")[-1]
        value = decimal[position - 1]
        return int(value)

    def get_pi_value(self, n_1, n_2, n_3, n_4):
        """Calculate pi value and return"""

        maximum = max(n_1, n_2, n_3, n_4)
        getcontext().prec = maximum + 1
        pi = Decimal(0)

        for k in range(maximum):
            numerator = ((-1) ** k) * (factorial(6 * k) * (13591409 + 545140134 * k))
            denominator = factorial(3 * k) * (factorial(k) ** 3) * (640320 ** (3 * k))
            pi += Decimal(numerator) / Decimal(denominator)
        pi = pi * Decimal(12) / Decimal(640320 ** Decimal(1.5))
        pi = 1 / pi

        logging.debug("value of pi is : ", pi)
        return pi

    def generate_random_number(self):
        """Generate 4 digit random number using n_1, n_2, n_3 and n_4"""

        n_1 = self.calculate_n1()
        n_2 = self.calculate_n2()
        n_3 = self.calculate_n3()
        n_4 = self.calculate_n4(n_1, n_2, n_3)
        new_random_number = 0
        pi = self.get_pi_value(n_1, n_2, n_3,n_4)
        k = 0
        for n in [n_1,n_2,n_3,n_4]:
            value = self.get_nth_digit(pi, n)
            new_random_number += value * (10 ** k)
            k += 1

        #print("new random number", new_random_number)
        #self.random_number = new_random_number
        return new_random_number
