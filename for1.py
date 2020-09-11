for passenger in "FC", "A", "FC", "C", "FA",  "SP", "A", "A":
    if(passenger == "FC" or passenger == "FA"):
        print("No check required")
        continue

    if(passenger == "SP"):
        print("Declare emergency in the airport")
        break

    if(passenger == "A" or passenger == "C"):
        print("Proceed with normal security check")

    print("Check the person")
    print("Check for cabin baggage ")
