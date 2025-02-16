import pytest

from pages.account_page import AccountPage
from pages.explore_page import ExplorePage
from pages.log_in_page import LogInPage
from tests.base_test import BaseTest


class TestHome(BaseTest):
    @pytest.fixture(autouse=True)
    def setup_pages(self):
        self.explore_page = ExplorePage(self.driver)
        self.account_page = AccountPage(self.driver)
        self.log_in_page = LogInPage(self.driver)

    def test_when_invalid_credentials_then_display_error_message(self):
        with self.explore_page.wait_for_page() as page:
            page.tap_profile_icon()

        with self.account_page.wait_for_page() as page:
            page.tap_log_in_button()

        with self.log_in_page.wait_for_page() as page:
            page.type_username_text_field("test_username")
            page.type_password_text_field("test_password")
            page.tap_log_in_button()
            page.view_log_in_error_label()


