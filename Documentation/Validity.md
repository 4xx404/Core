# Validity
* File Location: **Core/Validity.py**  

The **Validity** & [**Input**](https://github.com/4xx404/core/blob/main/Documentation/Input.md) are hybrid modules meaning that they often rely on each other. For example, **Validation().IsLinkFormat('example.com')** runs 3 validation checks from only having to call **InputManager().SetLink()**. The 3 validation checks that get ran are; **NotEmpty()**, **HasProtocol()** & **HasDomainExtension()**. This means that in your script, you only need to call **InputManager().SetLink()** without calling any of the validation methods (As shown below in [**Input**](https://github.com/4xx404/core/blob/main/Documentation/Input.md)). When **Validation** is not built into the Input function, Validation functions return a dictionary named **Response** consisting of 2 key:value pairs:  
1. **status** (Boolean)
2. **data** (String)) 

# Validation Usage  
```
from Core.Validity import Validation

ValidityCheck = Validation().HasProtocol("hello world")

if(ValidityCheck['status']):
    print(f"{ValidityCheck['data']} starts with http:// or https://")
else:
    print({ValidityCheck['data']}) # If validation fails, the 'data' value holds the error message
```
