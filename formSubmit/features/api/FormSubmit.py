from api.BasePage import BasePage
from selenium.webdriver.common.by import By
from config import ImageDir
from time import sleep
import datetime
class FormSubmit(BasePage):
    def __init__(self):
        super().__init__()
        #第一页的“下一页”按钮
        self.nextPageBtn =(By.XPATH,"//span[text()='下一页']/..") #(By.TAG_NAME, "button")
        #第二页的断言标题
        self.secondSuccess = (By.XPATH,"//div[contains(text(),'申请日期')]")
        #申请日期输入框
        self.appDateInput = (By.XPATH,"//input[@placeholder='年-月-日' and @class='ant-input']")
        #申请人输入框
        self.appPersonInput = (By.ID,"TextInputfield_19")
        #联系方式输入框
        self.contactInfo = (By.NAME,"field_20")
        #第二页的“下一页”按钮
        self.SecNextPageBtn = (By.XPATH,"//span[text()='下一页']/..")
        #第三页的断言标题
        self.thirdSuccess = (By.XPATH,"//span[text()='连续生产/开工类单位报备表']")
        #报备单位输入框
        self.repComInput = (By.ID,"TextInputfield_23")
        #在岗人数输入框和湖北籍输入框
        self.perNumInput = (By.XPATH,"//input[@role='spinbutton']")
        #单位负责人
        self.comLeaInput = (By.NAME,"field_27")
        #第三页联系方式
        self.conInfoInput = (By.NAME,"field_28")
        #疫情防控方案
        self.platTextarea = (By.NAME,"field_29")
        #第三张表单的提交按钮
        self.submitBtn = (By.XPATH,"//span[text()='提交']/..")
        #提交成功
        self.subSuccDiv = (By.CLASS_NAME,"ant-modal-confirm-content")
    #页面滚动
    def scroll(self,x,y):
        js = f"window.scrollTo({x},{y})"
        self.driver.execute_script(js)
    #屏幕截图
    def screenShot(self,fileName):
        fName = ImageDir+fileName
        self.driver.get_screenshot_as_file(fName)
    #表单第一页元素选择
    def firstForm(self,choice):
        #切换到iframe里定位元素
        self.driver.switch_to.frame(0)
        companyType = (By.XPATH, f"//span[contains(text(),'{choice}')]")
        type = self.element_wait(companyType)
        type.click()
        nextPageBtn = self.element_wait(self.nextPageBtn)
        nextPageBtn.click()
        self.screenShot("form_1.png")

    #第二页数据元素自动填写
    def secondForm(self,formDetails):
        #申请日期
        appDateInput = self.element_wait(self.appDateInput)
        year = datetime.date.today().year
        currDate = f'{year}-01-01'
        appDateInput.send_keys(formDetails[0])
        #申请人
        appPersonInput = self.element_wait(self.appPersonInput)
        appPersonInput.send_keys(formDetails[1])
        #联系方式
        contactInfoInput = self.element_wait(self.contactInfo)
        contactInfoInput.send_keys(formDetails[2])
        nextPageBtn = self.element_wait(self.SecNextPageBtn)
        nextPageBtn.click()
        self.screenShot("form_2.png")

    #第三页数据元素自动填写
    def thirdForm(self,formDetails):
        #报备单位
        repComInput = self.element_wait(self.repComInput)
        repComInput.send_keys(formDetails[0])
        #定位两个元素，在岗人数和接触湖北籍人数输入框
        perNumInputs = self.element_wait(self.perNumInput,multi=True)
        #在岗人数
        perNumInputs[0].send_keys(formDetails[1])
        #接触湖北籍人数
        perNumInputs[1].send_keys(formDetails[3])
        #报备日期
        appDateInput = self.element_wait(self.appDateInput)
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        appDateInput.send_keys(current_date)
        #单位负责人
        comLeaInput = self.element_wait(self.comLeaInput)
        comLeaInput.send_keys(formDetails[4])
        #联系方式
        conInfoInput = self.element_wait(self.conInfoInput)
        conInfoInput.send_keys(formDetails[5])
        #疫情防控方案
        platTextArea = self.element_wait(self.platTextarea)
        platTextArea.send_keys(formDetails[6])
        self.screenShot("form_3.png")
        #点击提交按钮
        submitBtn = self.element_wait(self.submitBtn)
        submitBtn.click()
        sleep(1)
        self.screenShot("form_SubmitSuccess.png")

    # 表单是否跳转成功的断言
    def isJumpToSuccess(self, num):
        flag = True
        try:
            if num == 2:
                secondSuccessDiv = self.element_wait(self.secondSuccess)
                secondSuccessDiv.click()
            elif num == 3:
                thirdSuccessSpan = self.element_wait(self.thirdSuccess)
                thirdSuccessSpan.click()
            elif num == 4:
                self.driver.switch_to.default_content()
                subSuccDiv = self.element_wait(self.subSuccDiv)
                if "提交成功" not in subSuccDiv.text:
                    print(f"期望：提交成功，实际：{subSuccDiv.text}")
                    raise "表单提交失败"
            else:
                raise "函数参数传递错误"
        except:
            flag = False
        return flag

if __name__ == "__main__":
    formPage = FormSubmit()
    formPage.get("https://jinshuju.net/templates/detail/Dv9JPD")
    formPage.firstForm("连续生产/开工类企事业单位")
    print(formPage.isJumpToSuccess(2))
    formPage.secondForm(["2024-01-01","自动化","13888888888"])
    print(formPage.isJumpToSuccess(3))
    formPage.thirdForm(["测试公司", "99", "2014-12-04","0","王娇","13888888888","测试内容"])
    print(formPage.isJumpToSuccess(4))
    formPage.quit()
