import json
import urllib2
import sys

allData = list()
def getData(url):
    response = urllib2.urlopen(url)
    data = json.load(response)
    global allData
    allData.extend(data['data'])
    print len(allData)
    if 'paging' in data:
        getData(data['paging']['next'])
    else:
        allData = json.dumps(allData, sort_keys=True, indent=4, ensure_ascii=False).encode('utf-8')
        file = open("data.json", 'w')
        file.write(allData)
        file.close

getData("https://graph.facebook.com/867704779984689/feed?fields=actions,from,message,comments.limit(0).summary(true),likes.limit(0).summary(true)&limit=1000&access_token=CAAWnAJjuBBkBAB6ZAsyDd26F84D5iAZAopuZBv9h4GzC8RGFlwCbJOUtVoQESpBKvSCSPZC6EZC78ZBAkeHZClIkvLWY3dTZB7WZBaeybQN2bVWt8hFrqamvjwizgx66K84Wry4bDoLpWy3MV3spFMgYOPrqMG0olGb7C6Pn4r064hTi1tFODQzLi")
