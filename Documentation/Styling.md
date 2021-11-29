# Styling  
* File Locations: **Core/Styling/Banners.py** || **Core/Styling/Colors.py**  

The **Styling** class consists of the **Banners** & **Colors** modules & are hybrid modules often in use together. The **Banners** module includes a Logo variable for your programs ascii art banner as well as status banners such as **SuccessBanner(sBan)**, **ErrorBanner(eBan)** & **InfoBanner(iBan)**.  

# Banner Usage  
```
from Core.Styling.Banners import sd

print(sd.Logo)
print(sd.sBan)
print(sd.eBan)
print(sd.iBan)
```

# Colors Usage  
```
from Core.Styling.Colors import bc

print(f"{bc.RC}This text is red")
print(f"{bc.GC}This text is green")
print(f"{bc.BC}This text is blue")
```
