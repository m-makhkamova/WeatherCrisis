#dictionary for valid possible weather crises entered in a help request
types = {'Flood': 4, 'Storm': 2, 'Hurricane': 5, 'Wildfire': 5, 'Earthquake': 3}

#defines the HelpRequest C
class HelpRequest: 
  #To create a help request, the arguments of the caller's name, the number of people within their group and location are needed
  def __init__(self, name: str, people_count: int, location):
    #instance attributes
    self.name = name
    self.people_count = people_count
    self.location = location

  #method which displays the all details of a help request: name, number of people and location
  def show_request(self):
      print(
        f"Request name:{self.name}\nRequest coordinates:{self.location}\nRequest current people count:{self.current_people}")
      print("---------")
