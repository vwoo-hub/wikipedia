from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class SettingsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.settings_label = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Settings"]')
        self.done_button = (AppiumBy.ACCESSIBILITY_ID, "Done")
        self.clear_cached_data_button = (AppiumBy.ACCESSIBILITY_ID, "Clear cached data")
        self.cached_data_cancel_button = (AppiumBy.ACCESSIBILITY_ID, "Cancel")
        self.cached_data_clear_cache_button = (AppiumBy.ACCESSIBILITY_ID, "Clear cache")

        self.initial_views = [
            self.settings_label,
            self.done_button,
            self.clear_cached_data_button
        ]

    def tap_done_button(self):
        self.driver.find_element(*self.done_button).click()
        return self

    def tap_clear_cached_data_button(self):
        self.driver.find_element(*self.clear_cached_data_button).click()
        return self

    def tap_cached_data_cancel_button(self):
        self.driver.find_element(*self.cached_data_cancel_button).click()
        return self

    def tap_cached_data_clear_cache_button(self):
        self.driver.find_element(*self.cached_data_clear_cache_button).click()
        return self