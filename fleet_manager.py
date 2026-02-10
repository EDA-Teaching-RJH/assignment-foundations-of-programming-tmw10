#Crew database
names = ["Picard", "Riker", "Data", "Worf", "Geordi"]
ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lieutenant"]
divisions = ["Command", "Command", "Operations", "Security", "Engineering"]
ids = [101, 102, 103, 104, 105]

def init_database():
    return names, ranks, divisions, ids

#display the menu of user inputs
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

#Add a crew member to the database
def add_crew_member(names, ranks, divisions, ids):
    new_id = int(input("Enter ID: "))
    if new_id in ids:
        print("ID already exists. Crew member not added.")
        return
    new_name = input("Enter name: ")
    new_rank = input("Enter rank: ")
    if new_rank not in ["Captain", "Commander", "Lt. Commander", "Lieutenant"]:
        print("Invalid rank. Crew member not added.")
        return
    new_division = input("Enter division: ")

    names.append(new_name)
    ranks.append(new_rank)
    divisions.append(new_division)
    ids.append(new_id)
    print("Crew member added successfully.")

    #Remove a crew member from the database
def remove_crew_member(names, ranks, divisions, ids):
    remove_id = int(input("Enter ID of crew member to remove: "))
    if remove_id not in ids:
        print("ID not found. No crew member removed.")
        return
    idx = ids.index(remove_id)
    names.pop(idx)
    ranks.pop(idx)
    divisions.pop(idx)
    ids.pop(idx)
    print(f"Crew member with ID {remove_id} removed successfully.")

    