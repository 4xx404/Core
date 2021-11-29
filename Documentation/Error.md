# **Error**
* File Location: **Core/Error.py**

The **Error** class makes it easy to handle your programs errors using if/else statements. You can also easily add errors into the handler.

# Adding Custom Errors  
In **Core/Error.py** **DefinedErrors**, define the error tag (**must** be separated by **underscores**):
```
self.DefinedErrors = [
    "number_too_high",
]
```

In the **Core/Error.py** function **Throw()**, add the error message:
```
elif(self.ErrorType == "number_too_high"):
    # Without passing in any ErrorData where you dont need to show what failed
    return f"\n{sd.eBan} Number is too high\n"
    # Result: Number is too high

    # With passing in ErrorData where you want to show what failed
    return f"\n{sd.eBan} Number {bc.RC}{self.ErrorData}{bc.BC} is too high\n"
    # Result: Number 10 is too high
```

# Throw Error  
In your program:
```
from Core.Error import ErrorHandler

def MyScript(self):
    self.Error = ErrorHandler()

    self.MyNum = 10
    if(self.MyNum <= 5):
        print(f"{self.MyNum} is less than or equal to 5")
    else:
        # Without passing in any ErrorData
        print(self.Error.Throw("number_too_high", None))
        
        # With passing in ErrorData
        print(self.Error.Throw("number_too_high", self.MyNum))
```
