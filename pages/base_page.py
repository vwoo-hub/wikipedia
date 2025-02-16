
from contextlib import contextmanager

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    initial_views = []

    def __init__(self, driver):
        self.driver = driver

    @contextmanager
    def wait_for_page(self, timeout=5):
        self.wait_for_views(self.initial_views, timeout)
        yield self

    def wait_for_views(self, matchers, timeout=5, condition="visible"):
        elements = []
        for matcher in matchers:
            try:
                wait = WebDriverWait(self.driver, timeout)
                if condition == "visible":
                    element = wait.until(EC.visibility_of_element_located(matcher))
                elif condition == "clickable":
                    element = wait.until(EC.element_to_be_clickable(matcher))
                elif condition == "presence":
                    element = wait.until(EC.presence_of_element_located(matcher))
                else:
                    raise ValueError(f"Unsupported condition: {condition}")
                elements.append(element)
            except TimeoutException:
                raise TimeoutException(
                    f"Element {matcher} did not match the condition '{condition}' within {timeout} seconds.")
        return elements

    def hide_keyboard(self):
        try:
            self.driver.hide_keyboard()
        except Exception as e:
            print(f"Keyboard not open or could not be hidden: {e}")

