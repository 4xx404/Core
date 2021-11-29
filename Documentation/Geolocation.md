# Geolocation
* File Location: **Core/Geolocation.py**

The **Geolocation** class is a location based module to help collect information about a location. The functions include **FindByAddress()**, **FindByCoordinates()** & **GetDistance()**. The result from each function is returned as a dictionary with the collected data & can be called as shown below...  

# Find By Address  
```
from Core.Geolocation import Locate

AddressData = Locate().FindByAddress("175 5th Avenue NYC")
"""
Find By Address Response Keys:
AddressData['id'] - The geopy registered location ID
AddressData['class'] - The location class (example: tourism)
AddressData['type'] - The location type (example: attraction)
AddressData['address'] - String holding the full address value
AddressData['latitude'] - The location latitude value
AddressData['longitude'] - The location longitude value
AddressData['altitude'] - The altitude of the location
"""
```

# Find By Coordinates  
```
from Core.Geolocation import Locate

Latitude = 41.49008
Longitude = -71.312796

AddressData = Locate().FindByCoordinates(Latitude, Longitude)
"""
Find By Coordinates Response Keys:
AddressData['id'] - The geopy registered location ID
AddressData['address'] - String holding the full address value
AddressData['latitude'] - The location latitude value
AddressData['longitude'] - The location longitude value
"""
```

# Get Distance  
```
from Core.Geolocation import Locate

FromCoordinates = [41.49008, -71.312796]
ToCoordinates = [41.499498, -81.695391]

# PrintResponse is False by default, which does not print the formatted response to the console
Distance = Locate().GetDistance(Measurement='miles', ToCoordinates=[41.49008, -71.312796], FromCoordinates=[41.499498, -81.695391], PrintResponse=True)

"""
Get Distance Response Keys:
Distance['from'] - From location coordinates
Distance['to'] - To location coordinates
Distance['measurement'] - Measurement of distance between From/To coordinates in metres or miles
Distance['distance'] - The calculated distance as a float value
Distance['placeholder'] - Banner for displaying the result in the format '432.34 Miles'
"""
```
