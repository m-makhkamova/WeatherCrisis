#defines the HelpRequest C
class HelpRequest: 
  #To create a help request, the arguments of the caller's name, the number of people within their group, crisis/danger type, disaster severity,
  #and location are needed
  def __init__(self, name: str, location):
    if danger_type.title() not in types: #an error will be raised if a valid crisis is not entered
      raise ValueError(("Invalid danger type"))
    #instance attributes
    self.name = name
    self.people_count = people_count
    self.danger_type = danger_type.title()
    self.disaster_severity = disaster_severity
    self.location = location

  #method which displays the all details of a help request: name, number of people, the crisis, the severity, and location
  def show_request(self):
    return f"""\n---------- Help Request -----------
    \nName: {self.name}
    \nPeople: {self.people_count}
    \nDanger Type: {self.danger_type}
    \nDisaster Severity: {self.disaster_severity}
    \nLocation: {self.location}
    \n----------------------------------"""
