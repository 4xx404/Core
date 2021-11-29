# Config  
* File Location: **Core/Config.py**  

The **Config** class is used to keep commonly required values that the program relies on.  

# Set Config Variable  
In **Core/Config.py**:
```
class CoreConfig:
    def __init__(self):
        self.AppName = "FruityLoop"
```

# Use Config Variable  
In your program:
```
from Core.Config import CoreConfig

print(CoreConfig().AppName)

Result: FruityLoop
```
