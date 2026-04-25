class Shelter:
    def __init__(self, name, location, capacity, current_people):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.current_people = current_people

    def has_space(self, people_count):
        if people_count > (self.capacity-self.current_people):
            return False
        else:
            return True

    def add_people(self, people_count):
        self.current_people += people_count
        print(f"{people_count} people added to {self.name}")

    def remaining_capacity(self):
        return self.capacity - self.current_people

    def show_shelter(self):
        print(f"Shelter name:{self.name}\nShelter coordinates:{self.location}\nShelter capacity:{self.capacity}\nShelter current people count:{self.current_people}")
        print("---------")

