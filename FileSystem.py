import sys
sys.dont_write_bytecode = True

from .Error import ErrorHandler

class FileManager:
    def __init__(self):
        self.Error = ErrorHandler()

    def ReadFromFile(self, FileName: str):
        self.FileName: str = FileName

        self.Response: dict = {
            "status": False,
            "data": []
        }

        try:
            self.File = open(self.FileName, "r")
            self.Lines: list = self.File.readlines(self.Content)
            
            for self.Line in self.Lines:
                self.Response["data"].append(self.Line)
            self.File.close()
        except Exception:
            self.Response["data"] = self.Error.Throw("read_from_file_failed", self.FileName)
        
        self.Response["status"] = True
        return self.Response

    def WriteToFile(self, FileName: str, Content: str):
        self.FileName: str = FileName
        self.Content: str = Content

        self.Response: dict = {
            "status": False,
            "data": ""
        }

        try:
            self.File = open(self.FileName, "w")
            self.File.write(self.Content)
            self.File.close()
        except Exception:
            self.Response["data"] = self.Error.Throw("write_to_file_failed", self.FileName)

        self.Response["status"] = True
        self.Response["data"] = self.FileName        
        return self.Response

    def AppendToFile(self, FileName: str, Content: list):
        self.FileName: str = FileName
        self.Content: list = Content

        self.Response: dict = {
            "status": False,
            "data": []
        }

        try:
            self.File = open(self.FileName, "a")
            for self.Data in self.Content:
                self.File.write(self.Data)
                self.Response["data"].append(self.Data)

            self.File.close()
        except Exception:
            self.Response["data"].append(self.Error.Throw("append_to_file_failed", [self.Data, self.FileName]))

        self.Response["status"] = True
        return self.Response
