from behave import step
from api.FormSubmit import FormSubmit
from time import sleep
formPage = FormSubmit()
@step('进入表单URL"{url}"')
def step_impl(context,url):
    global formPage
    formPage.get(url)
@step('选择"{companyType}"')
def step_impl(context,companyType):
    global formPage
    formPage.firstForm("连续生产/开工类企事业单位")
    pass
@step('跳转到第二页')
def step_impl(context):
    global formPage
    assert formPage.isJumpToSuccess(2)
    sleep(5)
@step('第二页表单内容')
def step_impl(context):
    global formPage
    dataList = []
    if context.table is not None:
        for row in context.table:
            dataList.append(row[1])
    formPage.secondForm(dataList)
@step('跳转到第三页')
def step_impl(context):
    global formPage
    assert formPage.isJumpToSuccess(3)
@step('第三页表单内容')
def step_impl(context):
    global formPage
    dataList = []
    if context.table is not None:
        for row in context.table:
            dataList.append(row[1])
    formPage.thirdForm(dataList)
@step('弹出提交成功提示框')
def step_impl(context):
    global formPage
    formPage.isJumpToSuccess(4)
    formPage.quit()