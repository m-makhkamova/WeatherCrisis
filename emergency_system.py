# EmergencySystem class manages shelters, requests, and assignments
class EmergencySystem:

    # Initialize system with empty lists for shelters, requests, and assignments
    def __init__(self):
        self.shelters = []
        self.requests_queue = []
        self.assignments = []

    # Add a new shelter to the system
    def add_shelter(self, shelter):
        self.shelters.append(shelter)

    # Add a new help request to the queue
    def add_request(self, request):
        self.requests_queue.append(request)

    # Display all shelters in the system
    def view_shelters(self):
        if len(self.shelters) == 0:
            print("No shelters added yet.")
        else:
            for shelter in self.shelters:
                shelter.show_shelter()

    # Display all pending help requests
    def view_requests(self):
        if len(self.requests_queue) == 0:
            print("No requests yet.")
        else:
            for request in self.requests_queue:
                request.show_request()

    # Display all completed assignments with distance
    def view_assignments(self):
        if len(self.assignments) == 0:
            print("No assignments yet.")
        else:
            for assignment in self.assignments:
                shelter, request, distance = assignment

                print(f"Request name: {request.name}")
                print(f"People assigned: {request.people_count}")
                print(f"Assigned shelter: {shelter.name}")
                print(f"Shelter location: {shelter.location}")
                print(f"Distance: {distance:.2f}")
                print("------------------")

    # Find the nearest shelter with enough capacity for the request
    def find_nearest_shelter(self, request):
        nearest_shelter = None
        shortest_distance = float('inf')

        # Loop through all shelters and calculate distance
        for shelter in self.shelters:
            if shelter.has_space(request.people_count):

                shelter_x = shelter.location[0]
                shelter_y = shelter.location[1]

                request_x = request.location[0]
                request_y = request.location[1]

                # Euclidean distance formula
                distance = ((shelter_x - request_x) ** 2 + (shelter_y - request_y) ** 2) ** 0.5

                # Update nearest shelter if distance is smaller
                if distance < shortest_distance:
                    shortest_distance = distance
                    nearest_shelter = shelter

        return nearest_shelter, shortest_distance

    # Assign a request to the nearest available shelter
    def assign_shelter(self, request):
        nearest_shelter, distance = self.find_nearest_shelter(request)

        # If no shelter is available
        if nearest_shelter is None:
            print("No available shelter")
            return

        # Update shelter occupancy and store assignment
        nearest_shelter.add_people(request.people_count)
        self.assignments.append([nearest_shelter, request, distance])

        print(f"{request.name} is assigned to {nearest_shelter.name} with nearest distance {distance:.2f}")

    # Display remaining capacity for each shelter
    def view_shelter_status(self):
        for shelter in self.shelters:
            print(f"{shelter.name} has {shelter.remaining_capacity()} space")