import random


print("-------------WELCOME TO 21!----------------")
print("\n")
 
deck = [1,2,3,4,5,6,7,8,9,10,11]

playerHand = []
cpuHand = []

def dealCard(hand):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)
    
def cpuChoice():
    choice = "Hit"
    curScore = calcScore(cpuHand)
    if(len(cpuHand)<= 2):
        return choice
    rand = random.randint(0, 1)
    if(rand ==1) or (curScore >= 21):
        choice = "Stay"
    
    return choice

def printCpuDeck():
    print("CPU's Hand: X,", end =" ")
    for x in range(1, len(cpuHand)):
        print(cpuHand[x], end =", ")
    print("\n")

def cpuTurn(choice):
    if(choice == "Hit"):
        dealCard(cpuHand)
        print("CPU has hit!")
        printCpuDeck()
    if(choice == "Stay"):
        print("Cpu has stayed!")
        printCpuDeck()

def calcScore(hand):
    score = 0
    for i in range(0, len(hand)):
        score += hand[i]
    return score

def printWinner():
    cpuScore = calcScore(cpuHand)
    playerScore = calcScore(playerHand)

    cpuFinal = 21 - cpuScore
    playerFinal = 21 - playerScore

    winner = ""

    if(cpuFinal < 0 or playerFinal < 0):
        if(cpuFinal < 0) & (playerFinal >= 0):
            winner = "Player"
        if(playerFinal < 0) & (cpuFinal >= 0):
            winner = "CPU"
        else:
            if(cpuFinal > playerFinal):
                winner = "CPU"
            else:
                winner = "Player"
    else:
        if(cpuFinal < playerFinal):
            winner = "CPU"
        else:
            winner = "Player"

    
    if(winner == "CPU"):
        print("_____________The CPU has won this round!_____________")
        print("Your Score:", playerScore, "/21")
        print("CPU Score:", cpuScore, "/21")
        
    if(winner == "Player"):
        print("_____________You have won this round!_____________")
        print("Your Score:", playerScore, "/21")
        print("CPU Score:", cpuScore, "/21")
        
    

def runGame():
    dealCard(playerHand)
    dealCard(cpuHand)
    printCpuDeck()
    cpuDec = "Hit"
    stay = False
    while(len(deck) != 0):
        if(cpuDec != "Stay"):
            cpuDec = cpuChoice()
        cpuTurn(cpuDec)

        print("Your Hand:", end =" ")
        print(playerHand)
        if(not stay):
            dec = input("Hit or Stay? ")
        
        if(dec == "Hit"):
            dealCard(playerHand)
            print("Your Hand:", end =" ")
            print(playerHand)
            print("\n")
        if(dec == "Stay"):
            stay = True
        if(dec == "Stay")& (cpuDec == "Stay"):
            break

    printWinner()
        

runGame()







