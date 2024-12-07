from api.SearchPage import SearchPage
from config import SearchURL
from comm.func import read_json_data
import pytest
class TestSearchKeyWord:
    def setup_class(self):
        self.searchPage = SearchPage()
    def teardown_class(self):
        self.searchPage.quit()
    def setup(self):
        self.searchPage.get(SearchURL)
    def teardown(self):
        pass
    @pytest.mark.parametrize("caseName,requ",read_json_data("SearchWord.json"))
    def test_search_keyWord(self,caseName,requ):
        print(caseName)
        self.searchPage.search(requ["keyWord"])