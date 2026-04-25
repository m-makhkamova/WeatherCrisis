class EmergencySystem:
    def __init__(self):
        self.shelters = []
        self.requests_queue = []
        self.assignments = []

    def add_shelter(self, shelter):
        self.shelters.append(shelter)

    def add_request(self, request):
        self.requests_queue.append(request)

    def view_shelters(self):
        for i in self.shelters:
            i.show_shelter()

    def view_requests(self):
        for i in self.requests_queue:
            i.show_request()

    def view_assignments(self):
        if len(self.assignments) == 0:
            print("No assignments yet.")
        else:
            for assignment in self.assignments:
                shelter = assignment[0]
                request = assignment[1]

                print(f"Request name: {request.name}")
                print(f"People assigned: {request.people_count}")
                print(f"Assigned shelter: {shelter.name}")
                print(f"Shelter location: {shelter.location}")
                print("------------------")

    def find_nearest_shelter(self, request):
        nearest_shelter = None
        shortest_distance = float('inf')

        for shelter in self.shelters:
            if shelter.has_space(request.people_count):
                shelter_x = shelter.location[0]
                shelter_y = shelter.location[1]

                request_x = request.location[0]
                request_y = request.location[1]

                distance = ((shelter_x - request_x) ** 2 + (shelter_y - request_y) ** 2) ** 0.5

                if distance < shortest_distance:
                    shortest_distance = distance
                    nearest_shelter = shelter

        return nearest_shelter

    def assign_shelter(self, request):
        nearest_shelter = self.find_nearest_shelter(request)
        if nearest_shelter is None:
            print("No available shelter")
            return
        else:
            nearest_shelter.add_people(request.people_count)
            self.assignments.append([nearest_shelter, request])
            print(f"{request.name} is assigned to {nearest_shelter.name}")

    def view_shelter_status(self):
        for shelter in self.shelters:
            print(f"{shelter.name} has {shelter.remaining_capacity()} space")

