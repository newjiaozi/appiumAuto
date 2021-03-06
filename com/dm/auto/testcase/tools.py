#coding=utf-8


from openpyxl import load_workbook


def getTestData(file,sheet,exec=10):
    wb = load_workbook(file)
    sheet = wb[sheet]
    data_tuple = tuple(sheet.rows)[1:]
    parsedData = parseData(data_tuple,exec)
    return parsedData

##将excel读取出的数据cell获取真正的数据返回格式为[[],[],[]]
def parseData(data_tuple,exec):
    a_list = []
    for i in data_tuple:
        b_list = []
        for j in i:
            b_list.append(j.value)
        if b_list[exec] and b_list[exec].strip().lower() == "yes":
            del b_list[exec]
            a_list.append(b_list)
    return a_list
