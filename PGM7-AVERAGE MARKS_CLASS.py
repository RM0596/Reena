class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("Hello....")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum +=val
        print("hi",self.name,"your average score is : ",sum/2)

Student1=Student("Reena",[12,34])
Student1.get_avg()
Student1.hello()

