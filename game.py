import random as r
top=int(input("Choose the upper limit to guess number: "))
if top<=0: 
    print("Please choose a number greater than 0")
    quit()
ans=r.randint(0, top)
count=1
choose= int(input("Guess the number computer chose. "))
while ans != choose:
    count+=1
    if ans> choose:
        choose=int(input("Wrong number. Guess higher: "))
    else:
        choose=int(input("Wrong number. Guess lower: "))
print("Correct number is", choose, "that you guessed in", count, "chances.")