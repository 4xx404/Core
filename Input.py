import sys
sys.dont_write_bytecode = True

from .Styling.Colors import bc

from .Commands import Command
from .Validity import Validation
from .Error import ErrorHandler

class InputManager:
    def __init__(self):
        self.Cmd = Command()
        self.Validator = Validation()
        self.Error = ErrorHandler()

    def SetLink(self, Placeholder: str = None):
        self.Placeholder: str = Placeholder

        self.Response: dict = {
            "status": False,
            "data": ""
        }

        if(self.Placeholder != None):
            while(self.Placeholder.startswith(" ") or self.Placeholder.endswith(" ")):
                if(Placeholder.startswith(" ")):
                    self.Placeholder = self.Placeholder[0:]
                elif(Placeholder.endswith(" ")):
                    self.Placeholder = self.Placeholder[:-1]

            if(self.Placeholder.endswith(":")):
                self.TruePlaceholder = f"{self.Placeholder}{bc.GC} "
            else:
                self.TruePlaceholder = f"{self.Placeholder}:{bc.GC} "
        else:
            self.TruePlaceholder = f"Link:{bc.GC} "

        self.Link: str = str(input(f"{bc.BC} {self.TruePlaceholder}"))
        
        self.ValidityResponse: dict = self.Validator.IsLinkFormat(self.Link)
        if(self.ValidityResponse["status"]):
            self.Response["status"] = True
            self.Response["data"] = self.ValidityResponse["data"]
        else:
            self.Response["data"] = self.ValidityResponse["data"]
        
        return self.Response

    def SetPhoneNumber(self):
        self.PhoneNumber: str = str(input(f"{bc.BC} Phone Number:{bc.GC} "))

        self.Response: dict = {
            "status": False,
            "data": ""
        }

        self.ValidityResponse: dict = self.Validator.IsPhoneNumberFormat(self.PhoneNumber)
        if(self.ValidityResponse["status"]):
            self.Response["status"] = True
            self.Response["data"] = self.ValidityResponse["data"]
        else:
            self.Response["data"] = self.ValidityResponse["data"]

        return self.Response

    def SetEmailAddress(self):
        self.Email: str = str(input(f"{bc.BC} Email Address:{bc.GC} "))
        
        self.Response: dict = {
            "status": False,
            "data": ""
        }

        self.ValidityResponse: dict = self.Validator.IsEmailFormat(self.Email)
        if(self.ValidityResponse["status"]):
            self.Response["status"] = True
            self.Response["data"] = self.ValidityResponse["data"] # Return Valid Email
        else:
            self.Response["data"] = self.ValidityResponse["data"] # Set Error Message

        return self.Response
