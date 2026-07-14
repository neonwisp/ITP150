"""
cookie_sales.py
Author: ITP 150 Ashlee Raya
Date Created: 7/14/2026
This script calculates the total sales for cookies at a stand. The total sale
for each customer is calculated. The total sale for all customers is
calculated and printed. We are using a sentinel value loop to control the
running of the program where the customer must enter Y to run the program or
N to quit. We use a for loop and Python’s zip() function to display the
types of cookies and their prices to the customer. The types of cookies and
their prices are stored in lists.
"""


buy_cookies = input('Would you like to buy some cookies? (Y/N)?\n')
while buy_cookies.upper() == 'Y':
    print("I am inside the loop.")
   
    buy_cookies = input('Would you like to buy some more cookies (Y/N)?\n')

print('Thanks for your support!')

