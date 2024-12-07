import os
BaseDir = os.path.abspath(os.path.dirname(__file__))
DataDir = os.path.join(BaseDir,"data","")
ImageDir = os.path.join(BaseDir,"image","")
SearchEngine = "Edge" #可填Chrome或者Edge
EdgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedgedriver.exe"#填写edgeDriver所在路径
#搜索引擎地址
SearchURL = "https://cn.bing.com/"
#顶流域名，如果想统计，则添加到数组中即可
Domain_Lists =["bing.com","baidu.com"]
