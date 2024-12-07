from appium import webdriver
from config import AppCliendCaps,AppServerUrl

class AppDriverTool:
    __driver = None

    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            cls.__driver = webdriver.Remote(AppServerUrl,AppCliendCaps)
            cls.__driver.implicitly_wait(10)
        return cls.__driver
    @classmethod
    def quit_driver(cls):
        if cls.__driver is not None:
            cls.__driver.quit()
            cls.__driver = None