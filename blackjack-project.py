import random
import time
import sys
import print_quotes
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print("\n\nWelcome to 24/7 Blackjack")

dictionary = {"playerCards": [],
              "computerCards": [],
}

#Functions for when a user decides to either hit or stand, hit draws a card for user until they declare they'd like to stand. Stand draws cards for computer.
def hit(cards, playerCards):
    dictionary["playerCards"].append(random.choice(cards))
def stand(cards, computerCards):
    dictionary["computerCards"].append(random.choice(cards))

#Function that displays users cards. Formatting that text also included inside.
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

#Same function as previous one but for computer. Text formatted aswell.
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
    print(f" [" + (str(sum(dictionary['computerCards'])) + "] "))

#Function that's only triggered if user chose "hit". It only checks if user hit above 21. 
#If so, program prematurely notifies the user that he's lost (this bit is done within main While loop) and ends current bet.
def playerCheck(hitStatus):
    playerCardTotal = 0
    for num in dictionary['playerCards']:
        playerCardTotal += num
        hitStatus = True 
    if playerCardTotal > 21:
        hitStatus = False
    return hitStatus, playerCardTotal

#Same but for computer and without prematurely ending the program.
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

#Function that checks who won. Based on the outcome users balance is dealt with accordingly.
def checkWin(userValue, compValue, newBalance, allocatedBalance):
    isWin = 0
    print("_" * 200 + "\n")    
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
    print(f"\nYour available balance is ${newBalance}\n")
    return newBalance


def clearDict():
    for key in dictionary:
        dictionary[key] = []

isPlaying = True
while isPlaying == True:
    hitStatus = True
    print("\n" + "_" * 200 + "\n")    
    play = input("\n\nWould you like to play?: ('y' for yes, 'n' for no) \n\n\n").lower()
    if play == "y":
        validBet = True
        allocatedBalance = int(input("\n\nPlace your bet: "))
        print("\n" + "_" * 200 + "\n")
        time.sleep(0.25)
        
        #If statement made for every iteration after the first one that's triggered if user bets more than they have.
        if allocatedBalance > newBalance:
            print("\n\nYou don't have enough to cover that bet.")
            validBet = False
            
        #Statement for valid bets, i.e. main code.
        elif newBalance > 0 and validBet == True:
            print("\n\nShuffling cards\n\n")
            
            #Draws two cards for user. (Doesn't display them yet)
            for card in cards * 2:
                card = random.choice(cards)
                print(card, end = " ")
                time.sleep(0.04)
            time.sleep(0.08)
            
            #Clears terminal
            print('\x1b[H\x1b[2J', end='')
            dictionary["playerCards"].append(random.choice(cards))
            dictionary["playerCards"].append(random.choice(cards))
            print(f"\n\nYour cards are {dictionary['playerCards'][-1]} and {dictionary['playerCards'][0]} [{dictionary['playerCards'][-1] + dictionary['playerCards'][0]}] \n")
            
            #If user drew two aces, program prompty splits two aces into a 11 & 1 combination.
            if dictionary['playerCards'][-1] == 11 and dictionary['playerCards'][0] == 11:
                dictionary['playerCards'][-1] = 1
                print(f"\nYou split your cards.\n\nYour cards are now {dictionary['playerCards'][-1]} and {dictionary['playerCards'][0]} [{dictionary['playerCards'][-1] + dictionary['playerCards'][0]}] \n")
            dictionary["computerCards"].append(random.choice(cards))
            print(f"Computer has {dictionary['computerCards'][0]} and \u2588 \n")
            
            #Least necessary while loop. Made only to filter rare case of user drawing perfect 21 hand.
            while hitStatus == True:
                if dictionary['playerCards'][0] + dictionary['playerCards'][1] != 21:  
                     
                    #If statement that asks the user "hit or stand" only if the total of his cards is less than 21.  
                    if playerCheck(hitStatus)[1] < 21:
                        hitOrStand = input("_" * 200 + "\n\nHit or stand?: ").lower()
                    compValue = 0
                    
                    if hitOrStand == "stand" or playerCheck(hitStatus)[1] == 21:
                        userValue = playerCheck(hitStatus)[1]
                        compValue = 0
                        compCardTotal, compHitStatus = compCheck(compHitStatus)
                        
                        #If computer has cards total greater than 16 he stops hitting. As done in real casinos.
                        if compCheck(compHitStatus)[0] > 16:
                            compValue = compCardTotal
                            showUserCards(countIteration)
                            showCompCards(countIteration)
                            compCheck(compHitStatus)
                            hitStatus = False
                        
                        #Else it keeps hitting until it's greater than 16.
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
                        
                        #Slightly confusing but hitStatus false means user has total greater than 21, stopping execution of this part of program.
                        if statusCheck == False and userValue != 21:
                            userValue = playerCheck(hitStatus)[1]
                            hitStatus = False
                            
                        #Same as above but for 21.
                        if statusCheck == False and userValue == 21:
                            hitOrStand = "stand"
                            break
                        
                #Part for a scenario where user drew perfect 21. Goes straight to computer drawing cards.
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
        
        #Final part, statement that checks who's won and changes users balance according to the outcome.
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
    
    if newBalance == 0:
        print("\n\n" + random.choice(print_quotes.depressingExitQuotes) + "\n\n")
        print("_" * 200 + "\n\n")
        sys.exit()
                
    #In case user likes to stop playing, our counter staff informs the user about the rest of his balance along with some inspirational quotes. 
    #Try it!
    if play == "n":
        print("\n" + "_" * 200 + "\n")    
        print(f"\n\nHere's your cashout. Your remaining balance is ${newBalance}. ", end = "")
        print(random.choice(print_quotes.exitQuotes) + "\n\n\n" + "_" * 200 + "\n\n\n")
        sys.exit()
