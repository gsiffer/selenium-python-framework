from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import StatusTest
import time
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        """
        We added these lines "lp = LoginPage(driver), lp.login("test@email.com", "abcabc") and request.cls.lp = lp
        to confest.py. So we don't need self.lp = LoginPage(self.driver) line now. We are logged in.
        That's the start position.
        """
        self.cp = RegisterCoursesPage(self.driver)
        self.ts = StatusTest(self.driver)

    # Need to verify two verification points
    # 1 fails, code will not go to the next verification point
    # If assert fails, it stops current test execution and
    # moves to the next test method
    @pytest.mark.run(oreder=1)
    def test_invalid_card_details(self):
        self.cp.clickCoursesLink()
        self.cp.enterCourseName("JavaScript")
        self.cp.clickSearchButton()
        self.cp.selectCourseToEnroll("javascript-for-beginners")
        self.cp.enrollInCourse("123456", "1222", "122")

        result = self.cp.verifyEnrollFailed()
        self.ts.markFinal("test_invalid_card_details", result, "Enrollment Failed Verification")

        time.sleep(4)
