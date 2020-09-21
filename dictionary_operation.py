crew_details = {
    "Pilot": "Kumar",
    "Co-pilot": "Raghav",
    "Head-Strewardess": "Malini",
    "Stewardess": "Mala"
}
print("Before update:")
print("Co-pilot:", crew_details.get("Co-pilot"))

crew_details.update({"Flight Attendant": "Jane", "Co-pilot": "Henry"})

print("\nAfter update:")
print("Co-pilot:", crew_details.get("Co-pilot"))
print("Flight Attendant:", crew_details["Flight Attendant"])
