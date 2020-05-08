import math
def main():
    n = int(input("Enter a positive whole number greater than 1: "))

    prime_num = True
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            prime_num = False
            break

    if prime_num:
        print(n, "is a prime number! ")

    else:
        print(n, "is not a prime number! ")
main()


