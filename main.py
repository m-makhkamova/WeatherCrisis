# Import classes from other files
from emergency_system import EmergencySystem
from request import HelpRequest
from shelter import Shelter

# Create main system object that will store shelters and requests
system = EmergencySystem()

# Infinite loop to keep program running until user exits
while True:
    # Display menu options to the user
    print("\n--- StormSafe Menu ---")
    print("1. Add Shelter")
    print("2. View Shelters")
    print("3. Add Help Request")
    print("4. View Requests")
    print("5. Assign Shelter")
    print("6. View Shelter Status")
    print("7. View assignments")
    print("8. Exit")

    # Take user input (always string)
    choice = input("Enter choice: ")

    # OPTION 1: Create and add a new shelter
    if choice == "1":
        name = input("Shelter name: ")
        capacity = int(input("Capacity: "))
        current = int(input("Current people: "))
        x = int(input("X location: "))
        y = int(input("Y location: "))

        # Create Shelter object and add to system
        shelter = Shelter(name, (x, y), capacity, current)
        system.add_shelter(shelter)
        print("Shelter is added")

    # OPTION 2: Display all shelters
    elif choice == "2":
        system.view_shelters()

    # OPTION 3: Create and add a help request
    elif choice == "3":
        name = input("Request name: ")
        people = int(input("Number of people: "))
        x = int(input("X location: "))
        y = int(input("Y location: "))

        # Create HelpRequest object and add to queue
        request = HelpRequest(name, people, (x, y))
        system.add_request(request)
        print("Request is added")

    # OPTION 4: Display all pending requests
    elif choice == "4":
        system.view_requests()

    # OPTION 5: Assign first request in queue to nearest shelter
    elif choice == "5":
        # Check if there are requests to process
        if len(system.requests_queue) == 0:
            print("No requests to process")
        else:
            # FIFO behavior: process first request in queue
            request = system.requests_queue.pop(0)
            system.assign_shelter(request)

    # OPTION 6: Show remaining capacity of each shelter
    elif choice == "6":
        system.view_shelter_status()

    # OPTION 7: Show completed assignments
    elif choice == "7":
        system.view_assignments()

    # OPTION 8: Exit program
    elif choice == "8":
        print("Exiting...")
        break

    # Handle invalid menu input
    else:
        print("Invalid choice")