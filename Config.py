import sys
sys.dont_write_bytecode = True

class CoreConfig:
    def __init__(self):
        # Default Application Variables
        self.AppName = "TestName" # Enter your app name
        self.Version = "V1"
        self.Headers = {
            'Accept-Language': 'en-US,en;q=0.5',
            'Cache-Control': 'no-cache',
            'User-Agent': f'{self.AppName}.{self.Version}'
        }

        # Database Variables
        self.SqliteDatabasePath = f"{self.AppName}.db"
        self.DBHost = "localhost"
        self.DBName = "" # Enter the name of your database
        self.DBUser = "root" # Usually root, change here if your database user is different
        self.DBPass = "" # If your mysql allows an empty password leave empty, else enter your password

        # CV2 Variables
        self.CascadeFilePath = "Core/Data/haarcascade_frontalface_default.xml"
