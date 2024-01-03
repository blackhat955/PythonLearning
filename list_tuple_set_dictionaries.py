# how to do operate within list and making changes at the same time

list=["Durgesh","Nibhapur","Om","Kuldeep","Sumit","Rajababu"]

print(list)# this one print a normal list [element here]
#['Durgesh', 'Nibhapur', 'Om', 'Kuldeep', 'Sumit', 'Rajababu']
# add element at desire loaction


list[0]="Jaunpur" # this will add value at the first position

print(list)
#['Jaunpur', 'Nibhapur', 'Om', 'Kuldeep', 'Sumit', 'Rajababu']

# append element in the given list

list.append("Gujrat")
print(list)
#['Jaunpur', 'Nibhapur', 'Om', 'Kuldeep', 'Sumit', 'Rajababu', 'Gujrat']

# Removing elemet by name

list.remove("Gujrat")
print(list)
# before:['Jaunpur', 'Nibhapur', 'Om', 'Kuldeep', 'Sumit', 'Rajababu', 'Gujrat']
# after remove:['Jaunpur', 'Nibhapur', 'Om', 'Kuldeep', 'Sumit', 'Rajababu']

# using pop functio
list.pop()
print(list)
#['Jaunpur', 'Nibhapur', 'Om', 'Kuldeep', 'Sumit']
# pop elemet from back
list1=["college Name ", "Subject you had chosen Before"]
list.insert(0,list1)
print('list become a 2D list by doing such')
print(list)

# run over to 2D list
for i in list[0]:
    print(i)



# tuple-> collection of order of immutable(unchangeble) used to grop together related data

student=("Bro", 21, "male")

print(student.count("Bro"))

print(student.index(21))

for x in student:
    print(x)

for age in student:
    if age != 21:
        continue
    print("Bro age is "+str(age))

# Set in the python
# is collection which is unorder ,unindexed . No duplicate values

val={'Utensil','knife','spoon','knife','knife','knife','knife'}

print('Here we are doing operation on the set elemennts')

print(len(val))

for x in val:
    print(x)

val.add('napkin')

print(val)

print(val.remove("spoon"))
print(val)

print(val.clear())# remove the elemet from the set
print(val)

# update the set
dol={'Utensil','knife','spoon','knife','knife','kitten','dog'}
val.update(dol)

print(val)

# join two set together

dinner_tabale=val.union(dol)

for x in dinner_tabale:
    print(x)

# difference

print(val.difference(dol))

# intersection

print(val.intersection(dol))


# dictionaries work in python
print('We are working on dictionaries over here############################################')
# dictipnaries : a changeable , unorder collection of unique key:value pair fast because they are using hasing keys, allow us to access value quikly and efficiently

capitals={
    'USA':'Washigaton DC',
    'India':'Delhi',
    'Germany':'Berlin',
    'China':'Beijing',
    'Russia':'Moscow',
}

print(capitals['Germany'])

print(capitals.get('Germany'))

print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key,value)


capitals.update({'Afrrica':'Ghana'})

capitals.update({'USA':'Las Vegas'})

print(capitals.items())

capitals.pop('China')
capitals.clear()