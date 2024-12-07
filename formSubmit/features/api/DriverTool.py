from selenium import webdriver
from config import SearchEngine,EdgePath
from selenium.webdriver.edge.options import Options
class DriverTool:
    __driver = None
    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            if SearchEngine=="Edge":
                cls.__driver = webdriver.Edge(EdgePath)
            else:
                cls.__driver = webdriver.Chrome()
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(10)
        return cls.__driver
    @classmethod
    def quit_driver(cls):
        if cls.__driver is not None:
            cls.__driver.quit()
            cls.__driver=None