import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Test case for Employee class"""

    def setUp(self):
        """Create an employee to use in all test methods"""
        self.employee = Employee('john', 'davis', 40000)

    def test_give_default_raise(self):
        """Test for the give_raise method with the default amount"""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 45000)

    def test_give_custom_raise(self):
        """Test for the give_raise method with the custom amount"""
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 50000)


if __name__ == '__main__':
    unittest.main()
