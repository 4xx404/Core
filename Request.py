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

    # Checks for status code 200
    def IsLive(self, Link: str):
        self.Link: str = Link
        try:
            self.Request = requests.get(self.Link, headers=self.Config.Headers)
        except Exception:
            return False

        return True

    # Return the page content as bytes by default, set ReturnAsString = True to return as string type
    def GetContent(self, Link: str, ReturnAsString: bool = False):
        self.Link: str = Link

        self.Response = {
            "status": False,
            "data": ""
        }

        if(self.Validator.NotEmpty(self.Link)):
            if(self.IsLive(self.Link)):
                self.Request = requests.get(self.Link, headers=self.Config.Headers)
                
                if(ReturnAsString):
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

    # Return a usable link or if not usable set to None
    def FormatLink(self, Link):
        self.Link = Link

        if(self.Validator.HasProtocol(self.Link)):
            self.ValidLink = self.Link
        elif(self.Link.startswith("/") and len(self.Link) > 1):
            if(self.BaseLink.endswith("/")):
                self.ValidLink = f"{self.BaseLink[:-1]}{self.Link}"
            else:
                self.ValidLink = f"{self.BaseLink}{self.Link}"
        else:
            self.ValidLink = None

        return self.ValidLink

    # Collect any "a" html tag's href and format into usable url's
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
                self.ValidLink = self.FormatLink(self.BaseLink, str(self.LinkTag["href"]))
                if(not self.ValidLink in self.Response["data"] and self.ValidLink != None):
                    self.Response["status"] = True
                    self.Response["data"].append(self.ValidLink)
                else:
                    continue
            
            return self.Response

        else:
            self.Response["data"].append(self.Error.Throw("request_collect_all_links_no_response", self.BaseLink))
            return self.Response
