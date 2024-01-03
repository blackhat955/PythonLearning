# list comprehension= a way to create new pythin list with less sentax
# can mimic certain lambda fuction, easier to read
# list=[expression for item in iterable if conditional] # this is way to written somthing using list comprehension
# list=[expression if/else for item in iterable]
# this is without a list comprehension
print( " How we can use list comprehension to write a list in one line more efficient way")
square=[]
for i in range(1,11):
    square.append(i*i)

print(square)

# Now I am using a list comprehension for the same

square_using_list_comprehension=[i*i for i in range(1,11)]

print(square_using_list_comprehension)

student=[1,3,4,67,3,44,5,6,666,755,665,4]

passing_students=list(filter(lambda data: data>60 ,student))

for i in passing_students:
    print(i)

passed_student=[i for i in student if i>60]

for i in passed_student:
    print(i)

# using conditional upfront before start properly
print("printing using conditional at first hand")

pass_stud=[i if i>60 else "Failed"  for i in student]

for i in pass_stud:
    print(i)


# dictionaries comprehension : way to create dictionaries using expression

# dictionaries={key:expression for(key,value) in interable}
# dictionaries={key:expression for(key,value) in interable if conditional}
# dictionaries={key:if/else for(key,value) in interable }
# dictionaries={key:fucntion(value) for(key,value) in interable }
wather={"new york":"sunny","boston":"cold","ohio":"dry","cincinati":"sunny"}

dict={key: value for(key,value) in wather.items() if value=="sunny" }

print(dict)

# using if and else

cities={"newYork":32,"boston":24,"Los Anglis":100,"Chicago":50}

dict_ifelse={key:("Warm" if value>=32 else"Nothing") for (key,value) in cities.items()}

print("Printing if else result values",dict_ifelse)


# we can also achieve same result by doing such
def checkTemp(val):
    if  val>40:
        return "It's Hot"
    elif 50>=val<=100:
        return " Warm"
    else:
        return "cold"

dict_weather={key:checkTemp(value) for (key, value) in cities.items()}

print(" This is printing result where value come from a diction fuction return values",dict_weather)

print(" Printing the value from zip fuction and we can use that ##############################")

# zip(*iterable) = aggregate element from two or more iterable (list, tuple, sets, etc.)
# create a zip object with the paired element stored in tuple of each element

username = ["Durgesh", "tiwari", "usa"]
password = ("p@words", "abc@123", "guest")

users = zip(username, password)
# You can convert zip to a dictionary or any other data structure you want

# print(dict(users))
print(type(users))

for i in users:
    print(i)



# for key, value in .items():
#     print(key+":"+value)

print("Mutithreding in python #############################")
print("threading concept to use how to make run a fuction on a certain gap of time")

# thread= a flow of execution like sepratre order of instruction
# However each thread take a turn running to achieve concurrency
# GIL= Global interpreter lock
# allow only one thread to hold control of the python interpreter

# cpu bound=program or task spend most's of it's time waiting for iternal event (CPU intensive)
# use multiprocessing

# io bound= program or task spend most of time waiting for external event (user input, web scraping )
# use multithreading
import threading
import time

def eat_breakfat():
    time.sleep(3)
    print("You finish eating breakfast")
def drink_coffe():
    time.sleep(4)
    print("You done with drinking coffe")
def study():
    time.sleep(2)
    print("You done with studing")

eat_breakfat()
drink_coffe()
study()


print("How we can use demon thread in python and how they are useful######################################")
# demon Thread run basically background, your program shouldn't need to wait to complete
# that thread this is somthing responsible for garage collection, waiting for input, long running process

