# doing stuff with string
name='BroDurgesh'
print(type(name))

print(name+' '+ 'Durgesh')

# String Method in python and how we can play around

print(len(name))

print(name.find('o')) # this one return the index where the value is actually present

print(name.capitalize())

print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.islower())
print(name.isalpha())
print(name.count('o'))

print(name*3) #this one print the name three time as whole
# type cast of the variable for the pythondata types

a=1
b=2.0
c="3"

print(int(b))
print(str(a))
print(int(c))
d=int(c)
# this type cast help when you want to add number and string at the same time

print(type(d))



# string slicing in python
# you can achieve this using indexing or slice in bulil function
name="Bro Code"
#[starting index:final index: step(how many gap you want in between)]

first_name=name[0:3]
print(first_name)
last_name=name[4:8:2]# Code->Cd this is printing after the two steps
print(last_name)

reverse_string=name[::-1]

print(reverse_string)

website='https://google.com'

# 0,1,2,3,4,5,6
# -1,-2,-3,-4- counting from back

slice=slice(7,-4)

print(website[slice])# print->google