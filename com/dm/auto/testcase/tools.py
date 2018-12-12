#coding=utf-8


from openpyxl import load_workbook


def getTestData(file,sheet):
    wb = load_workbook(file)
    sheet = wb[sheet]
    data_tuple = tuple(sheet.rows)[1:]
    parsedData = parseData(data_tuple)
    return parsedData

##将excel读取出的数据cell获取真正的数据返回格式为[[],[],[]]
def parseData(data_tuple):
    a_list = []
    for i in data_tuple:
        b_list = []
        for j in i:
            b_list.append(j.value)
        if b_list[10] and b_list[10].strip().lower() == "yes":
            a_list.append(b_list)
    return a_list
