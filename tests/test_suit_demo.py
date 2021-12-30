import unittest
from tests.home.login_tests import LoginTest
from tests.courses.register_courses_csv_data import  RegisterCoursesCSVDataTest

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTest)

# Create a test suit combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner(verbosity=2).run(smokeTest)