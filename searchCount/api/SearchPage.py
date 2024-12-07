from api.BasePage import BasePage
from selenium.webdriver.common.by import By
from comm.search_func import outPut_result
from config import SearchURL
from time import sleep
class SearchPage(BasePage):
    def __init__(self):
        super().__init__()
        self.input_search = (By.ID,"sb_form_q")
        self.btn_search = (By.ID,"search_icon")
        self.btn_page_num = (By.XPATH,"//a[@aria-label='第 2 页']")
        self.content_title = (By.CLASS_NAME,"tptt")
        self.content_url = (By.CLASS_NAME, "tpmeta")
    def search(self,keyWord):
        #定位搜索输入框
        search_input = self.element_wait(self.input_search)
        search_input.send_keys(keyWord)
        #定位搜索按钮
        search_btn = self.element_wait(self.btn_search)
        search_btn.click()
        sleep(10)
        #定位翻页按钮，查询结果基于第二页
        page_num_btn = self.element_wait(self.btn_page_num)
        page_num_btn.click()
        sleep(10)
        # 定位每个查询到的标题和链接
        titles = self.driver.find_elements(*self.content_title)
        urls =self.driver.find_elements(*self.content_url)
        #输出结果列表和结果统计
        outPut_result(titles,urls)
if __name__=="__main__":
    searPage = SearchPage()
    searPage.get(SearchURL)
    searPage.search("Selenium")
    searPage.quit()