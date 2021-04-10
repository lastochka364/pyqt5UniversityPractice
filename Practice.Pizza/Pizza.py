import time
from uuid import RESERVED_FUTURE, uuid4 as uid


class AddIngrError(Exception):
    """
    This class is custom Exception Class.
    It was made for raising exceptions from 'add_ingredients' method of 'Order' class.
    """
    def __init__(self, message):
        super().__init__(message)
        self.m = message


class Customer:
    """
    This class describes Customer.

    For creating one, you must indicate first, last name and phone number of customer.
    """
    def __init__(self, f_name, l_name, phone):
        if not isinstance(f_name, str) or f_name == '':
            pass
            #raise TypeError("First name must be a string.") 
        if not isinstance(l_name, str or l_name == ''):
            pass
            #raise TypeError("Last name must be a string.")
        if not isinstance(phone, str or phone == ''):
            pass
            #raise TypeError("Phone number must be a string.")
        
        self.f_name, self.l_name, self.phone = f_name, l_name, phone
        self.cid = uid()
        

    def __str__(self):
        return f"Customer: {self.cid}\n" \
               f"{self.l_name}, {self.f_name}. {self.phone}."

class Pizzeria:
    """
    This class describes Pizzeria.

    Through this class, you can discover, what is the pizza-of-the-day for today.
    """
    def __init__(self):
        self.days = {1:"Mon", 2:"Tue", 3:"Wed", 4:"Thu", 5:"Fri", 6:"Sat", 7:"Sun"}
        self.pizzas = {"M":"Margarita", "H":"Hawaiian", "B":"Barbeque", "C":"Carbonara", \
                      "K":"Karri", "P":"Pepperoni", "T":"Texas"}
        self.prices = {"Margarita":20, "Hawaiian":25, "Barbeque":35, \
                       "Carbonara":40, "Karri":50, "Pepperoni":40, "Texas":45}
        self.ingredients = ["Mushrooms", "Pineapple", "Olives", "Corn", \
                            "Mozarella", "Suluguni", "Tofu", "Parmesan"]

    @property
    def pizza_of_the_day(self):
        """
        This method discovers what day of week is today, and returns pizza-of-the-day.
        """
        if self.days[1] == time.ctime()[:3]:
            return f"{self.pizzas['M']}"
        if self.days[2] == time.ctime()[:3]:
            return f"{self.pizzas['H']}"
        if self.days[3] == time.ctime()[:3]:
            return f"{self.pizzas['B']}"
        if self.days[4] == time.ctime()[:3]:
            return f"{self.pizzas['C']}"
        if self.days[5] == time.ctime()[:3]:
            return f"{self.pizzas['K']}"
        if self.days[6] == time.ctime()[:3]:
            return f"{self.pizzas['P']}"
        if self.days[7] == time.ctime()[:3]:
            return f"{self.pizzas['T']}"

    @property
    def photo_of_the_day(self):
        """
        This method discovers what day of a week is today, and returns photo of today's pizza.
        Also, this method was created for qt only.
        """

        if self.days[1] == time.ctime()[:3]:
            return 'img\\pizza\\Margarita.jpg'
        if self.days[2] == time.ctime()[:3]:
            return 'img\\pizza\\Hawaiian.jpg'
        if self.days[3] == time.ctime()[:3]:
            return 'img\\pizza\\Barbeque.jpg'
        if self.days[4] == time.ctime()[:3]:
            return 'img\\pizza\\Carbonara.jpg'
        if self.days[5] == time.ctime()[:3]:
            return 'img\\pizza\\Karri.jpg'
        if self.days[6] == time.ctime()[:3]:
            return 'img\\pizza\\Pepperoni.jpg'
        if self.days[7] == time.ctime()[:3]:
            return 'img\\pizza\\Texas.jpg'

    @property
    def pizzaConsistency(self):
        if self.pizza_of_the_day == "Margarita":
            return f"Red sauce, mozarella, tomatoes, basil."
        if self.pizza_of_the_day == "Hawaiian":
            return f"White sauce, chicken\ham, pineapples, mozarella."
        if self.pizza_of_the_day == "Barbeque":
            return f"BBQ sauce, chicken, gounda and mozarella, onion."
        if self.pizza_of_the_day == "Carbonara":
            return f"Red sauce, ham, mozarella, egg."
        if self.pizza_of_the_day == "Karri":
            return f"Soy sauce, curry sauce, tomato sauce, chicken, mozarella, pepper, onion."
        if self.pizza_of_the_day == "Pepperoni":
            return f"Spicy red sauce, raw smoked sausage, chili pepper, tomatoes, mozarella."
        if self.pizza_of_the_day == "Texas":
            return f"BBQ sauce, smoked chicken, bacon, mushrooms, tomatoes, mozzarella and cheddar."

    def __str__(self):
        return f"Today's pizza-of-the-day is:\n" \
               f"{self.pizza_of_the_day}, {self.prices[self.pizza_of_the_day]}$.\n" \
               f"\n" \
               f"Pizza consistency: \n{self.pizzaConsistency}\n" \
               f"\n" \
               f"All ingredients are for 3$." 

class Order(Pizzeria):
    """
    This class describes Order.

    For instantiating this one, you will necessarily need an instance of "Customer" class.
    """
    def __init__(self, customer=None):
        super().__init__()
        if customer is not None and not isinstance(customer, Customer):
            raise TypeError(f"'{type(customer).__name__}' object cannot be interpreted as a customer.")
        self.customer = customer
        self.added_ingr = []
        self.oid = uid()

    def add_ingredients(self, ingr):
        """
        This method adds ingredients to your purchase and checks all stuff for mistakes.
        """
        try:
            self.added_ingr.append(ingr)
        except:
            raise AddIngrError(f"You should take ingredients from ingr. menu only:\n" \
                               f"{self.ingredients}")

    
    def remove_ingredients(self, ingr):
        """
        This method removes ingredients from your purchase.
        This metod was created for qt only.
        """
        try:
            self.added_ingr.remove(ingr)
        except:
            pass
    
        
    def make_purchase(self):
        """
        This method calculates all the stuff and returns all necessary info.
        """
        total = self.prices[self.pizza_of_the_day] + (len((self.added_ingr)) * 3)
        return f"{self.customer.__str__()}\n" \
               f"\n" \
               f"Order: {self.oid}\n" \
               f"You have bought the next pizza of the day: {self.pizza_of_the_day}.\n" \
               f"Added ingredients: {self.added_ingr}\n" \
               f"Total: {total}$."

    def added(self):
        return self.added_ingr
    
