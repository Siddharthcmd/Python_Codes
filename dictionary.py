crew_details = {
    "Pilot": "Kumar",
    "Co-Pilot": "Raghav",
    "Head-Strewardess": "Malini",
    "Stewardess": "Mala"
}
print("Pilots:", crew_details["Pilot"],
      "and Co-Pilot:", crew_details["Co-Pilot"])

print("\nIterating the dictionary using items function")
for key, value in crew_details.items():
    print(key, ":", value)
