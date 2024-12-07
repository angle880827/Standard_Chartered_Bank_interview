import json

from config import DataDir
def read_json_data(fileName,style="web"):
    fileDir = DataDir+fileName
    with open(fileDir,"r",encoding="utf-8") as f:
        data = json.load(f)
        paras = []
        for item in data:
            if style=="web":
                paras.append((item["caseName"],item["requ"]))
            else:
                paras.append((item["caseName"],item["locate_element"],item["operate_element"],item["expect"]))
    return paras
if __name__=="__main__":
    print(read_json_data("SearchWord.json"))