import time

import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions


class AppiumDriver:
    driver = None

    @pytest.fixture()
    def start_driver(self, request):
        desired_caps = {
            'platformName': 'iOS',
            'platformVersion': '17.4',
            'deviceName': 'iPhone 15 Pro',
            'udid': "DBD4EFA6-5984-4B46-A13C-5AF94AB85334",
            'automationName': 'XCUITest',
            'bundleId': 'org.wikimedia.wikipedia'
        }

        capabilities_options = XCUITestOptions().load_capabilities(desired_caps)
        self.driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
        self.driver.implicitly_wait(7)

        request.cls.driver = self.driver

        yield self.driver

        self.stop_driver()
        print("Driver teardown called")

    def stop_driver(self):
        if self.driver:
            try:
                print("Quitting driver...")
                self.driver.quit()
            except Exception as e:
                print(f"Driver quit failed: {e}")
        else:
            print("Driver already None or terminated.")


