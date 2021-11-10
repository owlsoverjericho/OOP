#-advanced ticket - discount 40% of the regular ticket price;
#-student ticket - discount 50% of the regular ticket price;
#-late ticket - additional 10% to the reguler ticket price

class Ticket:
    def __init__(self, price, number):
        self.price = price
        self.number = number
        
class TicketFactory:
    def __init__(self, basePrice):
        self.regular = basePrice
        self.advanced = int(basePrice * 0.4)
        self.student = int(basePrice * 0.5)
        self.late = int(basePrice * 1.1)
        #lists of integer numbers for each ticket type
        self.regularNumbers = list(range(100, 500))
        self.advancedNumbers = list(range(501, 1000))
        self.studentNumbers = list(range(1001, 1500))
        self.lateNumbers = list(range(1501, 2000))
        #these store tickets (instances of Ticket class)
        self.regularTickets = []
        self.advancedTickets = []
        self.studentTickets = []
        self.lateTickets = []
    def generateRegular(self, amount):
        for number in range(amount):
            self.regularTickets.append(Ticket(self.regular, self.regularNumbers[number]))
    def generateAdvanced(self, amount):
        for number in range(amount):
            self.advancedTickets.append(Ticket(self.advanced,  self.advancedNumbers[number]))
    def generateStudent(self, amount):
        for number in range(amount):
            self.studentTickets.append(Ticket(self.student,  self.studentNumbers[number]))
    def generateLate(self, amount):
        for number in range(amount):
            self.lateTickets.append(Ticket(self.late, self.lateNumbers[number]))

def EventCreator(daysBeforeEvent, regularTickets):
    event = TicketFactory(60)
    event.generateRegular(regularTickets)
    event.generateStudent(int(regularTickets * 0.3))
    if daysBeforeEvent >= 60:
        event.generateAdvanced(int(regularTickets * 0.1))
        event.generateLate(0)
    if daysBeforeEvent < 10:
        event.generateAdvanced(0)
        event.generateLate(int(regularTickets * 0.22))
    return event

def availableTickets(event):
    
    

while True:
    event = EventCreator(60, 100)
    
    
    break
    
