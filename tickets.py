Write a program for selling tickets to IT-events. Each ticket has a unique number and a price. There are four types of tickets: regular ticket, advance ticket (purchased 60 or more days before the event), late ticket (purchased fewer than 10 days before the event) and student ticket.
Additional information:
-advance ticket - discount 40% of the regular ticket price;
-student ticket - discount 50% of the regular ticket price;
-late ticket - additional 10% to the reguler ticket price.
All tickets must have the following properties:
-the ability to construct a ticket by number;
-the ability to ask for a ticket’s price;
-the ability to print a ticket as a String.

import random

class Ticket:
    def __init__(self, price, number):
        self.price = price
        self.number = number

class ticketFactory:
    def __init__(self):
        self.numberPool = set()
        self.ticketPool = []
    def generateTickets(self, amount, price):
        self.numberPool = [random.randint(100, 200) for _ in range(amount)]
        for number in self.numberPool:
            self.ticketPool.append(Ticket(price, number))
            
advanced_tickets = ticketFactory()
advanced_tickets.generateTickets(50, 100)

i = 0

for index in range(50):
    print(advanced_tickets.ticketPool[index].number)
