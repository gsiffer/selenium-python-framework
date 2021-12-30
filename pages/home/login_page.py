from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
from pages.home.navigation_page import NavigationPage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.nav = NavigationPage(self.driver)
        # self.driver = driver

    # Locators
    _login_link = "SIGN IN"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@type='submit']"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="id")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        # if not isLoginPageOpen:
        #     self.clickLoginLink()
        self.clickLoginLink()
        self.clearField(locator=self._email_field)
        self.clearField(locator=self._password_field)
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//button[@id='dropdownMenu1']//span[text()='My Account']",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.waitForElement("//span[text()='Your username or password is invalid. Please try again.']",
                            locatorType="xpath", pollFrequency=1)
        self.isElementPresent(element=result)
        # result = self.isElementPresent("//span[text()='Your username or password is invalid. Please try again.']",
        #                                locatorType="xpath")
        return result

    def verifyTitle(self):
        return self.verifyPageTitle("My Courses")

    def logout(self):
        self.nav.navigateToDropDownMenu()
        self.elementClick("Logout", "link")