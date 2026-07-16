"""
cookie_sales_v2.py
@Author: ITP 150 Ashlee Raya
Date Created: 7/14/2026
This script calculates the total sales for cookies at a stand. The total sale
for each customer is calculated. The total sale for all customers is
calculated and printed. We are using a sentinel value loop to control the
running of the program where the customer must enter Y to run the program or
N to quit. We use a for loop and Python’s zip() function to display the
types of cookies and their prices to the customer. The types of cookies and
their prices are stored in lists.
"""


troop_sales = 0

while True:
    cookies = ['Minty Thins', 'Peanut Butter Bundles', 'Shortcakes']
    prices = [5.00, 6.00, 5.50]
    print('Here are the types of cookies we have for sale and their prices:')
    # using for loop to display the contents of the cookies and prices list
    for index in range(0, len(cookies)):
        print(f'{cookies[index]}, ${prices[index]:.2f}')

    # get the input for the quantity of cookies to purchase
    mt_qty = int(input('How many Minty Thins do you want to buy?\n'))
    pb_qty = int(input('How many Peanut Butter Bundles do you want to buy?\n'))
    sc_qty = int(input('How may Shortcakes do you want to buy?\n'))

    # calculate the sale amount for each cookie
    mt_sale = mt_qty * prices[0]
    pb_sale = pb_qty * prices[1]
    sc_sale = sc_qty * prices[2]

    # calculate the sale amount for the customer
    customer_sale = mt_sale + pb_sale + sc_sale

    # accumulate the total troop sales
    troop_sales = troop_sales + customer_sale  # troop_sales += customer_sale

    print(f'{"Cookie Sales Receipt":^40}')
    print(f'{mt_qty:<5}{cookies[0]:<25s}{mt_sale:>10.2f}')
    print(f'{pb_qty:<5}{cookies[1]:<25s}{pb_sale:>10.2f}')
    print(f'{sc_qty:<5}{cookies[2]:<25s}{sc_sale:>10.2f}')
    print(f'{"Total Customer Sale":30s}{customer_sale:>10.2f}')

    buy_cookies = input('Would you like to buy some more cookies (Y/N)?\n')
    if buy_cookies.upper() != 'Y':
        break

print(f'{"Total Troop Sales":30s}{troop_sales:>10.2f}')
print('Thanks for your support!')

