from api.AppBasePage import AppBasePage
from selenium.webdriver.common.by import By
from time import sleep
class AppFirstPage(AppBasePage):
    def __init__(self):
        super().__init__()
    def locate_element(self,eleValue,style="ID"):
        if style=="ID":
            loca_ele = self.element_wait((By.ID,eleValue))
        elif style=="CLASS":
            loca_ele = self.element_wait((By.CLASS_NAME,eleValue))
        else:
            loca_ele = self.element_wait((By.XPATH,eleValue))
        return loca_ele
    def get_element_text(self,eleValue,style="ID"):
        element = self.locate_element(eleValue,style)
        ele_text = element.text
        return ele_text
    def click_element(self,eleValue,style="ID"):
        element = self.locate_element(eleValue,style)
        element.click()

if __name__ == "__main__":
    textView = "cn.ianzhang.android:id/textview_first"
    nextBtn = "cn.ianzhang.android:id/button_first"
    secondBtn = "cn.ianzhang.android:id/button_second"
    firstPage = AppFirstPage()

    firstPage_text = firstPage.get_element_text(textView)
    assert "Hello" in firstPage_text

    firstPage.click_element(nextBtn)

    secondPage_text = firstPage.get_element_text(secondBtn)
    assert "PREVIOUS" in secondPage_text

    firstPage.click_element(secondBtn)

    sleep(3)
    firstPage.quit()