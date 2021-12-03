import sys
sys.dont_write_bytecode = True

from geopy.geocoders import Nominatim
from geopy.distance import geodesic

from .Styling.Colors import bc

from .Config import CoreConfig
from .Error import ErrorHandler

class Locate:
    def __init__(self):
        self.Config = CoreConfig()
        self.Error = ErrorHandler()

    def FindByAddress(self, Address: str, PrintResponse: bool = False):
        self.Address: str = Address

        self.PrintResponse: bool = PrintResponse

        try:
            self.Geolocator = Nominatim(user_agent=self.Config.AppName)
            self.TrueLocation: dict = self.Geolocator.geocode(self.Address)

            self.Response: dict = {
                "id": self.TrueLocation.raw["place_id"],
                "class": self.TrueLocation.raw["class"],
                "type": self.TrueLocation.raw["type"],
                "address": self.TrueLocation.raw["display_name"],
                "latitude": self.TrueLocation.raw["lat"],
                "longitude": self.TrueLocation.raw["lon"],
                "altitude": self.TrueLocation.altitude
            }

            if(self.PrintResponse):
                for K, V in self.Response.items():
                    print(f" {bc.BC}{K.title()}: {bc.GC}{V}")

                return self.Response
            else:
                return self.Response
        except Exception:
            print(self.Error.Throw("find_by_address_failed", self.Address))
            return None

    def FindByCoordinates(self, Latitude: str, Longitude: str, PrintResponse: bool = False):
        self.Latitude: str = Latitude
        self.Longitude: str = Longitude

        self.PrintResponse: bool = PrintResponse

        try:
            self.Geolocator = Nominatim(user_agent=self.Config.AppName)
            self.TrueLocation: dict = self.Geolocator.reverse(f"{self.Latitude}, {self.Longitude}")

            self.Response: dict = {
                "id": self.TrueLocation.raw["place_id"],
                "address": self.TrueLocation.raw["display_name"],
                "latitude": self.TrueLocation.raw["lat"],
                "longitude": self.TrueLocation.raw["lon"]
            }

            if(self.PrintResponse):
                for K, V in self.Response.items():
                    print(f" {bc.BC}{K.title()}: {bc.GC}{V}")

                return self.Response
            else:
                return self.Response
        except Exception:
            print(self.Error.Throw("find_by_coordinates_failed", [self.Latitude, self.Longitude]))
            return None

    def GetDistance(self, Measurement: str, FromCoordinates: list, ToCoordinates: list, PrintResponse: bool = False):
        self.Measurement: str = Measurement.lower()
        self.FromCoordinates: list = FromCoordinates
        self.ToCoordinates: list = ToCoordinates

        self.PrintResponse: bool = PrintResponse

        try:
            self.Response: dict = {
                "from": self.FromCoordinates,
                "to": self.ToCoordinates,
                "measurement": "",
                "distance": 0.00,
                "placeholder": "",
            }

            if(self.Measurement == "metre" or self.Measurement == "metres" or self.Measurement == "meter" or self.Measurement == "meters"):
                self.Response["measurement"] = "Metres"
                self.Response["distance"] = round(geodesic(self.FromCoordinates, self.ToCoordinates).meters, 2)
            else:
                self.Response["measurement"] = "Miles"
                self.Response["distance"] = round(geodesic(self.FromCoordinates, self.ToCoordinates).miles, 2)

            self.Response["placeholder"] = f"{self.Response['distance']} {self.Response['measurement']}"

            if(self.PrintResponse):
                for K, V in self.Response.items():
                    print(f" {bc.BC}{K.title()}: {bc.GC}{V}")

                return self.Response
            else:
                return self.Response
        except Exception:
            print(self.Error.Throw("get_distance_failed", [self.FromCoordinates, self.ToCoordinates]))
            return None
