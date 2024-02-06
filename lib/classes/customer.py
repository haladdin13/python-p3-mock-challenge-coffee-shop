class Customer:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) == str and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise Exception("Invalid name")
    
        
    def orders(self):
        from classes.order import Order
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))
    
    def create_order(self, coffee, price):
        from classes.order import Order
        order = Order(self, coffee, price)
        Order.all.append(order)
        return order