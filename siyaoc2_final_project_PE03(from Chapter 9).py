from random import randrange

def main():
    printIntro()
    n = numbers_of_games()
    wins = simNGames(n)
    printresult(n, wins)

def printIntro():
    print("This program is to simulate multiple games of craps")
    print("and estimate the probability that the player wins, the rules are")
    print("if the initial roll is 2, 3, or 12, the player loses")
    print("If the roll is 7 or 11, the player wins, and rolling a 7 first is a loss")
    print("If the player rolls the initial value again before rolled a 7 is a win.")

def numbers_of_games():
    n = eval(input("How many games to simulate? "))
    return n

def simNGames(n):
    wins = 0
    roll_the_dice_1 = randrange(1,7) + randrange (1,7)
    if roll_the_dice_1 == 2 or roll_the_dice_1 == 3 or roll_the_dice_1 == 12:
        wins = 0
    elif roll_the_dice_1 == 7 or roll_the_dice_1 == 11:
        wins = wins + 1
    else:
        for_point = 0
        while for_point != 7 and for_point != roll_the_dice_1:
            for_point = randrange(1,7) + randrange(1,7)

            if for_point == roll_the_dice_1:
                    wins = wins + 1
            else:
                for_point == 7
                wins = wins
            return for_point
    return wins


def printresult(n,wins):
    print(n, 'games simulated in total,', wins, 'games win, and the win rate is:'+ str(100*(wins/n)) +'%')

if __name__ == '__main__':
    main()
