def liters_100km_to_miles_gallon(liters):
    galone = liters / 3.785411784  # galon_to_litre = 3.785411784
    miles = 100000 / 1609.344  # miles_to_km = 1609.344
    return miles / galone


def miles_gallon_to_liters_100km(galones):
    km = 100000 / 1609.344
    liters = galones / 3.785411784
    return km/liters
    
    
    
    


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
