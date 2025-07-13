class student:
    def data(self,name, age):
        self.name=name
        self.age=age
s1=student()
s1.data('Ram',20)

print(s1.name)
print(s1.age)

#...
class Point:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        return Point(self.x+other.x)
p1=Point(3)
p2=Point(4)
p3= p1+p2
print(p3.x)


#.
class Animal:
    def speak(self):
        print('Animal Sound')

class Dog(Animal):
    def bark(self):
        print('Bark')

d=Dog()
d.speak()
d.bark()

#.

class User:
    def __init__(self,role):
        self.role = role

def create_user(role):
    return User(role)

u=create_user('admin')
print(u.role)