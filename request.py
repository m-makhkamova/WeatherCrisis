#defines the HelpRequest Class
class HelpRequest: 
  #To create a help request, the arguments of the caller's name, the number of people within their group and location are needed
  def __init__(self, name: str, people_count: int, location):

    #instance attributes
    self.name = name
    self.people_count = people_count
    self.location = location

  #method which displays the all details of a help request: name, number of people and location
  def show_request(self):
    print(f"Name: {self.name}\nPeople: {self.people_count}\nLocation: {self.location}")
    print("---------")