import requests
from requests.exceptions import ConnectionError
import re
from urllib.parse import urlparse


class CtxRequest(object):
    def __init__(self, url):
        self.url = url
        self.linkList = []
        self.emailList = []
        self.url_status_code = None
        self.url_validity = True

    def checkIfurlValid(self, url):
        badUrlExtesions = ['pdf', 'png', 'gif', 'csv', 'txt', 'jpg', 'swf']
        regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if re.match(regex, url):
            if url[-3:] not in badUrlExtesions:
                return True
        return False

    def __getPageContent(self, url=None):
        urlGo = self.url if url is None else url
        if not self.checkIfurlValid(urlGo):
            self.url_validity = False
            return None
            
        try:
            req = requests.get(urlGo, timeout=(2, 5))
            self.url_status_code = req.status_code
        except:
            self.url_status_code = "Error"
            return None

        if url is None:
            print("Parsing links: ", self.url, "Status: ", req.status_code)
        else:
            print("Parsing info. on: ", url, "Status: ", req.status_code)
        return req.content


    def getLinks(self):
        content = self.__getPageContent()
        if content is not None:
            linkSet = set()
            print("CONTENT IS NOT NONE")
            urls = re.findall(r'href=[\'"]?([^\'" >]+)', content.decode())
            urlList =  [item for item in urls if urlparse(self.url).netloc == urlparse(item).netloc and self.checkIfurlValid(item) == True]
            linkSet.update(urlList)
            self.linkList = [*list(linkSet)]

            print(urlList)
            return urlList
        return None


    def getEmails(self):
        self.getLinks()
        emailSet = set()
        
        for link in self.linkList:
            content = self.__getPageContent(link)
            # emllst = re.findall(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', content.decode())
            emllst = re.findall(r'[\w\.-]+@[\w\.-]+', content.decode())

            if len(emllst) >=1:
                self.emailList = [*self.emailList, *[item for item in emllst]]
        emailSet.update(self.emailList)
        self.emailList = [*list(emailSet)]
        return {"emails": self.emailList, "status": self.url_status_code, "urlValidity": self.url_validity}