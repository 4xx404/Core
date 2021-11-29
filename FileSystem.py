import sys
sys.dont_write_bytecode = True

from .Error import ErrorHandler

class FileManager:
    def __init__(self):
        self.Error = ErrorHandler()

    def WriteToFile(self, FileName, Content):
        self.FileName = FileName
        self.Content = Content

        self.Response = {
            "status": False,
            "data": ""
        }

        try:
            self.File = open(self.FileName, "w")
            self.File.write(self.Content)
            self.File.close()
            self.Response["status"] = True
            self.Response["data"] = self.FileName
        except Exception:
            self.Response["data"] = self.Error.Throw("write_to_file_failed", self.FileName)
        
        return self.Response
