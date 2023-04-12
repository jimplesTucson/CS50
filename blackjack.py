import random
# clear the deck
length = 10
deck = []
for i in range(length):
    test = random.randint(1,length)
    good = True
    for j in range(len(deck)):
        if test == deck[j]:
            good = False
            break
    if good == True:
        deck.append(test)
for i in range(length):
    print ("i is ", i, " deck is ", deck[i])
    