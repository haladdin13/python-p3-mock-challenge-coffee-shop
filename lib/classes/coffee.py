class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, 'name'):
            if type(name) == str and len(name) >= 3:
                self._name = name
            else:
                raise Exception("Coffee name must be a string greater than 3 characters")
        else:
            raise Exception("Coffee already has name")
        
    def orders(self):
        from classes.order import Order
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list(set([order.customer for order in self.orders()]))
    
    def num_orders(self):
        return len([order for order in self.orders() if order.coffee == self])
    
    def average_price(self):
        price_average = [
            order.price for order in self.orders() if order.coffee == self
        ]
        return sum(price_average) / len(price_average)