import time

from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
from selenium.webdriver import ActionChains


class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    # _all_courses_xpath = "//a[text()='ALL COURSES']"
    _search_box_name = "course"
    _search_button_xpath = "//button[@type='submit']"
    # _course_xpath = "//div[@id='course-list']//a[@href='/courses/{0}']"
    _course_xpath = "//div[@id='course-list']//a[@*]//h4[contains(text(), '{0}')]"
    _enroll_button_xpath = "//button[text()='Enroll in Course']"
    _cc_num_xpath = "//input[@name='cardnumber' and contains(@class, 'InputElement')]"
    _cc_exp_name = "exp-date"
    _cc_cvv_name = "cvc"
    _submit_enroll_xpath = "//input[@id='gdpr']/parent::div/following-sibling::button"
    _enroll_error_message = "//span[text()='Your card number is incomplete.']"

    # def clickCoursesLink(self):
    #     self.elementClick(self._all_courses_xpath, locatorType="xpath")

    def enterCourseName(self, name):
        self.sendKeys(name, self._search_box_name, locatorType="name")

    def clickSearchButton(self):
        self.elementClick(self._search_button_xpath, locatorType="xpath")

    def selectCourseToEnroll(self, fullCourseName):

        self.elementClick(self._course_xpath.format(fullCourseName), locatorType="xpath")

    def clickEnrollInCourseButton(self):

        enrollInCourseElement = self.waitForElement(locator=self._enroll_button_xpath, locatorType="xpath",
                                                    pollFrequency=1)
        self.elementClick(element=enrollInCourseElement)

        # self.elementClick(self._enroll_button_xpath, locatorType="xpath")

    def enterCardNum(self, num):
        # self.switchToFrame(name='__privateStripeFrame2155')
        self.switchFrameByIndex(self._cc_num_xpath, locatorType="xpath")
        self.sendKeys(num, self._cc_num_xpath, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        # self.switchToFrame(index=1)
        # expElement = self.waitForElement(self._cc_exp_name, locatorType="name")
        self.switchFrameByIndex(self._cc_exp_name, locatorType="name")
        self.sendKeys(exp, self._cc_exp_name, locatorType="name")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        # self.switchToFrame(index=2)
        self.switchFrameByIndex(self._cc_cvv_name, locatorType="name")
        self.sendKeys(cvv, self._cc_cvv_name, locatorType="name")
        self.switchToDefaultContent()

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        self.enterCardNum(num)

    def clickEnrollSubmitButton(self):
        self.elementClick(self._submit_enroll_xpath, locatorType="xpath")

    def enrollInCourse(self, num="", exp="", cvv=""):
        self.clickEnrollInCourseButton()
        self.webScroll('down')
        self.webScrollCustom(-200)
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        result = self.isElementPresent(self._enroll_error_message, locatorType="xpath")
        return result