

class People : #parent class
    def __init__(self, eye_color, weight):#init function, parameters
        self.eye=eye_color #attributes
        self.weight=weight

    def describe_self(self):#
        print(f"This person has {self.eye} eyes and weighs {self.weight} kilos.")

class Child (People): #child class
    def __init__ (self, age, eye_color, weight):
        People.__init__(self, eye_color, weight)
        self.age=age

    def tell_age(self): #class method
        print(f"I am {self.age} years old.")

child1=Child(4, "brown", 33)#arguments, instantiation

child1.tell_age()#instance, dot_operator, class method
child1.describe_self()