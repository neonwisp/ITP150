""" 
nova_status.py
Author: ITP 150 Ashlee Raya
Date Created: 6/18/2026
This script prompts the user to enter if they are graduationg from NOVA this 
semester. It also calculates the years and months that the student has spent
at NOVA. It then prints the graduation status, years, and months spent at NOVA.
"""

name = input('Please enter your name:\n')
print('Are you graduating from NOVA this semester? (Enter True or press Enter '
      'for False)')
is_graduating = bool(input())

months_attended = int(input('How many months have you attended NOVA?\n'))

years = months_attended // 12  # floor division to extract the years
months = months_attended % 12  # modulo division to extract remaining months

dream_salary = float(input('What is your dream salary after graduation?\n'))


print('you have attended NOVA for ' +str(years) + ' year(s) and ' +
      str(months) + ' month(s).')
print('Your graduation status is', is_graduating, '.') 
print('Wow', name, '! Best wishes for a salary of $' +str(dream_salary) + '.')
