import random

def gen():
    rolls=[]
    for i in range(0,4):
       rolls.append(random.randint(1,6))

    rolls.remove(min(rolls))

    return sum(rolls)
