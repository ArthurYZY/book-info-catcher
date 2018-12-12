import json
import os

path = "./info/"
files = os.listdir("./info/")


# print(files)
def getAuthor(book):
    author = ''
    for i in range(len(book["author"])):
        author += book["author"][i] + " "
    return author

booksList = []
for file in files:
    with open(path + file, 'r') as f:
        line = f.read()
        bookInfo = json.loads(line)["books"][0]
    booksList.append(bookInfo)
    # print(file, bookInfo["title"])
    # break

mdInfo = []
for i in range(len(booksList)):
    book = booksList[i]
    expectedName = files[i][:-4]
    info = ""
    info += "## " + expectedName + '  \n'
    info += "爬虫得到的书名: " + book["title"] + '  \n'
    info += "作者: " + getAuthor(book) + '  \n'
    info += "出版社: " + book["publisher"] + '  \n'
    info += "ISBN10: " + book["isbn10"] + '  \n'
    info += "[搜索网址]" + "(https://tsinghua-primo.hosted.exlibrisgroup.com/primo-explore/search?query=any,contains,%s&tab=default_tab&search_scope=print_scope&vid=86THU&lang=zh_CN&offset=0)" % expectedName + '  \n'
    mdInfo.append(info)

with open("info.md", 'w') as f:
    f.writelines(mdInfo)