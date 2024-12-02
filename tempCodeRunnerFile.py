import random
import time
from matplotlib._type1font import _BalancedExpression

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print("Welcome to 24/7 Blackjack")

dictionary = {"playerCards": [],
              "computerCards": [],
}

def hit(cards, playerCards):
    dictionary["playerCards"].append(random.choice(cards))

def stand(cards, computerCards):
    dictionary["computerCards"].append(random.choice(cards))
    
countIteration = 0

def showUserCards(countIteration):
    print("\nYour cards are ", end = "")
    for each in dictionary['playerCards']:
        print(each, end = "")
        if countIteration == len(dictionary['playerCards']) - 2:
            print(" and ", end = "")
            countIteration += 1
        if countIteration < len(dictionary['playerCards']) - 2:
            print(", ", end = "")
            countIteration += 1
    print(f" [" + (str(sum(dictionary['playerCards']))) + "]\n")

def showCompCards(countIteration):
    print("\nComputer has ", end = "")
    for each in dictionary['computerCards']:
        print(each, end = "")
        if countIteration == len(dictionary['computerCards']) - 2:
            print(" and ", end = "")
            countIteration += 1
        if countIteration < len(dictionary['computerCards']) - 2:
            print(", ", end = "")
            countIteration += 1
    print(f" [" + (str(sum(dictionary['computerCards']))) + "]\n" + "_" * 100 + "\n")
    
def playerCheck(hitStatus):
    playerCardTotal = 0
    for num in dictionary['playerCards']:
        playerCardTotal += num
        hitStatus = True 
    if playerCardTotal > 21:
        hitStatus = False
    return hitStatus, playerCardTotal
        
compHitStatus = True

def compCheck(compHitStatus):
    compHitStatus = True
    compCardTotal = 0
    for num in dictionary['computerCards']:
        compCardTotal += num
    if compCardTotal > 21:
        compHitStatus = False
    if compCardTotal == 21:
        compHitStatus = False
    if compCardTotal < 21:
        compHitStatus = True
    return compCardTotal, compHitStatus

balance = int(input("\n\nHow much would you like to buy in for? (Use numbers): \n\n\n"))
newBalance = balance

def checkWin(userValue, compValue, newBalance, allocatedBalance):
    isWin = 0
    
    if userValue < 21 and userValue > compValue:
        print("\nWin!\n")
        isWin = 0
    elif userValue == 21 and userValue > compValue:
        print("\nBlackjack!\n")
        isWin = 0
    elif userValue == 21 and userValue < compValue:
        print("\nBlackjack!\n")
        isWin = 0
    elif userValue == 21 and userValue == compValue:
        isWin = 1
        print("\nPush!\n")
    elif userValue < 21 and userValue < compValue and compValue < 21:
        isWin = 2
        print("\nDealer wins!\n")
    elif userValue < 21 and userValue < compValue and compValue > 21:
        isWin = 0
        print("\nWin!\n")
    elif userValue < 21 and userValue == compValue:
        isWin = 1
        print("\nPush!\n")
    elif userValue > 21 and userValue > compValue:
        isWin = 2
        print("\nDealer wins!\n")
    elif compValue > 21 and userValue < compValue:
        isWin = 0
        print("\nWin!\n")
    elif compValue == 21 and userValue < compValue:
        isWin = 2
        print("\nDealer wins!\n")
    elif compValue < 21 and userValue < compValue:
        isWin = 2
        print("\nDealer wins!\n")
    if isWin == 0:
        newBalance += allocatedBalance
    elif isWin == 1:
        newBalance = newBalance
    elif isWin == 2:
        newBalance -= allocatedBalance
    print(f"\n\nYour available balance is ${newBalance}\n\n")
    print("_" * 100 + "\n")
    return newBalance


def clearDict():
    for key in dictionary:
        dictionary[key] = []

isPlaying = True
while isPlaying == True:
    hitStatus = True
    play = input("\n\nWould you like to play?: ('y' for yes, 'n' for no) \n\n\n").lower()
    if play == "y":
        validBet = True
        allocatedBalance = int(input("\n\nPlace your bet: "))
        time.sleep(0.25)
        if allocatedBalance > newBalance:
            print("\n\nYou don't have enough to cover that bet.")
            validBet = False
        elif newBalance >= 0 and validBet == True:
            print("\n\nShuffling cards\n\n")
            for card in cards * 2:
                card = random.choice(cards)
                print(card, end = " ")
                time.sleep(0.04)
            time.sleep(0.08)
            print('\x1b[H\x1b[2J', end='')
            dictionary["playerCards"].append(random.choice(cards))
            dictionary["playerCards"].append(random.choice(cards))
            print(f"\n\nYour cards are {dictionary['playerCards'][-1]} and {dictionary['playerCards'][0]} [{dictionary['playerCards'][-1] + dictionary['playerCards'][0]}] \n")
            if dictionary['playerCards'][-1] == 11 and dictionary['playerCards'][0] == 11:
                dictionary['playerCards'][-1] = 1
                print(f"\nYou split your cards.\n\nYour cards are now {dictionary['playerCards'][-1]} and {dictionary['playerCards'][0]} [{dictionary['playerCards'][-1] + dictionary['playerCards'][0]}] \n")
            dictionary["computerCards"].append(random.choice(cards))
            print(f"Computer has {dictionary['computerCards'][0]} and \u2588 \n")
            while hitStatus == True:
                if dictionary['playerCards'][0] + dictionary['playerCards'][1] != 21:     
                    if playerCheck(hitStatus)[1] < 21:
                        hitOrStand = input("_" * 100 + "\n\nHit or stand?: ").lower()
                    compValue = 0
                    if hitOrStand == "stand" or playerCheck(hitStatus)[1] == 21:
                        userValue = playerCheck(hitStatus)[1]
                        compValue = 0
                        compCardTotal, compHitStatus = compCheck(compHitStatus)
                        if compCheck(compHitStatus)[0] > 16:
                            compValue = compCardTotal
                            showUserCards(countIteration)
                            showCompCards(countIteration)
                            compCheck(compHitStatus)
                            hitStatus = False
                            
                        while compCardTotal < 17:
                            showUserCards(countIteration)
                            stand(cards, dictionary["computerCards"])
                            showCompCards(countIteration)
                            compCardTotal, compHitStatus = compCheck(compHitStatus)
                            compValue = compCardTotal
                        hitStatus = False
                        break
                    if hitOrStand == "hit":
                        hit(cards, dictionary["playerCards"])
                        showUserCards(countIteration)
                        statusCheck = playerCheck(hitStatus)[0]
                        userValue = playerCheck(hitStatus)[1]
                        if statusCheck == False and userValue != 21:
                            userValue = playerCheck(hitStatus)[1]
                            hitStatus = False
                        if statusCheck == False and userValue == 21:
                            hitOrStand = "stand"
                            break
                else:
                    userValue = playerCheck(hitStatus)[1]
                    compValue = 0
                    compCardTotal, compHitStatus = compCheck(compHitStatus)
                    if compCheck(compHitStatus)[0] > 16:
                        compValue = compCardTotal
                        compCheck(compHitStatus)
                        hitStatus = False
                            
                    while compCardTotal < 16:
                        stand(cards, dictionary["computerCards"])
                        compCardTotal, compHitStatus = compCheck(compHitStatus)
                        compValue = compCardTotal
                        showUserCards(countIteration)
                        showCompCards(countIteration)
                    hitStatus = False
        if validBet == True:
            if userValue < 22:
                newBalance = checkWin(userValue, compValue, newBalance, allocatedBalance)
                clearDict()
            elif userValue == 21:
                newBalance = checkWin(userValue, compValue, newBalance, allocatedBalance)
                clearDict()
            elif userValue > 21:
                newBalance = checkWin(userValue, compValue, newBalance, allocatedBalance)
                clearDict()