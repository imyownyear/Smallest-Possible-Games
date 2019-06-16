import random
print("Guess x(0-10):")
x= str(random.randint(0,10))
s= "Winner" if input() == x else "Loser x={}".format(x)
print(s)