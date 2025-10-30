def getPage(url):
    try:
        import urllib.request
        page = urllib.request.urlopen(url).read()
        return page.decode("utf-8")
    except:
        return ""


def extractLinks(index):
    links = []
    secondQuoteLocation = 0
    while True:
        firstHrefLocation = index.find("a href=", secondQuoteLocation)
        if firstHrefLocation == -1:
            break
        firsQuoteLocation = (index.find('"', firstHrefLocation)) + 1
        secondQuoteLocation = index.find('"', firsQuoteLocation )
        link = index[firsQuoteLocation:secondQuoteLocation]

        links.append(link)

    return(links)


def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)

def addContentToIndex(index, page, content):
    words = content.split()
    for word in words:
        found = False
        for line in index:
            if word == line[0]:
                line[1].append(page)
                found = True
                break
        if not found:
            index.append([word, [page]])

def formatter(index):
    formatted = ""
    for line in index:
        formatted = formatted + str(line) + "\n"
    return formatted

def finder(keyword ,index):
    for line in index:
        if keyword == line[0]:
            return line[1]
    return[]



def crawlWeb(seed):
    toCrawl = [seed]
    crawled = []
    index = []
    while toCrawl:
        page = toCrawl.pop()
        if page not in crawled:
            content = getPage(page)
            addContentToIndex(index, page, content)
            union(toCrawl, extractLinks(content))
            crawled.append(page)
    return index


myIndex= crawlWeb("https://searchengineplaces.com.tr")

print(finder("wait", myIndex))
