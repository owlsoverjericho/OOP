#-advanced ticket - discount 40% of the regular ticket price;
#-student ticket - discount 50% of the regular ticket price;
#-late ticket - additional 10% to the reguler ticket price

class Ticket:
    def __init__(self, price, number, ticketType):
        self.price = price
        self.number = number
        self.ticketType = ticketType
        
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
        self.myTickets = []
    def generateRegular(self, amount):
        for number in range(amount):
            self.regularTickets.append(Ticket(self.regular, self.regularNumbers[number], "Regular"))
    def generateAdvanced(self, amount):
        for number in range(amount):
            self.advancedTickets.append(Ticket(self.advanced,  self.advancedNumbers[number], "Advanced"))
    def generateStudent(self, amount):
        for number in range(amount):
            self.studentTickets.append(Ticket(self.student,  self.studentNumbers[number], "Student"))
    def generateLate(self, amount):
        for number in range(amount):
            self.lateTickets.append(Ticket(self.late, self.lateNumbers[number], "Late"))

def EventCreator(daysBeforeEvent, regularTickets):
    event = TicketFactory(regularTickets)
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
    print(f"Regular tickets available: {len(event.regularTickets)}, price: {event.regular}$")
    print(f"Student tickets available: {len(event.studentTickets)}, price: {event.student}$")
    print(f"Advanced tickets available: {len(event.advancedTickets)}, price: {event.advanced}$")
    print(f"Late tickets available: {len(event.lateTickets)}, price: {event.late}$\n")
    
def showMenu(event):
    print("1: Buy a regular ticket\n2: Buy a student ticket\n3: Buy an advanced ticket\n4: Buy a late ticket\n5: Show my tickets\n6: exit")
    choice = int(input("Enter an option number:"))
    if choice == 1:
        if(len(event.regularTickets) != 0):
            event.myTickets.append(event.regularTickets[0])
            event.regularTickets.pop(0)
            print("\nThanks for purchasing!\n")
            availableTickets(event)
            showMenu(event)
        else:
            print("Sorry, we`re out of regular tickets\n")
            showMenu(event)
    elif choice == 2:
        if(len(event.studentTickets) != 0):
            event.myTickets.append(event.studentTickets[0])
            event.studentTickets.pop(0)
            print("\nThanks for purchasing!\n")
            availableTickets(event)
            showMenu(event)
        else:
            print("Sorry, we`re out of student tickets\n")
            showMenu(event)
    elif choice == 3:
        if(len(event.advancedTickets) != 0):
            event.myTickets.append(event.advancedTickets[0])
            event.advancedTickets.pop(0)
            print("\nThanks for purchasing!\n")
            availableTickets(event)
            showMenu(event)
        else:
            print("Sorry, we`re out of advanced tickets\n")
            showMenu(event)
    elif choice == 4:
        if(len(event.lateTickets) != 0):
            event.myTickets.append(event.lateTickets[0])
            event.lateTickets.pop(0)
            print("\nThanks for purchasing!\n")
            availableTickets(event)
            showMenu(event)
        else:
            print("Sorry, we`re out of late tickets\n")
            showMenu(event)
    elif choice == 5:
        if (len(event.myTickets) != 0):
            for index in range(len(event.myTickets)):
                print(f"Ticket type: {event.myTickets[index].ticketType}, Ticket number:{event.myTickets[index].number}")
        else:
            print("Sorry, You didn`t buy any, yet")
            showMenu(event)
    else:
        print("\n\nPlease choose a valid option\n")
        availableTickets(event)
        showMenu(event)


while True:
    event = EventCreator(60, 10)
    availableTickets(event)
    showMenu(event)
    break
