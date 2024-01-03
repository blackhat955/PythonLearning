# *args=parameter that will pack all argument into tuple
# useful so that a function can accept a varying amout of argument

#*kwargs= parameter that will pack all argi=uments into a dictionaries
# useful so that a function can accept a varying amount of keyword and arguments
def sum_num(*args):
    print(type(args))# this is type of tuple
    sum=0
    for i in args:
        sum+=i
    return sum
print(sum_num(1,3,4,5,6,7,7,4,5,6,45,49))



def hello(first, last ):
    print(first,last)
# but this one will stop working if you put a middle name right here
# because in your hello fuction there is no place for the middle name
# and because of this we need this *kwargs which prevent from the such kind of accident
#hello('durgesh','tiwari',middle:'rup')
hello('durgesh','tiwari')


# to make such process error less we can do these things

def new_hello(**kwargs):
    print('Hello'+kwargs['first']+''+kwargs['last'])
    for key, value in kwargs.items():
        print(value)

new_hello(first='durgesh',last='tiwari',middle='rup')
# here you can see this is still workig even though there is
# no positional argument for the middle name in the function


