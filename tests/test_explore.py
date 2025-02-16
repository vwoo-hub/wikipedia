import pytest

from pages.explore_page import ExplorePage
from pages.search_page import SearchPage
from tests.base_test import BaseTest


class TestHome(BaseTest):
    @pytest.fixture(autouse=True)
    def setup_pages(self):
        self.explore_page = ExplorePage(self.driver)
        self.search_page = SearchPage(self.driver)

    def test_when_input_search_query_then_show_search_results(self):
        with self.explore_page.wait_for_page() as page:
            page.type_search_field("Reddit")
            page.type_search_field("")

        with self.search_page.wait_for_page() as page:
            page.tap_search_query_one("Reddit")
            page.view_search_query_page("Reddit")


