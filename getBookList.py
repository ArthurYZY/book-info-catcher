import xlrd

data = xlrd.open_workbook('bookList.xlsx') # 打开xls文件
table = data.sheets()[0] # 打开第一张表
nrows = table.nrows # 获取表的行数


bookList = []
for i in range(nrows): # 循环逐行打印
    bookList.append(table.row_values(i)[0] + '\n') # 取前十三列

with open("bookList.txt", 'w') as f:
    f.writelines(bookList)
