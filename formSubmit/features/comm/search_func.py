from config import Domain_Lists
def outPut_result(titles,urls):
    result_list = {}
    for engine in Domain_Lists:
        result_list[engine] = 0
    #输入搜索结果的标题和连接
    print("结果列表")
    for index in range(len(titles)):
        print(f'{titles[index].text} --> {urls[index].text} ')
        for engine in Domain_Lists:
            if engine in urls[index].text:
                result_list[engine] = result_list[engine]+1
    #出现顶级搜索域名出现的次数，顶级搜索域名可在config.py中设置
    print("结果统计")
    for engine,count in result_list.items():
        print(f'{engine} --> {count}')