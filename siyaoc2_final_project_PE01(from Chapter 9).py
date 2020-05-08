from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins are the point when serving. Player A always")
    print("has the first serve.")

def getInputs():
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("Best of n games matches? "))
    return a, b, n

def simNGames(n, probA, probB):
    winsA = 0
    winsB = 0
    game = 0
    while winsA <= n/2 and winsB <= n/2:
        game = game + 1
        if game % 2 == 0:
            scoreA, scoreB = simOneGame(probA, probB, "B") # player B serves first in the even games of the matches
        else:
            scoreA, scoreB = simOneGame(probA, probB, "A") # player A serves first in the odd games
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGame(probA, probB, serving):
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
    return a==15 or b==15

def printSummary(winsA, winsB):
    n = winsA + winsB
    print("\nGames simulated:", n)
    print("Wins for A: {0} ({1:0.1%})". format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})". format(winsB, winsB/n))

if __name__ == '__main__':
    main()

