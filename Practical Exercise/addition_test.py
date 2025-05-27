import addition_function
from unittest import TestCase

class  Addition_Testing(TestCase):
	def test_that_addition_function_exists(self):
		addition_function.addition(16, 14)



class Subtraction_Test(TestCase):
	def test_that_subtraction_function_exists(self):
		subtraction_function.subtraction(10, 20)