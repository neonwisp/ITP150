"""
functions_lab.py
@Author: ITP 150 Ashlee Raya
Date Created: 7/14/2026
This script covers functions with positional arguments, keyword arguments,
default parameters, arbitrary arguments *args, argument tuple packing and
unpacking, and **kwargs
"""

from datetime import datetime # datetime is a Python built-in module/library


def heading():
    """
    The heading function takes no arguments, and it calls the now() method
    from Python's datetime library to print the current date and time from
    the underlying operating system.
    """
    print('Sales Receipt', datetime.now())


def purchase_item(qty, description, price):
    """ This function calculates the total for a purchase and prints it.

    Args:
        qty (int): quantity purchased
        description (string): item purchased
        price (float): item price
    """
    item_total = qty * price
    print(qty, description, '@', price, '=', item_total)



def purchase_total(qty, price):
    """ This function calculates the total for a purchase and returns it.

    Args:
        qty (int): quantity purchased
        price (float): item price
    Returns:(float): item_total
    """
    item_total = qty * price
    return item_total


def purchase_item_defaults(qty=1, description='Tea', price=3.50):
    """This function calculates the total for a purchase and prints it.

    Args:
        qty (int, optional): item qty. Defaults to 1.
        description (str, optional): item description. Defaults to 'Tea'.
        price (float, optional): item price. Defaults to 3.50.
    """
    item_total = qty * price
    print(qty, description, '@', price, '=', item_total)

 
def average_price(*args):
    """
    Uses arbitrary arguments which are placed into a tuple
    """
    sum_price = 0
    print(args) # shows the arguments in a tuple
    print(type(args)) # shows arguments are a type of tuple to be unpacked
    for a in args: # now we are iterating over the tuple with a loop    
        sum_price = sum_price + a # sum_price += a
    average_price = sum_price / len(args)
    print(f'Average price is $ {average_price:.2f}')


def purchase_item_kwargs(**purchase_details):
    """ This function calculates the total for a purchase, prints details.

    Args:
    purchase_details: an arbitrary number of purchase arguments to unpack
    the keywords specified in the function call must be used to
    to access the value. The parameters are stored in a dictionary.
    """
    print(type(purchase_details))
    item_total = purchase_details['qty'] * purchase_details['price']
    print(purchase_details['qty'], purchase_details['description'], '@',
        purchase_details['price'], '=', item_total)


def main():

    print('Task 1. Call the heading() function.')
    heading()

print('\nTask 2. Call the purchase_item() function.')
purchase_item(2, 'Tea', 4.00)

print('\nTask 3. Print a call the purchase_item() function which forces a')
print('return. Functions without a return statement always return None.')
print('Functions with an empty return statement always return None.')
print(purchase_item(2, 'Tea', 4.00)) # Notice it returns a value of None

print('\nTask 4. See the documentation for the purchase_item() function.')
# help(purchase_item) # comment out after running the first time.

print('\nTask 5. Call the purchase_total() function.')
ttl = purchase_total(2, 4.00)
print(f'Total Purchase $ {ttl:.2f}')

print('\nTask 6. Cause an error. Call purchase_item() function with')
('arguments in the wrong order.')
# purchase_item('Tea', 2, 4.00) # Comment out after testing.

print('\nTask 7. Call the purchase_item() function using keyword arguments.')
print('The keywords must match the argument names, but you can put them in')
print('any order.')
purchase_item(description='Tea', qty=2, price=4.00)

print('\nTask 8. Cause a SyntaxError. Call purchase_item() function ')
print('using a mix of positional then keyword then positional arguments.')
# purchase_item(2, description='Tea', 4.00) # Comment out after testing.

print('\nTask 9. Call purchase_item() function using a mix of positional')
print('then keyword arguments. You can mix positional and keyword')
print('arguments but keyword arguments must follow positional arguments.')
purchase_item(2, description='Tea', price=4.00)

print('\nTask 10. Use default parameters when you need to set a default')
print('value for one or more parameters which allows you the option of')
print('calling the function without arguments when default parameters are')
print('set. The defaults will be used. You can also specify argument')
print('values when the defaults are not what you need but be careful.')
purchase_item_defaults() # This will use the defaults of 1 Tea 3.50
purchase_item_defaults(2, 5.00) # Be Careful. Check for logical Error
# Error. Comment the below after testing.
# purchase_item_defaults('Coffee') # Error. Coffee was assumed to be qty.
purchase_item_defaults(2, 'Coffee') # OK, used the default for price

print('\nTask 11. Use *args (arbitrary arguments) when you need the function')
print('to accept a varying number of arguments. Be careful because the')
print('logic within the function may not work for a varying number of args.')
average_price(4.00, 4.50, 5.00)
average_price(4.00, 4.50, 5.00, 5.50)

print('\nTask 12. Argument tuple unpacking is used on the call. This is used')
print('to unpack an existing iterable typically a list or tuple into')
print('individual arguments before passing the arguments to the function.')
print('After unpacking, they are treated like positional arguments.')
purchase = (3, 'Chocolate Bars', 2.50) # this is a tuple
purchase_item(*purchase) # The * in front of the list causes unpacking.
purchase_item_defaults(*purchase) # works with defaults

print('\nTask 13. Argument tuple packing and unpacking.')
prices = [2.50, 3.00, 3.50] # We unpack by using *prices below.
average_price(*prices) # Remember average_price accepts arbitrary *args

print('\nTask 14. Arbitrary Keyword Arguments, **kwargs. If you do not ')
print('know how many keyword arguments to pass into your function,')
print('add two ** asterisks before the parameter name in the')
print('function definition. When you call the function, specify the')
print('keywords in the function call. The parameters are stored in')
print('in a Python dictionary. Therefore, the keywords become the ')
print('dictionary key which is used to access the values.')
purchase_item_kwargs(qty=6, description='Apples', price=1.00)


if __name__ == '__main__':
    main()