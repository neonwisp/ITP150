"""
sales_taxes_with_functions.py
@Author: ITP 150 Ashlee Raya
Date Created: 7/14/2026
This script calculates different types of tax amounts for a purchase.
It calculates the total taxes and the total sales after taxes. To assist
in learning, this script will be modified to incorporate a function that
calculates the tax amounts for each type of tax and a function to display
a receipt.
"""

def main():
    STATE_RATE = .043
    COUNTY_RATE = .01
    SPECIAL_RATE = .007

    while True:
        print('This program will calculate sales taxes on purchases:')

        purchase_amount = validate_purchase_amount()

        # calculate the taxes and the total tax
        state_tax = calculate_taxes(purchase_amount, STATE_RATE)
        county_tax = calculate_taxes(purchase_amount, COUNTY_RATE)
        special_tax = calculate_taxes(purchase_amount, SPECIAL_RATE)
        total_tax = state_tax + county_tax + special_tax
        total_with_taxes = purchase_amount + total_tax

        # save the variables in a list and pass the list down to the function.
        amounts = [purchase_amount, state_tax, county_tax, special_tax,
                   total_tax, total_with_taxes]
        # call the function to display the results
        display_receipt(amounts)

        run_program = input('Do you want to calculate more taxes (Y/N)?\n')
        if run_program.upper() != 'Y':
            break

    print('Thank you for your business. Please come again!')


def validate_purchase_amount():
    while True:
        try:
            purchase_amount = float(input('Please enter the amount purchased:\n'))
            if purchase_amount < 0:
                raise ValueError
            return purchase_amount
        except ValueError:
            print('Invalid amount. Please enter a non-negative number.')


def calculate_taxes(purchase_amt, tax_rate):
    tax_amount = purchase_amt * tax_rate
    return tax_amount


def display_receipt(amounts):
    print(f'{"Sales Receipt":^40s}')
    print(f'{"Total Before Taxes":20s}{amounts[0]:20.2f}')
    print(f'{"State Tax":20s}{amounts[1]:20.2f}')
    print(f'{"County Tax":20s}{amounts[2]:20.2f}')
    print(f'{"Special Tax":20s}{amounts[3]:20.2f}')
    print(f'{"Total Taxes":20s}{amounts[4]:20.2f}')
    print(f'{"Total After Taxes":20s}{amounts[5]:20.2f}')


if __name__ == '__main__':
    main()