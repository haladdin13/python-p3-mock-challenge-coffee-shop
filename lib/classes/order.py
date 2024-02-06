class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if not hasattr(self, "price"):
            if type(price) == float and 1 <= price <=  10.0:
                self._price = price
            else:
                raise Exception("Price not a float between 1 and 10")
        else:
            raise Exception("Price already set")
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        from classes.customer import Customer
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise Exception("Customer must me an instance of Customer")
        
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        from classes.coffee import Coffee
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise Exception("Coffee must me an instance of Coffee")
    

    