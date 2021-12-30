from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = driver

    # Locators
    _home ="HOME"
    _all_courses = "ALL COURSES"
    _support = "SUPPORT"
    _my_courses = "MY COURSES"
    _community = "COMMUNITY"
    _drop_down_menu = "dropdownMenu1"

    def navigateToAllCourses(self):
        self.elementClick(self._all_courses, "link")

    def navigateToDropDownMenu(self):
        self.elementClick(self._drop_down_menu)
