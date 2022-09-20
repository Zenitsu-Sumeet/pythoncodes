class class1():

   def display1(self):
       fname=input("enter the firstname: ")
       print("your firstname is ",fname)
class class2():

   def display2(self):
       lname = input("enter the lastname: ")
       print("your last name is ",lname)
       
class class3(class1,class2):
    def display3(self):
        rollno=int(input("enter the rollno: "))
        print("Roll no is: ",rollno)

class marks(class2):
    def markscount(self):
        marks=int(input("enter the marks "))
        

obj = class3()
obj2 = marks()
obj.display1()
obj.display2()
obj.display3()
print("your have be assigned ")
print("enter your marks students ")
obj2.display2()
obj2.markscount()
