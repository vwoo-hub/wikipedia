from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class LogInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.cancel_button = (AppiumBy.ACCESSIBILITY_ID, "Cancel")
        self.log_in_label = (AppiumBy.ACCESSIBILITY_ID, "Log in to your account")
        self.join_wikipedia_button = (AppiumBy.ACCESSIBILITY_ID, "Don't have an account? Join Wikipedia.")
        self.username_text_field = (AppiumBy.CLASS_NAME, 'XCUIElementTypeTextField')
        self.password_text_field = (AppiumBy.CLASS_NAME, 'XCUIElementTypeSecureTextField')
        self.forgot_your_password_button = (AppiumBy.ACCESSIBILITY_ID, "Forgot your password?")
        self.log_in_button = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Log in"]')
        self.log_in_error_label = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Incorrect username or password entered. Please try again."]')

        self.initial_views = [
            self.cancel_button,
            self.log_in_label,
            self.join_wikipedia_button,
            self.username_text_field,
            self.password_text_field,
            self.forgot_your_password_button,
            self.log_in_button
        ]

    def tap_cancel_button(self):
        self.driver.find_element(*self.cancel_button).click()
        return self

    def tap_join_wikipedia_button(self):
        self.driver.find_element(*self.join_wikipedia_button).click()
        return self

    def type_username_text_field(self, username):
        self.driver.find_element(*self.username_text_field).send_keys(username)
        return self

    def type_password_text_field(self, password):
        self.driver.find_element(*self.password_text_field).send_keys(password)
        return self

    def tap_forgot_your_password_button(self):
        self.driver.find_element(*self.forgot_your_password_button).click()
        return self

    def tap_log_in_button(self):
        self.driver.find_element(*self.log_in_button).click()
        return self

    def view_log_in_error_label(self):
        self.wait_for_views([self.log_in_error_label])
        return self