import json

from config import DataDir
def read_json_data(fileName):
    fileDir = DataDir+fileName
    with open(fileDir,"r",encoding="utf-8") as f:
        data = json.load(f)
        paras = []
        for item in data:
            paras.append((item["caseName"],item["requ"]))
    return paras
if __name__=="__main__":
    print(read_json_data("SearchWord.json"))