import os
BaseDir = os.path.abspath(os.path.dirname(__file__))
DataDir = os.path.join(BaseDir,"data","")
SearchEngine = "Chrome" #可填Chrome或者Edge
EdgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedgedriver.exe"
#搜索引擎地址
SearchURL = "https://cn.bing.com/"
#顶流域名，如果想统计，则添加到数组中即可
Domain_Lists =["bing.com","baidu.com"]

AppCliendCaps = {
"platformName":"android",
    "platformVersion":"9",
    "deviceName":"MI 9",
    "appPackage":"cn.ianzhang.android",#包名
    "appActivity":".MainActivity",#界面名
}
AppServerUrl = "http://127.0.0.1:4723/wd/hub"