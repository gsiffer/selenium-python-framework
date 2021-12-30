from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import StatusTest
import time
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from pages.home.navigation_page import NavigationPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        """
        We added these lines "lp = LoginPage(driver), lp.login("test@email.com", "abcabc") and request.cls.lp = lp
        to confest.py. So we don't need self.lp = LoginPage(self.driver) line now. We are logged in.
        That's the start position.
        """
        self.cp = RegisterCoursesPage(self.driver)
        self.ts = StatusTest(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourses()

    # Need to verify two verification points
    # 1 fails, code will not go to the next verification point
    # If assert fails, it stops current test execution and
    # moves to the next test method
    @pytest.mark.run(oreder=1)
    @data(*getCSVData("D:/Works/workspace_python/letskodeit/testdata.csv"))
    @unpack
    def test_invalid_card_details(self, courseName, ccNum, ccExp, ccCVV):

        self.cp.enterCourseName(courseName)
        self.cp.clickSearchButton()
        self.cp.selectCourseToEnroll(courseName)
        self.cp.enrollInCourse(ccNum, ccExp, ccCVV)

        result = self.cp.verifyEnrollFailed()
        self.ts.markFinal("test_invalid_card_details", result, "Enrollment Failed Verification")

        # self.driver.find_element(By.LINK_TEXT, 'ALL COURSES').click()

        time.sleep(4)


