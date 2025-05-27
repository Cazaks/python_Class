import cube
from unittest import TestCase

class TestCube(TestCase):
	def test_that_get_cube_function_exists(self):
		cube.get_cube(3)
	def test_that_get_cube_function_exists(self):
		actual = cube.get_cube(5)
		expected = 125
		self.assertEqual(actual, expected)
		actual = cube.get_cube(10)
		expected = 1000
		self.assertEquate(actual, expected)

	def test_that_get_cube_function_work_for_ number_between_1_to_(self):
		self.