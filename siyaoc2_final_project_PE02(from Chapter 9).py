from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

def printIntro():
    print("This program simulates a game of volleyball between two")
    print('players called "A" and "B". The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the team wins a rally is awarded a point.")

def getInputs():
    a = float(input("What is the prob. player A wins a rally? "))
    b = float(input("What is the prob. player B wins a rally? "))
    n = int(input("Numbers of games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGame(probA, probB):
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB= scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB
def gameOver(a,b):
    return (a>=25 and a - b >= 2) or (b >= 25 and b-a >= 2)
    # Games are played to a score of 25, and must be won by at least 2 points.
    # a & b represent scores they earned for this game.

def printSummary(winsA, winsB):
    n = winsA + winsB
    print("\nGames simulated:", n)
    print("Wins for A: {0} ({1:0.1%})". format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})". format(winsB, winsB/n))

if __name__ == '__main__':
    main()
