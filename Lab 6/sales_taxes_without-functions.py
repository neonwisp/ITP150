"""
sales_taxes_without_functions.py
@author: ITP 150 Student. Put your name here.
Date Created: Put current date here.
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
 
         purchase_amount = float(input('Please enter the amount purchased:\n'))

         # calculate the taxes and the total tax
         state_tax = purchase_amount * STATE_RATE
         county_tax = purchase_amount * COUNTY_RATE
         special_tax = purchase_amount * SPECIAL_RATE
         total_tax = state_tax + county_tax + special_tax
         total_with_taxes = purchase_amount + total_tax

         # display the results
         print(f'{"Sales Receipt":^40s}')
         print(f'{"Total Before Taxes":20s}{purchase_amount:20.2f}')
         print(f'{"State Tax":20s}{state_tax:20.2f}')
         print(f'{"County Tax":20s}{county_tax:20.2f}')
         print(f'{"Special Tax":20s}{special_tax:20.2f}')
         print(f'{"Total Taxes":20s}{total_tax:20.2f}')
         print(f'{"Total After Taxes":20s}{total_with_taxes:20.2f}')

         run_program = input('Do you want to calculate more taxes (Y/N)?\n')
         if run_program.upper() != 'Y':
             break


     print('Thank you for your business. Please come again!')
 
if __name__ == '__main__':
     main()
