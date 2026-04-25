#dictionary for valid possible weather crises entered in a help request
types = {'Flood': 4, 'Storm': 2, 'Hurricane': 5, 'Wildfire': 5, 'Earthquake': 3}

#defines the HelpRequest C
class HelpRequest: 
  #To create a help request, the arguments of the caller's name, the number of people within their group, crisis/danger type, disaster severity,
  #and location are needed
  def __init__(self, name: str, people_count: int, danger_type: str, disaster_severity: int, location):
    if danger_type.title() not in types: #an error will be raised if a valid crisis is not entered
      raise ValueError(("Invalid danger type"))
    #instance attributes
    self.name = name
    self.people_count = people_count
    self.danger_type = danger_type.title()
    self.disaster_severity = disaster_severity
    self.location = location

  #method to deteermine the priority of a help request
  def get_priority(self):
    #within the get_priority method, is the get_person_severity method
    #this calculates one of the three severity factors that determine priority
    def get_person_severity(people_count): #this method takes the amount of people in the help request as an argument
      person_severity = 0 #severity is initialize at 0
      if people_count <= 50: #if less than 50 people need help, person severity is rated a level 1
        person_severity = 1
      elif people_count <= 100: #if more than 50 but 100 or less people need help, person severity is rated a level 2
        person_severity = 2
      elif people_count <= 500: #if more than 100 but 500 or less people need help, person severity is rated a level 3
        person_severity = 3
      elif people_count <= 1000: #if more than 500 but 1000 or less people need help, person severity is rated a level 4
        person_severity = 4
      else: #otherwise, when more than 1000 people are in need in the help request, the severity is rated a level 5
        person_severity = 5
      return person_severity #returns the severity level based on the number of people in need 

    #variable with calculates the overall priority level of a help request based on the crisis type, number of people, and inputted severity level
    priority_level = self.disaster_severity + types[self.danger_type] + get_person_severity(self.people_count)
    return f"Crisis priority level: {priority_level}" #returns the priority level of the help request

  #method which displays the all details of a help request: name, number of people, the crisis, the severity, and location
  def show_request(self):
    return f"""\n---------- Help Request -----------
    \nName: {self.name}
    \nPeople: {self.people_count}
    \nDanger Type: {self.danger_type}
    \nDisaster Severity: {self.disaster_severity}
    \nLocation: {self.location}
    \n----------------------------------"""
