#Crew database
names = ["Picard", "Riker", "Data", "Worf", "Geordi"]
ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lieutenant"]
divisions = ["Command", "Command", "Operations", "Security", "Engineering"]
ids = [101, 102, 103, 104, 105]

def init_database():
    return names, ranks, divisions, ids

def display_menu():
    name = input("Enter crew member name: ")
    print("1. View Crew")
    print("2. Add Crew")
    print("3. Remove Crew")
    print("4. Update Rank")
    print("5. Search Crew")
    print("6. Filter by Division")
    print("7. Display Roster")
    print("8. Calculate Payroll")
    print("9. Count Officers")
    print("10. Exit")
    return int(input(f"Hello {name}, select an option: "))  