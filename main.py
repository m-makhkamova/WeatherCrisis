from emergency_system import EmergencySystem
from request import HelpRequest
from shelter import Shelter

system = EmergencySystem()

while True:
    print("\n--- StormSafe Menu ---")
    print("1. Add Shelter")
    print("2. View Shelters")
    print("3. Add Help Request")
    print("4. View Requests")
    print("5. Assign Shelter")
    print("6. View Shelter Status")
    print("7. Exit")

    choice = input("Enter choice: ")

    # OPTION 1
    if choice == "1":
        name = input("Shelter name: ")
        capacity = int(input("Capacity: "))
        current = int(input("Current people: "))
        x = int(input("X location: "))
        y = int(input("Y location: "))

        shelter = Shelter(name, (x, y), capacity, current)
        system.add_shelter(shelter)
        print("Shelter is added")

    # OPTION 2
    elif choice == "2":
        system.view_shelters()

    # OPTION 3
    elif choice == "3":
        name = input("Request name: ")
        people = int(input("Number of people: "))
        x = int(input("X location: "))
        y = int(input("Y location: "))

        request = HelpRequest(name, people, (x, y))
        system.add_request(request)
        print("Request is added")

    # OPTION 4
    elif choice == "4":
        system.view_requests()

    # OPTION 5
    elif choice == "5":
        if len(system.requests_queue) == 0:
            print("No requests to process")
        else:
            request = system.requests_queue.pop(0)
            system.assign_shelter(request)


    # OPTION 6
    elif choice == "6":
        system.view_shelter_status()

    # EXIT
    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice")