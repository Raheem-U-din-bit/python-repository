class Employee:
  company = "ITC"
  def show(self):
    print(f"the name is {self.name} and the salary is {self.salary}")
class Programmer(Employee):
    company = "ITC Infotech"
    
    def showLanguage(self):
      print(f"the name is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programmer()
print(a.company, b.company)
a.show()



















































'''
class Train:
  def __init__(self, num_of_seats=50):
    self.num_of_seats = num_of_seats
  def book_ticket(self, num):
    if num <= 0:
        return "Invalid number of tickets!"
    if num > self.num_of_seats:
        return f"Sorry, not enough seats available."
    self.num_of_seats -= num
      
    return f"{num}, Ticket booked! seats left: {self.num_of_seats}"
  def status(self):
     if(self.num_of_seats == 0):
        return "no more seats are available"
     else:
        return f"\n{self.num_of_seats} seats are available"
  def fare(self, From, to):
    if(From == "dera ismail khan" and to == "islamabad"):
        return f"\nthe fare from {From} to {to} is 1800"
    elif(From == "dera ismail khan" and to == "karachi"):
       return f"\nthe fare from {From} to {to} is 3500"
    
cmer = Train()
print(cmer.book_ticket(2), cmer.status(), cmer.fare("dera ismail khan", "islamabad"))
'''
