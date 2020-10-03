import re

flight_details = "Flight Savana Airlines a2138"

if(re.search(r"Airlines", flight_details) != None):
    print("Match Found: Airlines")
else:
    print("Match Not Found")

if(re.search(r"a2138$", flight_details) != None):
    print("Match Found: a2138")
else:
    print("Match Not Found")


if(re.search(r"^F", flight_details) != None):
    print("Match Found: Message starts with 'F'")
else:
    print("Match Not Found")


if(re.search(r"F..", flight_details) != None):
    print("Match Found: Word starts with F and two consecutive characters")
else:
    print("Match Not Found")

if(re.search(r"\bSav\b", flight_details) != None):
    print("Match Found:Word with blank spaces on both sides")
else:
    print("Match Not Found")

if(re.search(r"\d$", flight_details) != None):
    print("Match Found: Message ends with number")
else:
    print("Match Not Found")

print("Word replaced in the message:")
print(re.sub(r"Flight", "Plane", flight_details))
print("Word replaced in the message:")
print(re.sub(r"a(\d{4})", r"A\1", flight_details))
