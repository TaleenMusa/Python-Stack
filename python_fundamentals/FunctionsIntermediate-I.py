import random


def randInt(min=0, max=100):
    num = int(min + random.random()*(max-min))
    return num


print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))
