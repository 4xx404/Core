import sys
sys.dont_write_bytecode = True

import requests
from bs4 import BeautifulSoup

from .Config import CoreConfig
from .Validity import Validation
from .Error import ErrorHandler

class RequestHandler:
    def __init__(self):
        self.Config = CoreConfig()
        self.Validator = Validation()
        self.Error = ErrorHandler()

    def IsLive(self, Link: str):
        self.Link: str = Link
        
        try:
            self.Request = requests.get(self.Link, headers=self.Config.Headers)
        except Exception:
            return False

        return True

    def GetContent(self, Link: str, ReturnAsString: bool = False):
        self.Link: str = Link

        self.ReturnAsString = ReturnAsString

        self.Response = {
            "status": False,
            "data": ""
        }

        if(self.Validator.NotEmpty(self.Link)):
            if(self.IsLive(self.Link)):
                self.Request = requests.get(self.Link, headers=self.Config.Headers)
                
                if(self.ReturnAsString):
                    self.Response["status"] = True
                    self.Response["data"] = self.Request.content.decode()
                else:
                    self.Response["status"] = True
                    self.Response["data"] = self.Request.content
            else:
                self.Response["data"] = self.Error.Throw("request_get_content_no_response", self.Link)
        else:
            self.Response["data"] = self.Error.Throw("request_get_content_empty_link_value", None)

        return self.Response

    def CollectAllLinks(self, BaseLink: str):
        self.BaseLink: str = BaseLink

        self.Response = {
            "status": False,
            "data": []
        }


        if(self.IsLive(self.BaseLink)):
            self.Request = requests.get(self.BaseLink, headers=self.Config.Headers)
            self.Soup = BeautifulSoup(self.Request.content, 'html.parser')

            for self.LinkTag in self.Soup.find_all("a", href=True):
                self.Link = str(self.LinkTag["href"])

                if(self.Link.startswith("http://") or self.Link.startswith("https://")):
                    self.ValidLink = self.Link
                elif(self.Link.startswith("/") and len(self.Link) > 1):
                    if(self.BaseLink.endswith("/")):
                        self.ValidLink = f"{self.BaseLink[:-1]}{self.Link}"
                    else:
                        self.ValidLink = f"{self.BaseLink}{self.Link}"
                else:
                    self.ValidLink = None

                if(not self.ValidLink in self.Response["data"] and self.ValidLink != None):
                    self.Response["status"] = True
                    self.Response["data"].append(self.ValidLink)
                else:
                    continue
            
            return self.Response

        else:
            self.Response["data"].append(self.Error.Throw("request_collect_all_links_no_response", self.BaseLink))
            return self.Response
