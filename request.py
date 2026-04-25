#defines the HelpRequest Class
class HelpRequest: 
  #To create a help request, the arguments of the caller's name and location are needed
  def __init__(self, name, location):
    #instance attributes
    self.name = name
    self.location = location

  #method to display all the details of a help request together: name and location
  def show_request(self):
    return f"""\n---------- Help Request -----------
    \nName: {self.name}
    \nLocation: {self.location}
    \n----------------------------------"""
