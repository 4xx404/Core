import sys, os
sys.dont_write_bytecode = True

from .Styling.Banners import sd

from .Error import ErrorHandler

class Command:
    def __init__(self):
        self.Error = ErrorHandler()

        self.Logo: str = sd.Logo

    def Clear(self):
        os.system("clear")
        print(self.Logo)

    def MoveFile(self, FileToMove: str, Destination: str):
        self.FileToMove: str = FileToMove
        self.Destination: str = Destination

        try:
            os.system(f"sudo mv {self.FileToMove} {self.Destination}")
        except Exception:
            print(self.Error.Throw("file_move_failed", [self.FileToMove, self.Destination]))
            return False

        return True

    def MakeDirectory(self, DirectoryPath: str):
        self.DirectoryPath: str = DirectoryPath

        try:
            os.mkdir(self.DirectoryPath)
        except Exception:
            print(self.Error.Throw("create_directory_failed", self.DirectoryPath))
            return False

        return True

    def ListDirectory(self, DirectoryToView: str):
        self.DirectoryToView: str = DirectoryToView

        try:
            os.listdir(self.DirectoryToView)
        except Exception:
            print(self.Error.Throw("list_directory_failed", self.DirectoryToView))
            return False

        return True

    def ChangeDirectory(self, DirectoryToMoveTo: str):
        self.DirectoryToMoveTo: str = DirectoryToMoveTo

        try:
            os.chdir(self.DirectoryToMoveTo)
        except Exception:
            print(self.Error.Throw("change_directory_failed", self.DirectoryToMoveTo))
            return False

        return False

    def RenameFileOrDirectory(self, FileOrDirectoryName: str, NewFileOrDirectoryName: str):
        self.FileOrDirectoryName: str = FileOrDirectoryName
        self.NewFileOrDirectoryName: str = NewFileOrDirectoryName
        try:
            os.rename(self.FileOrDirectoryName, self.NewFileOrDirectoryName)
        except Exception:
            print(self.Error.Throw("rename_file_or_dir_failed", [self.FileOrDirectoryName, self.NewFileOrDirectoryName]))
            return False
        
        return True

    def RemoveDirectory(self, DirectoryToDelete: str):
        self.DirectoryToDelete: str = DirectoryToDelete

        try:
            os.rmdir(self.DirectoryToDelete)
        except Exception:
            print(self.Error.Throw("remove_directory_failed", self.DirectoryToDelete))
            return False

        return True
