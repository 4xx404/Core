import sys
sys.dont_write_bytecode = True

import re

from .Commands import Command
from .Error import ErrorHandler

class Validation:
    def __init__(self):
        self.Cmd = Command()
        self.Error = ErrorHandler()

        self.EmailRegex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        self.PhoneNumberRegex = r"^\(*\+*[1-9]{0,3}\)*-*[1-9]{0,3}[-. /]*\(*[2-9]\d{2}\)*[-. /]*\d{3}[-. /]*\d{4} *e*x*t*\.* *\d{0,4}$"

        self.DomainExtensions: list = [".com", ".net", ".edu", ".org", ".gov", ".int", ".mil", ".aero", ".cat", ".asia", ".mobi", ".coop", ".travel", ".tel", ".jobs", ".pro", ".biz", ".info", ".store", ".me", ".co", ".online", ".xyz", ".site", ".club", ".shop", ".app", ".live", ".ac", ".ad", ".ae", ".af", ".ag", ".ai", ".al", ".am", ".an", ".ao", ".aq", ".ar", ".as", ".at", ".au", ".aw", ".ax", ".az", ".ba", ".bb", ".bd", ".be", ".bf", ".bg", ".bh", ".bi", ".bj", ".bl", ".bm", ".bn", ".bo", ".br", ".bq", ".bs", ".bt", ".bv", ".bw", ".by", ".bz", ".ca", ".cc", ".cd", ".cf", ".cg", ".ch", ".ci", ".ck", ".cl", ".cm", ".cn", ".co", ".cr", ".cs", ".cu", ".cv", ".cw", ".cx", ".cy", ".cz", ".dd", ".de", ".dj", ".dk", ".dm", ".do", ".dz", ".ec", ".ee", ".eg", ".eh", ".er", ".es", ".et", ".eu", ".fi", ".fj", ".fk", ".fm", ".fo", ".fr", ".ga", ".gb", ".gd", ".ge", ".gf", ".gg", ".gh", ".gi", ".gl", ".gm", ".gn", ".gp", ".gq", ".gr", ".gs", ".gt", ".gu", ".gw", ".gy", ".hk", ".hm", ".hn", ".hr", ".ht", ".hu", ".id", ".ie", ".il", ".im", ".in", ".io", ".iq", ".ir", ".is", ".it", ".je", ".jm", ".jo", ".jp", ".ke", ".kg", ".kh", ".ki", ".km", ".kn", ".kp", ".kr", ".kw", ".ky", ".kz", ".la", ".lb", ".lc", ".li", ".lk", ".lr", ".ls", ".lt", ".lu", ".lv", ".ly", ".ma", ".mc", ".me", ".mf", ".mg", ".mh", ".mk", ".ml", ".mm", ".mn", ".mo", ".mp", ".mq", ".mr", ".ms", ".mt", ".mu", ".mv", ".mw", ".mx", ".my", ".mz", ".na", ".nc", ".ne", ".nf", ".ng", ".ni", ".nl", ".no", ".np", ".nr", ".nu", ".nz", ".om", ".pa", ".pe", ".pf", ".pg", ".ph", ".pk", ".pm", ".pn", ".pr", ".ps", ".pt", ".pw", ".qa", ".re", ".ro", ".rs", ".ru", ".rw", ".sa", ".sb", ".sc", ".sd", ".se", ".sg", ".si", ".sj", ".sk", ".sl", ".sm", ".sn", ".so", ".sr", ".ss", ".st", ".su", ".sv", ".sx", ".sy", ".sz", ".tc", ".td", ".tf", ".tg", ".th", ".tj", ".tk", ".tl", ".tm", ".tn", ".to", ".tp", ".tr", ".tt", ".tv", ".tw", ".tz", ".ua", ".ug", ".uk", ".um", ".us", ".uy", ".uz", ".va", ".vc", ".ve", ".vg", ".vi", ".vn", ".vu", ".wf", ".ws", ".ye", ".yt", ".yu", ".za", ".zm", ".zr", ".zw"]

    def NotEmpty(self, Object: str or list or dict):
        self.Object: str or list or dict = Object

        if(type(self.Object) == str):
            if(self.Object != "" or self.Object != " "):
                return True
            else:
                return False
        elif(type(self.Object) == list):
            if(len(self.Object) > 0):
                return True
            else:
                return False
        elif(type(self.Object) == dict):
            if(len(self.Object.keys()) > 0):
                return True
            else:
                return False
                

    def HasProtocol(self, Link: str):
        self.Link: str = Link

        if(self.Link.startswith("http://") or self.Link.startswith("https://")):
            return True
        else:
            return False

    def HasDomainExtension(self, Link: str):
        self.Link: str = Link
        self.InLinkCount: int = 0

        for self.Extension in self.DomainExtensions:
            if(self.Extension in self.Link):
                self.InLinkCount += 1
            else:
                continue
        
        if(self.InLinkCount > 0):
            return True
        else:
            return False
        
    def StartsOrEndsWith(self, TrailType: str, StringValues: str, CharacterToCheck: str):
        self.TrailType: str = TrailType.lower() # start || end
        self.StringValue: str = StringValues # example: "does this string have a space?"
        self.CharacterToCheck: str = CharacterToCheck # example: " " // Space

        if(self.TrailType == "start"):
            if(self.StringValue.startswith(self.CharacterToCheck)):
                return True
            else:
                return False
        elif(self.TrailType == "end"):
            if(self.StringValue.endswith(self.CharacterToCheck)):
                return True
            else:
                return False

    def IsEmailFormat(self, Email: str):
        self.Email: str = Email

        self.Response: dict = {
            "status": False,
            "data": ""
        }

        if(self.NotEmpty(self.Email)):
            if(re.fullmatch(self.EmailRegex, self.Email)):
                self.Response["status"] = True
                self.Response["data"] = self.Email
            else:
                self.Response["data"] = self.Error.Throw("invalid_email_format", self.Email)
        else:
            self.Response["data"] = self.Error.Throw("empty_email_value", None)

        return self.Response

    def IsPhoneNumberFormat(self, PhoneNumber: str):
        self.PhoneNumber: str = PhoneNumber

        self.Response: dict = {
            "status": False,
            "data": ""
        }

        if(self.NotEmpty(self.PhoneNumber)):
            if(self.PhoneNumber.startswith("+")):
                self.PhoneNumber = self.PhoneNumber
            else:
                self.PhoneNumber = f"+{self.PhoneNumber}"

            if(re.fullmatch(self.PhoneNumberRegex, self.PhoneNumber)):
                self.Response["status"] = True
                self.Response["data"] = self.PhoneNumber
            else:
                self.Response["data"] = self.Error.Throw("invalid_phone_number_format", self.PhoneNumber)
        else:
            self.Response["data"] = self.Error.Throw("empty_phone_number_value", None)

        return self.Response

    def IsLinkFormat(self, Link: str):
        self.Link: str = Link

        self.Response: dict = {
            "status": False,
            "data": ""
        }

        if(self.NotEmpty(self.Link)):
            if(self.HasProtocol(self.Link)):
                if(self.HasDomainExtension(self.Link)):
                    self.Response["status"] = True
                    self.Response["data"] = self.Link
                else:
                    self.Response["data"] = self.Error.Throw("invalid_link_domain_extension", self.Link)
            else:
                self.Response["data"] = self.Error.Throw("invalid_link_protocol", self.Link)
        else:
            self.Response["data"] = self.Error.Throw("empty_link_value")

        return self.Response
