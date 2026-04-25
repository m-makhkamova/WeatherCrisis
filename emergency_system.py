class EmergencySystem:
    shelters = []
    requests_queue = []
    assignments = []

    def add_shelter(self, shelter):
        self.shelters.append(shelter)

    def add_requests(self, request):
        self.requests_queue.append(request)

    def view_shelters(self):
        for i in self.shelters:
            i.show_info()

    def view_requests(self):
        for i in self.requests_queue:
            i.show_info()

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
        nearest_shelter.current_people+=request.people_count
        self.assignments.append([nearest_shelter, request])

    def view_shelter_status(self):
        for shelter in self.shelters:
            print(f"{shelter.name} has {shelter.remaining_capacity()} space")

