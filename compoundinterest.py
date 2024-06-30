import sys

def main():
    initial = int(sys.argv[1])
    interest = float(sys.argv[2])/100 # Entered as if it were a percentage (e.g. 4.4 for 4.4%)
    years = int(sys.argv[3])

    if (len(sys.argv) == 5):
        amountAddedPerYear = int(sys.argv[4])

    total = initial
    # print (initial)
    # print (interest)
    # print (years)
    for i in range(years):
        earnedInterest = total * interest
        total += earnedInterest
        if 'amountAddedPerYear' in locals():
            total += amountAddedPerYear
        print("Earned interest for year " + str(i + 1) + ": $" + f'{round(earnedInterest, 2):,}')
        
    print("Total ending amount: $" + f'{round(total, 2):,}')

main()