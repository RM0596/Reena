
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real , "i+", self.img ,"j")

    def __add__(self,num2):
        Newreal = self.real + num2.real
        Newimg = self.img + num2.img
        return Complex(Newreal,Newimg)
    
    def __sub__(self,num2):
        Newreal = self.real - num2.real
        Newimg = self.img - num2.img
        return Complex(Newreal,Newimg)
    
num1=Complex(1,3)
num1.showNumber()

num2=Complex(5,7)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

num4 = num1 - num2
num4.showNumber()