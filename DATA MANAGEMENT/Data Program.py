import random
def roll_a_die(chooseList):
    die = [1,2,3,4,5,6]
    roll = random.choice(die)
    chooseList.append(roll)
    return chooseList

def pick_a_card():
    cards = [1,2]
    choice = random.choice(cards)
    chooseList.append(choice)

def checkSum(sumOfCombo):
    for x in chooseList:
        sumOfCombo += x
    return sumOfCombo

def addToMain (arrangementsList,sum1,counter,chooseListIndex):
    if sum1 == number and chooseList not in arrangementsList:
        arrangementsList[counter].append(chooseList)
        counter+=1
        print("added to list")
    return arrangementsList


chooseList = []
arrangementsList = []
number = int(input("What sum are you looking for:" ))
sumOfCombo = 0

for x in range (100):
    chooseListIndex = x
    counter = 0
    roll = roll_a_die(chooseList)
    roll2 = roll_a_die(chooseList)
    pick = pick_a_card()
    pick2 = pick_a_card()
    sum1 = checkSum(sumOfCombo)
    print (chooseList)
    final = addToMain(arrangementsList,sum1,counter,chooseListIndex)
    print(sum1)
    print(chooseList)
    chooseList.clear()        
    sumOfCombo = 0    

print(final)

    
