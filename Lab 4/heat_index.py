"""
heat_index.py
Author: ITP 150 Ashlee Raya
Date Created: July 7, 2026
This program is a warning system to the user that notifies the user of the
classification and possible medical conditions that may result from a heat
index in Fahrenheit measured in the ranges below:
Temperature in F Classification Possible Medical Condition
< 80 No Warning No Warning associated with measured heat index.
80-90 Caution Fatigue Possible
91-103 Extreme Caution Possible Heat Stroke, Heat Cramps, Heat Exhaustion
104-124 Danger Likely Heat Stroke, Heat Cramps, Heat Exhaustion
125 or higher Extreme Danger Heat Stroke Highly Likely
"""

temperature = int(input('Please enter the temperature in F as an integer:\n'))
# decision structure to determine classification and possible medical conditions
if temperature < 80:
    classification = 'No Warning'
    possible_med_cond = 'No Warning Associated with measured heat index.'
elif temperature <= 90:
    classification = 'Caution'
    possible_med_cond = 'Fatigue Possible'
elif temperature <= 103:
    classification = 'Extreme Caution'
    possible_med_cond = 'Possible Heat Stroke, Heat Cramps, Heat Exhaustion'
elif temperature <= 124:
    classification = 'Danger'
    possible_med_cond = 'Likely Heat Stroke, Heat Cramps, Heat Exhaustion'
else:
    classification = 'Extreme Danger'
    possible_med_cond = 'Heat Stroke Highly Likely'
# display output in tabular format
print(f'{"Heat Index":30s}{temperature:50d}')
print(f'{"Classification":30s}{classification:>50s}')
print(f'{"Possible Medical Condition":30s}{possible_med_cond:>50s}')
