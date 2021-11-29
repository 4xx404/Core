import sys
sys.dont_write_bytecode = True

import cv2

from .Config import CoreConfig
from .Request import RequestHandler
from .FileSystem import FileManager
from .Error import ErrorHandler

class Recognise:
    def __init__(self):
        self.Config = CoreConfig()
        self.Request = RequestHandler()
        self.FileSys = FileManager() 
        self.Error = ErrorHandler()

        self.CascadeFile = self.Config.CascadeFilePath
