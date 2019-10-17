import calendar
import os
from datetime import datetime, timezone, timedelta
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
    unix_timestamp = calendar.timegm(site_gmt.timetuple())
    local_datetime = datetime.fromtimestamp(unix_timestamp)
    assert site_gmt.resolution >= timedelta(microseconds=1)
    return local_datetime.replace(microsecond=site_gmt.microsecond)


def change_system_time(converted_date):
    date_format = str(converted_date.strftime("%m")) + "-" + str(converted_date.strftime("%d")) + "-" + \
                  str(converted_date.strftime("%y"))
    time_format = str(converted_datetime.strftime("%X"))
    os.system("date " + date_format)
    os.system("time " + time_format)


site = WebSite('https://google.com/')
site_datetime = get_sites_date(site)
converted_datetime = convert_gmt_to_local(site_datetime)
change_system_time(converted_datetime)

