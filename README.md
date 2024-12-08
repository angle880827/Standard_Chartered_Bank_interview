# Standard_Chartered_Bank_interview
渣打银行笔试项目

## 一、搜索关键字并输出搜索结果标题和链接和APP测试

1、python所需三方包：selenium,pytest，appuim,pytest-html

2、项目所在文件夹为SearchCount,该项目中包含了第一题和第三题APP测试的代码

3、设置文件config.py

​			SearchEngine可设置使谷歌还是Edge进行测试

​					如果使用谷歌测试，则需要把chromedriver.exe（根据自已的浏览器版本下载 ）并放在python的安装目录下

​					如果使用Edge测试，需要将EdgePath设置为msedgedriver.exe（根据自已的浏览器版本下载 ）所在路径

​			SearchURL可设置关键字搜索的网址

​			Domain_Lists可设置想要统计的顶流域名

 4、APP测试时，需要下载模拟器和Appuim软件，并在config.py中设置模拟器的安卓版本和Appuim的所在路径

5、在searchCount目录下执行pytest命令即可运行本项目

6、如果想单独运行关键字搜索，则将当前项目运行环境设置为venv，然后在scripts目录中右击test_01_search_keyWord.py进行运行

7、如果想单独运行关键字搜索，则将当前项目运行环境设置为venv,然后在scripts目录中右击test_02_appium.py并运行



## 二、基于cucumber进行表单填写并生成测试报告

1、python 所需三方包：selenium,behave,behave-html

2、项目所在文件夹为formSubmit,在该目录下执行behave即可运行该项目