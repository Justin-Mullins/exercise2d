'''

Exercise 2d

Write a function that takes a list of Python objects. Sum the objects that either
are integers or can be turned into integers, ignoring the others.

'''

def sum(*objects):
    sum = 0
    for object in objects:
        if (isinstance(object, str)):
            if (object.isnumeric()):
                sum += int(object)
        if (isinstance(object, int)):
            sum += object
    return sum

print(sum(*['1', 'this', 7, '101',  1]))
print(sum(*('today', 5, '0', 'car', '4', '19')))