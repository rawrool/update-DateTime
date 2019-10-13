import datetime
from urllib.request import urlopen
res = urlopen('http://just-the-time.appspot.com/')
result = res.read().strip()
siteHeaders = res.info()
headerDict = dict(res.info())
print(headerDict.get("Date"))
# print(result.decode('utf-8'))
# print(datetime.datetime.now())
# print(datetime.datetime.utcfromtimestamp())
