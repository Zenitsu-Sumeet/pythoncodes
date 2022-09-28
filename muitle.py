class Number:
    Multiplier = None
    def __init__(x,y):
        self.x=x
        self.y=yield
    def add(self):
        return self.x+self.y
    @classmethod
    def multiply(cls,a):
        return  a*cls.Multiplier


obj=Number()
print(obj.add(5,10))
print(obj.Multiply(10))
