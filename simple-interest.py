# This script calculates simple interest given principal,
# annual rate of interest, and time period in years.
# Do not use this in production. Sample purpose only.
# Author: Upkar Lidder (IBM)
# Additional Authors:
# Pavidu-Dilshan

# Input:
# p, principal amount
# t, time period in years
# r, annual rate of interest

# Output:
# simple interest = p * t * r / 100

def calculate_simple_interest(p, r, t):
    return (p * r * t) / 100

def main():
    try:
        p = float(input("Enter the principal amount: "))
        r = float(input("Enter the rate of interest per year: "))
        t = float(input("Enter the time period in years: "))
        interest = calculate_simple_interest(p, r, t)
        print(f"The simple interest is: {interest}")
    except ValueError:
        print("Please enter valid numeric inputs.")

if __name__ == "__main__":
    main()
