#decorators - wrapping functions  used a lot in libraries and framework

def my_decorators(func):
    def wrap_func(x,y):
        print("*****")
        func(x,y)
        print("*****")
    return wrap_func

@my_decorators
def hello(greeting, emoji):
    print(greeting,emoji)
hello("heloooo",':)')

#error handling:
while True:
    try:
        age = int(input("enter your age:" ))
    except ValueError:
        print("please enter a number")
        break
    except ZeroDivisionError:
        print("enter value greater then zero")
        break
    else:
        print("Thank you")
        break
    finally:
        print("Done") #useful to record logs
        break
    print("Completed") #if there is no break in this loop this line will run
    
#error handeling 2 
# def sum(num1,num2):
#     try:
#         return(num1+num2)
#     except (TypeError,ZeroDivisionError): #we can handle mul errors
#         print(err)

# a = sum(23 + "23")
# print(a)

#generators - allows to generate sequence of value in time ex. range is an generator
#generators doesn't need any disk  space
def make_list(n):
    result = []
    for i in range(n):
        result.append(i*2)
    return result
    
a = make_list(23)
print(a)
#yield function 
def generator_function(n):
    for i in range(n):
        yield i

g = generator_function(55)
next(g)
next(g)
next(g)
print(next(g)) #remembers most recent value

#testing generator's efficiency
# from time import time
# def performance(fn):
#     def wrapper(*args,**kwargs):
#         t1 = time
#         result = fn(*args,**kwargs)
#         t2 = time
#         print(t2-t1)
#         return result
#     return wrapper

# @performance
# def long_time():
#     print("1")
#     for i in range(100000):
#         i*5
# @performance
# def short():
#     print('2')
#     for i in list(range(100000)):
#         i*5

# long_time()
# short()



