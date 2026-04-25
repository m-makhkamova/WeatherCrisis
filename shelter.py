# Shelter class represents a single emergency shelter with capacity and location
class Shelter:
    # Initialize shelter with name, location (x, y), total capacity, and current occupancy
    def __init__(self, name, location, capacity, current_people):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.current_people = current_people

    # Check if the shelter has enough space for a given number of people
    def has_space(self, people_count):
        if people_count > (self.capacity - self.current_people):
            return False
        else:
            return True

    # Add people to the shelter and update current occupancy
    def add_people(self, people_count):
        self.current_people += people_count
        print(f"{people_count} people added to {self.name}")

    # Return remaining available capacity in the shelter
    def remaining_capacity(self):
        return self.capacity - self.current_people

    # Display shelter details
    def show_shelter(self):
        print(f"Shelter name: {self.name}\nShelter coordinates: {self.location}\nShelter capacity: {self.capacity}\nShelter current people count: {self.current_people}")
        print("---------")