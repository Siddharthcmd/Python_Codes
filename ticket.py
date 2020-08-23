# The flight ticket rates for a round-trip (Mumbai->Dubai) were as follows:
# Rate per Adult: Rs. 37550.0
# Rate per Child: 1/3rd of the rate per adult
# Service Tax: 7% of the ticket amount (including all passengers)
# As it was a holiday season, the airline also offered 10% discount on the final
# ticket cost (after inclusion of the service tax).
#
# Find and display the total ticket cost for a group which had adults and children.

def total_ticket_cost(totalAdults, totalKids):
    cost = 37550*totalAdults+(37550/3)*totalKids
    totalCost = cost-((cost/100)*3)
    return totalCost


adults = input("enter the total number of adults:")
kids = input("enter the total number of kids:")
total = total_ticket_cost(adults, kids)
print("amount to be paid:", total)
