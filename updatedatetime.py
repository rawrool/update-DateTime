from datetime import datetime, timezone
from urllib.error import URLError
from urllib.request import urlopen

site = urlopen('http://just-the-time.appspot.com/')
siteHeaders = site.info()
headerDict = dict(siteHeaders)
dateString = headerDict.get("Date")
dateStringFormatted = dateString.replace(",", "")
dateTimeGMT = datetime.strptime(dateStringFormatted, '%a %d %b %Y %X %Z')
dateTimeLocal = dateTimeGMT.replace(tzinfo=timezone.utc).astimezone(tz=None)
print(dateTimeLocal)


class WebSite:
    def __init__(self, url):
        self.siteUrl = url
        self.siteResponse = self.get_site_response()

    def get_site_response(self):
        try:
            self.siteResponse = urlopen(self.siteUrl)
        except URLError as e:
            if hasattr(e, 'reason'):
                print('We failed to reach the site.')
                print('Reason: ', e.reason)
            elif hasattr(e, 'code'):
                print('The server couldn\'t fulfill the request.')
                print('Error code: ', e.code)
        else:
            return self.siteResponse
