import requests
import re
from urllib.parse import urlparse

class CtxRequest(object):
    def __init__(self, url):
        self.url = url
        self.linkList = []
        self.emailList = []
        self.url_status_code = None

    def __getPageContent(self, url=None):

        urlGo = self.url if url is None else url
        urlGO = urlparse(urlGo).netloc
        print("URLPARSER: ", urlGo)
        req = requests.get(urlGo)
        self.url_status_code = req.status_code


        if url is None:
            print("Parsing links: ", self.url, "Status: ", req.status_code)
        else:
            print("Parsing info. on: ", url, "Status: ", req.status_code)
        return req.content


    def getLinks(self):
        content = self.__getPageContent()
        urls = re.findall(r'href=[\'"]?([^\'" >]+)', content.decode())
        urlList =  [item for item in urls if urlparse(self.url).netloc == urlparse(item).netloc]
        self.linkList = [*urlList]
        return urlList


    def getEmails(self):
        self.getLinks()
        emailSet = set()
        for link in self.linkList:
            content = self.__getPageContent(link)
            emllst = re.findall(r'[\w\.-]+@[\w\.-]+', content.decode())

            if len(emllst) >=1:
                self.emailList = [*self.emailList, *[item for item in emllst]]
        emailSet.update(self.emailList)
        self.emailList = [*list(emailSet)]
        return {"emails": self.emailList, "status": self.url_status_code}