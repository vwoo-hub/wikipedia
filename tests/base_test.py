import allure
import pytest
from allure_commons.types import AttachmentType

from driver.appium_driver import AppiumDriver


class BaseTest(AppiumDriver):
    @pytest.fixture(autouse=True)
    def setup_driver(self, start_driver, request):
        self.driver = start_driver

        yield self.driver


    @pytest.fixture(autouse=True)
    def screenshot_failure(self, request):
        yield
        item = request.node
        if hasattr(item, "rep_call") and item.rep_call.failed:
            try:
                print(f"Driver state before screenshot: {self.driver}")
                if self.driver:
                    allure.attach(
                        self.driver.get_screenshot_as_png(),
                        name="screenshot_on_failure",
                        attachment_type=AttachmentType.PNG,
                    )
                else:
                    print("Driver is None; cannot capture screenshot.")
            except Exception as e:
                print(f"Screenshot failure error: {type(e).__name__}: {e}")
                raise