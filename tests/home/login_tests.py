from pages.home.login_page import LoginPage
from utilities.teststatus import StatusTest
import time
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        """
        We added these lines "lp = LoginPage(driver), lp.login("test@email.com", "abcabc") and request.cls.lp = lp
        to confest.py. So we don't need self.lp = LoginPage(self.driver) line now. We are logged in.
        That's the start position.
        """
        # self.lp = LoginPage(self.driver)
        self.ts = StatusTest(self.driver)

    # Need to verify two verification points
    # 1 fails, code will not go to the next verification point
    # If assert fails, it stops current test execution and
    # moves to the next test method
    @pytest.mark.run(oreder=2)
    def test_validLogin(self):

        self.lp.login("test@email.com", "abcabc")

        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "Title verified")

        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login was successful")

        time.sleep(2)

    @pytest.mark.run(oreder=1)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.login("test@email.com", "abcabcabc")

        result = self.lp.verifyLoginFailed()
        self.ts.markFinal("test_invalidLogin", result, "Login was not successful")

        time.sleep(2)
