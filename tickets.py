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
    print(f"Regular tickets available: {len(event.regularTickets)}, price: {event.regular}")
    print(f"Student tickets available: {len(event.studentTickets)}, price: {event.student}")
    print(f"Advanced tickets available: {len(event.advancedTickets)}, price: {event.advanced}")
    print(f"Late tickets available: {len(event.lateTickets)}, price: {event.late}\n")
    
def showMenu(event):
    print("1: Buy a regular ticket\n2: Buy a student ticket\n3: Buy an advanced ticket\n4: Buy a late ticket\n5: exit")
    choice = int(input("Enter an option number:"))
    if choice == 1:
        event.regularTickets.pop(0)
        print("\nThanks for purchasing!\n")
        availableTickets(event)
        showMenu(event)
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    else:
        pass
while True:
    event = EventCreator(50, 100)
    availableTickets(event)
    showMenu(event)
    break
