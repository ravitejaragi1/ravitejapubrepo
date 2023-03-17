class Dog:
    def __init__(self , name):
        print(name)
        self.name=name

    def get_name(self):
        return self.name 
    @classmethod
    def get_age(cls,amount):


d = Dog()
print(type(d))

d.get_age

