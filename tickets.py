#Write a program for selling tickets to IT-events. Each ticket has a unique number and a price. There are four types of tickets: regular ticket, advance ticket (purchased 60 or more days before the event), late ticket (purchased fewer than 10 days before the event) and student ticket.
#Additional information:
#-advance ticket - discount 40% of the regular ticket price;
#-student ticket - discount 50% of the regular ticket price;
#-late ticket - additional 10% to the reguler ticket price.
#All tickets must have the following properties:
#-the ability to construct a ticket by number;
#-the ability to ask for a ticket’s price;
#-the ability to print a ticket as a String.

class Ticket:
    def __init__(self, price, number):
        self.price = price
        self.number = number
        
class TicketFactory:
    def __init__(self, basePrice):
        self.regular = basePrice
        self.advanced = int(basePrice * 0.4)
        self.student = int(basePrice * 0.5)
        self.atTheDay = int(basePrice * 1.1)
        self.regularNumbers = list(range(100, 500))
        self.advancedNumbers = list(range(501, 1000))
        self.studentNumbers = list(range(1001, 1500))
        self.atTheDayNumbers = list(range(1501, 2000))
        self.regularPool = []
        self.advancedPool = []
        self.studentPool = []
        self.atTheDayPool = []
    def generateRegular(self, amount):
        for number in range(amount):
            self.regularPool.append(Ticket(self.regular, self.regularNumbers[number]))
    def generateAdvanced(self, amount):
        for number in range(amount):
            self.advancedPool.append(Ticket(self.advanced,  self.advancedNumbers[number]))
    def generateStudent(self, amount):
        for number in range(amount):
            self.studentPool.append(Ticket(self.student,  self.studentNumbers[number]))
    def generateAtTheDay(self, amount):
        for number in range(amount):
            self.atTheDayPool.append(Ticket(self.atTheDay, self.atTheDayNumbers[number]))
            
x = TicketFactory(131);

x.generateRegular(10)

x.generateAdvanced(10)

x.generateStudent(10)

x.generateAtTheDay(10)

print("Regular ticket price:", x.regularPool[0].price)
print("Advanced ticket price:", x.advancedPool[0].price)
print("Student ticket price:", x.studentPool[0].price)
print("At the day ticket price:", x.atTheDayPool[0].price)
