import pytest

from pages.account_page import AccountPage
from pages.explore_page import ExplorePage
from pages.settings_page import SettingsPage
from tests.base_test import BaseTest


class TestHome(BaseTest):
    @pytest.fixture(autouse=True)
    def setup_pages(self):
        self.explore_page = ExplorePage(self.driver)
        self.account_page = AccountPage(self.driver)
        self.settings_page = SettingsPage(self.driver)

    def test_when_in_settings_then_clear_cached_data_successfully(self):
        with self.explore_page.wait_for_page() as page:
            page.tap_profile_icon()

        with self.account_page.wait_for_page() as page:
            page.tap_settings_button()

        with self.settings_page.wait_for_page() as page:
            page.tap_clear_cached_data_button()
            page.tap_cached_data_cancel_button()
            page.tap_clear_cached_data_button()
            page.tap_cached_data_clear_cache_button()

