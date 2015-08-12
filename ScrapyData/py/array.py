__author__ = 'land'

start_urls = [
        "http://tuliu.com/view-372131.html"
    ]
initUrl = "http://tuliu.com/view-3721"
for i in range(100):
    url = initUrl + str(i).zfill(2) + ".html"
    print(url)
    start_urls.append(url)