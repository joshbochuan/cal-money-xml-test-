import xml.etree.ElementTree as ET # 匯入XML函式庫 並命名為ET

def xml_to_dict(element):
    result = {}
    for child in element:
        if len(child) == 0:
            result[child.tag] = child.text
        else:
            result[child.tag] = xml_to_dict(child)
    return result

tree = ET.parse("setting.xml") # 讀取設定檔
root = tree.getroot() # 獲取裡面的資料
data = xml_to_dict(root)

money = int(data["money"])
interest = int(data["interest"])
months = int(data["months"])

total = 0
for i in range(months):
    total += money
    total *= 1+(interest)/100

result = open("result.txt","w",encoding="utf-8")
result.write("you have "+str(total)+" dollars left")
result.close()