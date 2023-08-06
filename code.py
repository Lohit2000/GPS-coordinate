pip install geopy


# from address to latitude and longitude

from geopy.geocoders import Nominatim

# Initialize the geolocator
geolocator = Nominatim(user_agent="myGeolocator)

# Example address
address = "Pakalavari street berhampur"

# Geocode the address
location = geolocator.geocode(address)

# Extract latitude and longitude
latitude = location.latitude
longitude = location.longitude

print(f"Latitude: {latitude}, Longitude: {longitude}")
