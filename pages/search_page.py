from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage

class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.explore_button = (AppiumBy.ACCESSIBILITY_ID, "Explore")
        self.return_to_explore_button = (AppiumBy.ACCESSIBILITY_ID, "Wikipedia, return to Explore")
        self.profile_button = (AppiumBy.ACCESSIBILITY_ID, "profile-button")
        self.search_button = (AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")

        self.cancel_button = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Cancel"]')
        self.clear_button = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Clear"]')

    def tap_search_query_one(self, search_query):
        element = (AppiumBy.XPATH, "(//XCUIElementTypeStaticText[@name='" + search_query + "'])[1]")
        self.wait_for_page(element)
        self.driver.find_element(*element).click()
        return self

    def tap_cancel_button(self):
        self.driver.find_element(*self.cancel_button).click()
        return self

    def tap_clear_button(self):
        self.driver.find_element(*self.clear_button).click()
        return self

    def view_search_query_page(self, search_query):
        element = (AppiumBy.XPATH, "//XCUIElementTypeNavigationBar[@name='" + search_query + "']")
        self.wait_for_page(element)
        self.driver.find_element(*element).click()
        return self

