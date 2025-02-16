from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.log_in_button = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Log in / Join Wikipedia"]')
        self.donate_button = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Donate"]')
        self.profile_button = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Year in Review"]')
        self.settings_button = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Settings"]')

        self.initial_views = [
            self.log_in_button,
            self.donate_button,
            self.profile_button,
            self.settings_button
        ]

    def tap_log_in_button(self):
        self.driver.find_element(*self.log_in_button).click()
        return self

    def tap_donate_button(self):
        self.driver.find_element(*self.donate_button).click()
        return self

    def tap_profile_button(self):
        self.driver.find_element(*self.profile_button).click()
        return self

    def tap_settings_button(self):
        self.driver.find_element(*self.settings_button).click()
        return self

