# class and inheritance
from turtle import update


class Durgesh:
    __village = 'Nibhapur'  # this one is local varibale to the class
    print(type(__village))
    __update = "Durges"
    # we are creating intructor for the python class

    def __init__(self, name, home, college, place,x, history):
        self.name = name
        self.home = home
        self.college = college
        self.place = place
        self.x=x
        self.history=history


    def __creating_new_person(self):
        print(f"will be a new {self.name} person{self.place}")

    def you_should(self):
        print(f"go college {self.college} at {self.place} to make fun")
    def print_list(self):
        for i in self.x:
            print(i)
    def print_history(self):
        for key,val in self.history.items(): # you just forget to add items() over here and because of this this one shows you too many value to unpack
            print(self.history[key])
            print(val)



# make object to access the class you have define above

person =Durgesh("durgesh", "Thakur Complex,Mumbai", "Thakur College of Engineering and technology", "Mumbai", [1,2,3,4,5,5,6,6,7,7,66],{'Name':'Durgesh','Place':'Mumbai'})

person._Durgesh__creating_new_person()
# this is how we  can access the private variable outside of thd class
# there is no concept for any private variable in python you can access the private varibale using object._classNmae__fuctionName

person.you_should()
print(person._Durgesh__update) # this is how we can access the private variable for the class we have define in the given class

person.village="Kanyakumari"

print(person.village)

person.print_list()

person.print_history()




# Inheritance we have parents child relation in which the lowe class can access all the method have in prents class

class Anil:
    village="Nibhapur"
    def working(self):
        print('Just going for the regular job')
    def sleepping(self):
        print('slipping inn Night and can be do many things')

class Durgesh(Anil):
    pass
class om(Anil):
    pass
class kuldeep(Anil):
    pass
durgesh=Durgesh()
om=om()
kuldeep=kuldeep()

print("this is printing name from the parent class"+' '+durgesh.village)
# As you seen the child class can access the caaribale for the main class and can do many stuff as you want


# how we can implement multilevel inheritance applied using python method


print('Checking for multilevel inheritance####################################')
class welcome:
    festival='Diwali'

    def make_thing_possible(self):
        print('this is happen all this time since very start')
        return "Durgesh"

    def can_do_it(self):
        print(" can be do the stuff and welcome to the must be part of what happen with you ")
        return "Come so soon"

class coming(welcome):
    we=welcome()
    def come_to_end(self): # we need self to access anything inside the fuction
        print(f'this come to so soon {self.we.make_thing_possible()}')
        return " Welcome Back"
class multi_inheritance(coming):
    co=coming()
    we=welcome()
    def come(self):
        print(f'this is form chil class{self.co.come_to_end()}')
        print(f'Can be come from a parent class welcome {self.we.make_thing_possible()}')

go=multi_inheritance()

go.come()


print("Print how to use super class in python ###################################")
#  SuperFuction:Access use to give access to the method of a parent class.
# return a temporary object of a parent class when used

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
class Square(Rectangle):
    def __init__(self,length, width):
        super().__init__(self, length, width)
    def area(self):
        return self.length*self.width
    #     self.length=length
    #     self.width=width
    # now we can access method of the parent class using super method

# class Cube(Rectangle):
#
#     def __init__(self, length, width, height):
#          super().__init__(length, width)
#          self.height=height
#     def volume(self):
#         return self.length * self.width * self.height
#
#
# square=Square(3,4)
# cube=Cube(4,5,6)

# print(square.area())
# print(cube.volume())




print("abtract class work in pyhton###############################")

# prevent use to creating a object of the class
# compiles a user to override abstract clss method in a child class

# abstract class= a class which contain one or more abstract mehtods
# abstract method= a method that has a declaration but does not have a implementation

from abc import ABC, abstractmethod
class vehicale(ABC):
    # this way we can prevent this clss to user, so they can't creat objet for this class
    @abstractmethod
    def go(self):
        pass
class Car(vehicale):
    def go(self):
        print("You are driving a car")
class Motercycle(vehicale):
    def go(self):
# also this is nervertheless imperative that you have impliment go class here without go method it shold throw err because of
# go method present in abtract class and y]you have to implement that one
        print("You ride the mootercycle")
car=Car()
moter=Motercycle()

#veh=vehicale() we can't do this anymore since this is a abatract class
car.go()
moter.go()

# Creating a class and a seprate fuction and see how thing can be done

class Car:
    color=None

class MoterCyle:
    color=None

def GiveColor(vehicale,color):
    print(f"Name of vehicale {vehicale}, and the assign color {color}")

car_1=Car()
car_2=Car()
car_3=Car()

GiveColor(car_1,"red")
GiveColor(car_2,"green")
GiveColor(car_3,"Blue")



# Duck typing in pyhton

# Duck typing: concept where class of the object is less important  than the method / attribute
# class type is not checked if minimum methods /attributes are present
# if it walks like a duck, and quake like a duck, then it must be a duck


class Duck:
    def walk(self):
        print('duck is walking like a dog')
    def talk(self):
        print("The duck is quacking")
class Chicken:
    def walk(self):
        print("Chiken is walking ")
    def talk(self):
        print("The chicken is clucking")

class Person():
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("you caught the credit")

duck=Duck()
chicken=Chicken()
person=Person()

person.catch(duck)

person.catch(chicken)



print("Walrus Operator :=  also known as an assigment operator######################")

happy=True

# yiu can't do this in python without a walrus operator
# like I give you down below


# this one show you the errror and you can't print it out without walrus operator
#print(happy=True)

# The above print statement can be print only if using a walrus operator
print(happy:=True)

# This is only work width version 3.8 or above in python


# foods=list()
#
# print( "This is doing without walrus operator #################")
# while True:
#     food=input("Enter the food you like?")
#     if food =="quit":
#         break
#     foods.append(food)
#
#
# print("Doing same using walrus operator")
#
# foods=list()
#
# while food:=input("Enter the food you like?")!="quit":
#     foods.append(food)




# Assigen a fuction to a variable

def hello():
    print("this is me for most welcome to the furhter come so the bid for all")

print ("This one is memory address of the fuction",hello)

hi=hello

hi()

# You can also use print function like this
say=print

say("this is me doing this since very long")



# Higher Order fuction in pyhton

print(" A higher order function is a fuction which tak a fuction as argument or return a function###################")

 # this is example how the higher order function work
def loud(val):
   return val.upper()

def quit(val):
    return val.lower()

def hello(func,val):
    text=func(val)
    print(text)
hello(quit,"Durgesh")


# another example
def divisor(val):
    def dividend(y):
        return val/y
    return dividend
# The above fuction work like first x hold the value which we are passing and then
# it return dividend as fuction and assign to value dividea and then we pass value for dividen
# with the help of divide and call dividend again and this way it work.


divide=divisor(3)
print(divide(10))



print(" How to use lambda fucntion in pyhton###############################")

def double(val):
    return val*2

print(double(4))

# this can be also done using other way like using lambda fucntion

# functionName=lambda val # here we can write multiple parameters: val*2

doubleValue=lambda val:val*2

print(doubleValue(19))


print('Different to use sort fuction and how they are uesful at all')
# sorting of the fuction using inbuilt pyhthon method

#sort() method= use with list only
# sort fuction= use with iterable

students=["Raju","singal","Manoj","Parik","sanjit"]

# want to sort these functions
#new=students.sort() you can assign a variable to the fuction for the sort which is use for diaplacy the function
students.sort(reverse=True) # this is sort the using descending order
for i in students:
    print(i)
 # how we can sort the value using key for any given list


# for other iterable like tuple and dictionaries


students_names=("Raju","singal","Manoj","Parik","sanjit")

tuple_sorted=sorted(students_names)
print("this is printing value after sorted them form tuple list")
for i in tuple_sorted:
    print(i)

print("this is printing name which is sorted by name in alphabetical order")
name=[("kumar"," A",34),
      ("HUrj"," B",23),("Tyuud"," C",23),("Spensor"," A",23),("Tylor"," B",26)]

#name.sort()
# now we can use key to sort them out

kay_sort=lambda age:age[2]

# same thing we can do with if the given is not list rather a tuple

name.sort(key=kay_sort,reverse=True)
for i in name:
    print(i)


print("How to use map fuction in the python #########################")


# map()= applies a function to each item in a iterable (lis, tuple, etc;)

# map(function, iterable)

store=[
    ("shirt",20.00),
    ("pant", 10.00),
    ("jacket", 16.00),
    ("jeans", 4.00),
    ("cap", 3.00),
]

to_euro=lambda data:(data[0],data[1]*1.2)

to_euro_price=map(to_euro,store)

print(type(to_euro_price))

for i in to_euro_price:
    print(i)



# filter fuction
print("Here we are goin to learn how to use filter function")

# filter(function, iterable)

store=[
    ("shirt",20.00),
    ("pant", 10.00),
    ("jacket", 16.00),
    ("jeans", 4.00),
    ("cap", 3.00),
]

# find items whose price is greater than 18

price=lambda data:data[1]>=18

item_prices=filter(price,store)

for i in item_prices:
    print(i)


# how to use reduce fuction in python

print("how to use reduce fuction in python ######################")

# reduce function is a fucntion to an itreable to reduce it to a single cumulative value.
# reduce(function, iterable)

word=["He","ll","o"]

import functools

cumulated_words=functools.reduce(lambda x,y:x+y,word)

print(cumulated_words)




