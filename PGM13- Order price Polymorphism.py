class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,Order2):
        return self.price > Order2.price

Order1=Order("Mango",45)
print(Order1.item,Order1.price)

Order2=Order("Apple",50)
print(Order2.item,Order2.price)

print(Order1 > Order2)