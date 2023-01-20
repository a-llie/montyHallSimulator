import random 

#agent always chooses to change 
def change():
    winningDoor, firstChoice  = random.randint(1,3), random.randint(1,3)
    #choose door to reveal 
    showOptions, shownDoor = [1,2,3], 0
    showOptions.remove(firstChoice)
    #if either door is the winningDoor, show the other losing door
    if (showOptions[0] == winningDoor):
        shownDoor = showOptions[1]
        showOptions.remove(showOptions[1])
    elif (showOptions[1] == winningDoor):
        shownDoor = showOptions[0]
        showOptions.remove(showOptions[0])
    #else, pick a door randomly
    else:
        shownDoor = random.choice([showOptions[0], showOptions[1]])
        showOptions.remove(shownDoor)
    #agent changes chosen door
    secondChoice = showOptions[0]
    if (secondChoice == winningDoor):
        return 1
    return 0
    
#this agent always stays 
def stay():
    winningDoor = random.randint(1,3)
    firstChoice = random.randint(1,3)
    if (firstChoice == winningDoor):
        return 1
    return 0

#this agent randomly chooses to stay or change 
def chaos():
    return random.choice([stay(), change()])


def round(wins, total):
    return format((wins/total)* 100,'.2f')

def main(): 
    changeWins, stayWins, chaosWins = 0, 0, 0
    simulations = 500000

    for i in range(simulations):
        changeWins += change()
        stayWins += stay()
        chaosWins += chaos()

    print("Out of " , simulations, " rounds: ")
    print("Change wins: " , changeWins, "/", simulations, ":", round(changeWins, simulations), "%")
    print("Stay wins: " , stayWins, "/", simulations, ":", round(stayWins, simulations), "%")
    print("Chaos wins: " , chaosWins, "/", simulations, ":",round(chaosWins, simulations), "%")

main()