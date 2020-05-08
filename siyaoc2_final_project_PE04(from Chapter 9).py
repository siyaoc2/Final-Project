from random import random

def main():
    printIntro()

def printIntro():
    print("Throwing darts can estimate the value of pi ")


n = int(input("What is the number of darts thrown out? "))

hit = 0
for i in range(n):
    x= 2* random()-1
    y = 2* random()-1
    if x ** 2 + y ** 2 <=1:
        hit = hit + 1
def printSummary(hit,n):
    print("The numbers of darts simulated: ", n)
    print("The numbers of darts hit the board: {0} ({1:0.1})". format(hit, hit/n))
    print("The value of pi estimates: ", 4*hit / n)

printSummary(hit,n)

if __name__ == '__main__':
    main()


