from api.AppDriverTool import AppDriverTool
from selenium.webdriver.support.wait import WebDriverWait
class AppBasePage:
    def __init__(self):
        self.appDriver = AppDriverTool.get_driver()

    def element_wait(self, data,multi=False):
        wdw = WebDriverWait(self.appDriver, 10, 0.5)
        if multi:
            element = wdw.until(lambda x:x.find_elements(*data))
        else:
            element = wdw.until(lambda x: x.find_element(*data))
        return element

    def quit(self):
        AppDriverTool.quit_driver()