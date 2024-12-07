from api.DriverTool import DriverTool
from selenium.webdriver.support.wait import WebDriverWait
class BasePage:
    def __init__(self):
        self.driver = DriverTool.get_driver()
    def element_wait(self,data):
        wdw = WebDriverWait(self.driver,30,0.5)
        element = wdw.until(lambda x:x.find_element(*data))
        return element
    def get(self,url):
        self.driver.get(url)
    def quit(self):
        DriverTool.quit_driver()