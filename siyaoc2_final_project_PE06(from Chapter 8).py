initial = 1

interest_rate = float(input('Enter the interest rate: '))

final_amount = initial

years = 0

while final_amount < 2 * initial:
    years += 1
    interest = final_amount * interest_rate / 100
    final_amount = final_amount + interest


print('When an interest rate of {:.2f}, your initial investment of ${:.2f} will be double ${:.2f} in {} years'.format(interest_rate, initial, final_amount, years))
