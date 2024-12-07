from api.AppDriverTool import AppDriverTool
from comm.func import read_json_data
import pytest
from api.AppFirstPage import AppFirstPage

class TestApp:
    def setup_class(self):
        self.appDriver = AppFirstPage()
    def teardown_class(self):
        self.appDriver.quit()

    @pytest.mark.parametrize("caseName,locate_element,operate_element,expect", read_json_data("app_page.json",style="app"))
    def test_app_page(self,caseName,locate_element,operate_element,expect):
        print(caseName)
        ele_text = self.appDriver.get_element_text(locate_element["ele_locate_value"],style=locate_element["ele_locate_style"])
        flag = False
        if expect in ele_text: flag=True
        self.appDriver.click_element(operate_element["ele_locate_value"],style=operate_element["ele_locate_style"])
        assert flag