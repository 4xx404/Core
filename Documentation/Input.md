# Input
* File Location: **Core/Input.py**

The **Input** class helps to handle user input & cannot return anything other than input that matches the valid format. This means that the user is entered into an input prompt loop while the expected value is an incorrect format. **Input** & [**Validity**](https://github.com/4xx404/core/blob/main/Documentation/Validity.md) are hybrid modules meaning that they often rely on each other.  

# Prompt User Input  
```
from Core.Input import InputManager

Link = InputManager().SetLink()
print(Link) # Only returned if the value is a valid url
```

* InputManager().SetLink() can also take a **Placeholder** parameter allowing you to set the input placeholder when prompting the user for input.  
```
from Core.Input import InputManager
Link = InputManager().SetLink('Target URL')

# Result: The user sees 'Target URL: ' when prompted for input
```
