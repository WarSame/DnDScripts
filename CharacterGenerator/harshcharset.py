import random

def gen():
    rolls=[]
    for i in range(0,3):
       rolls.append(random.randint(1,6))

    return sum(rolls)
