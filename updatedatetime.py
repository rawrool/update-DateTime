from datetime import datetime, timezone
from urllib.error import URLError
from urllib.request import urlopen


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

    def get_site_headers(self):
        return self.siteResponse.info()

    def get_header_value(self, header_key):
        header_dict = dict(self.get_site_headers())
        date_value = header_dict.get(header_key)
        return date_value


def get_sites_date(website):
    date_string = website.get_header_value("Date")
    date_string_formatted = date_string.replace(",", "")
    return datetime.strptime(date_string_formatted, '%a %d %b %Y %X %Z')


def convert_gmt_to_local(site_gmt):
    return site_gmt.replace(tzinfo=timezone.utc).astimezone(tz=None)


site = WebSite('http://just-the-time.appspot.com/')
site_datetime = get_sites_date(site)
local_datetime = convert_gmt_to_local(site_datetime)
print(local_datetime)

