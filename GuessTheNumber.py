import random
print("Guess x(0-10):")
x= random.randint(0,10)
s= ("Loser x={}".format(x), "Winner")[x==input()]
print(s)