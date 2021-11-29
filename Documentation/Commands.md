# Commands  
* File Location: **Core/Commands.py**  

The Commands class consists of many functions that handle common system actions such as the **Clear** command which clears the console of any output as well as printing your programs ascii art logo.  

# Command Usage  
```
from Core.Commands import Command

# Clear the console
Command().Clear()

# Move a file or directory
FileToMove = "path/to/example.txt"
WhereToMoveFile = "home/new-directory"
if(Command().MoveFile(FileToMove, WhereToMoveFile)):
    # Success, do something
else:
    # Error, do something
```
