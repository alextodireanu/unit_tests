# write a class called Employee. the __init__ method should take in a first name, last name and annual salary and
# store each of these as attributes. Write a method called give_raise that adds $5000 by default but also accepts
# a different raise amount.
# Write a test case for Employee. Write 2 test methods, test_give_default_raise and test_give_custom_raise. Use the
# setUp method so you don't have to create a new employee instance in each test method. Run your test case and make sure
# both tests pass.


class Employee:
    """Representation of an employee"""
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, custom_raise=''):
        """Method to raise the annual salary by default or custom amount"""
        if custom_raise:
            self.annual_salary += custom_raise
        else:
            self.annual_salary += 5000
