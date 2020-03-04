departure = ["Auckland", "Wellington", "Christchurch"]
destinations = ["Sydney", "Tonga", "Shanghai", "London"]

print ("welcome to my travel system")
print ("please enter your departure location")
print ("Auckland")
print ("Wellington")
print ("Christchurch")
departure_location=input ("")
if departure_location=="Auckland":
    print (departure[0])
elif departure_location=="Wellington":
    print (departure[1])
else:
    print (departure[2])
