from uuid import uuid4 as uid
import datetime


class Tickets:
    """
    This class describes tickets.

    This is the base class for future inheritating by "Event" class.
    """
    def __init__(self):
        self.Type = ""
        self.dct = {}
        self.regularPrice = int()

    def get_tick_info(self, ticket):
        """
        This method gives you info about each ticket.
        """
        if ticket == "Regular":
            return f"Regular Ticket:\n" \
                   f"This is the most common ticket, full price."
        if ticket == "Early":
            return f"Eraly Ticket:\n" \
                   f"This ticket is 40% off."
        if ticket == "Student":
            return f"Student Ticket:\n" \
                   f"This one is for students, 50% off.\n" \
                   f"Can be purchased only with a student card!"
        if ticket == "Late":
            return f"Late Ticket:\n" \
                   f"This ticket is 10% increase. (Can be purchased fewer than 10 days before the event)."
        else:
            return f"You have enetered an incorrect value. Please, try again."
            
    def get_tick_price(self, ticket):
        """
        This method gives info about tickets prices.
        """
        if ticket == "Regular":
            return self.regularPrice
        if ticket == "Early":
            self.earlyPrice = float('{:.3f}'.format(self.regularPrice - (self.regularPrice / 100) * 40))
            return self.earlyPrice
        if ticket == "Student":
            self.studentPrice = float('{:.3f}'.format(self.regularPrice - (self.regularPrice / 100) * 50))
            return self.studentPrice
        if ticket == "Late":
            self.latePrice = float('{:.3f}'.format(self.regularPrice + (self.regularPrice / 100) * 10))
            return self.latePrice
    
    def buy_ticket(self, ticket):
        """
        This method allows you to buy some ticket.
        """
        if not isinstance(ticket, str):
            raise TypeError(f"Your input type must be a string. Your's one: {type(ticket)}")
        else:
            if ticket == "Regular":
                rt = str(uid())
                self.Type = "Regular"
                self.dct.update({rt : self.Type})
                return f"You just purchased regular ticket for {self.regularPrice}$\n" \
                    f"It's unique number is: {rt}."
            if ticket == "Early":
                at = str(uid())
                self.Type = "Early"
                self.dct.update({at : self.Type})
                return f"You just purchased early ticket for {self.earlyPrice}$\n" \
                   f"It's unique number is: {at}."
            if ticket == "Student":
                st = str(uid())
                self.Type = "Student"
                self.dct.update({st : self.Type})
                return f"You just purchased student ticket for {self.studentPrice}$\n" \
                   f"It's unique number is: {st}."
            if ticket == "Late":
                lt = str(uid())
                self.Type = "Late"
                self.dct.update({lt : self.Type})
                return f"You just purchased late ticket for {self.latePrice}$\n" \
                   f"It's unique number is: {lt}."

    def construct_tick_by_num(self, val):
        """
        This method allows you to discover ticket type by it's unique number.
        """
        if val in self.dct:
            return f"Your ticket type is {self.dct[val]}"
        else:
            return f"No such ticket in our base."

    def set_tick_price(self, val):
        self.regularPrice = val

    def get_dct(self):
        return self.dct


class Event(Tickets):
    def __init__(self, day=None, month=None, year=None, tick_price=None, info=None):
        super().__init__()
        if not isinstance(day, int):
            raise TypeError("Day must be a number.")
        if not isinstance(month, int):
            raise TypeError("Month must be a number.")
        if not isinstance(year, int):
            raise TypeError("Year must be a number.")
        if not isinstance(info, str):
            raise TypeError("Info must be a string.")

        self.event_date = datetime.date(year, month, day)
        self.event_info = info
        self.tick_price = tick_price
        self.set_tick_price(self.tick_price)

    def __str__(self):
        return f"Date of the Event: {self.event_date}\n" \
               f"Event info: {self.event_info}\n" \
               f"Regular Ticket Price: {self.tick_price}$"


"""
if __name__== "__main__":

    event1 = Event(4, 9, 2020, 50, "Epam is the best company in the world.")
    print(event1)

    print(event1.get_tick_info("Early"))
    print()
    print(event1.get_tick_price("Early"))
    print()
    print(event1.buy_ticket("Early"))
    print()
    print(event1.construct_tick_by_num())
    print()
   
    event2 = Event(11, 11, 2020, "The most biggest sale on Ali.")
    print(event2)

    print(event2.get_tick_info("Student"))
    print(event2.get_tick_price("Student"))
    print(event2.buy_ticket("Student"))
    print(event2.construct_tick_by_num())
""" 

    
