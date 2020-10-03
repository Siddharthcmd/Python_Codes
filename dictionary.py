crew_details = {
    "THEIR": "THEIR", "BUSINESS": "BISINESS",
    "WINDOWS": "WINDMILL", "WERE": "WEAR", "SAMPLE": "SAMPLE"
}
# print("Pilots:", crew_details["Pilot"],
#     "and Co-Pilot:", crew_details["Co-Pilot"])
count_list = []
print("\nIterating the dictionary using items function")
for key, value in crew_details.items():
    count = 0
    #key = sorted(key)
    #value = sorted(value)
    if (len(key) == len(value)):
        print(key + ":" + value)
        for i in range(0, len(key)):
            if (key[i] != value[i]):
                count += 1
    if (count <= 2):
        count_list.append(count)
print(count_list)
