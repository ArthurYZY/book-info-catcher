import urllib.request


SRUInfo = "https://tsinghua.alma.exlibrisgroup.com/view/sru/86THU_INST?version=1.2&operation=searchRetrieve&recordSchema=marcxml&startRecord=11&maximumRecords=50&query=alma.title%20all%20%22$$%22"


requestList = []

with open("./bookList.txt", 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    for i in range(len(lines)):
        s = urllib.parse.quote(lines[i])
        requestList.append(SRUInfo.replace('$$', s))


for i in range(len(requestList)):
    url = "https://api.douban.com/v2/book/search?q=%s" % urllib.parse.quote(lines[i])
    print("getting %s" % lines[i])
    # url = requestList[i]
    request = urllib.request.Request(url)
    #爬取结果
    response = urllib.request.urlopen(request)
    data = response.read()
    #设置解码方式
    data = data.decode('utf-8')
    #打印结果
    with open("./info/" + lines[i] + ".txt", 'w') as f:
        f.write(data)