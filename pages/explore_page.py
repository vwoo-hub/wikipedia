from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class ExplorePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.profile_icon = (AppiumBy.ACCESSIBILITY_ID, "profile-button")
        self.search_field = (AppiumBy.CLASS_NAME, "XCUIElementTypeSearchField")
        self.today_label = (AppiumBy.ACCESSIBILITY_ID, "Today")
        self.featured_article_label = (AppiumBy.ACCESSIBILITY_ID, "Featured article")
        self.article_overflow_button = (AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="overflow"])[1]')
        self.save_for_later_button = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Save for later"]')

        self.initial_views = [
            self.profile_icon,
            self.search_field,
            self.today_label
        ]

    def tap_profile_icon(self):
        self.driver.find_element(*self.profile_icon).click()
        return self

    def tap_search_field(self):
        self.driver.find_element(*self.search_field).click()

    def type_search_field(self, search_query):
        self.driver.find_element(*self.search_field).send_keys(search_query)
        return self

    def tap_featured_article_label(self):
        self.driver.find_element(*self.featured_article_label).click()
        return self

    def tap_article_overflow_button(self):
        self.driver.find_element(*self.article_overflow_button).click()
        return self

    def tap_save_for_later_button(self):
        self.driver.find_element(*self.save_for_later_button).click()
        return self

