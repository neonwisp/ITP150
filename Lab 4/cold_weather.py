"""
cold_weather.py
Author: ITP 150 Ashlee Raya
Date Created: July 7, 2026
This program issues a cold weather advisory within the state of Virginia
based on the following conditions:

A Cold Weather Advisory is issued when either wind chill or temperature
is expected to fall to:
    * 0 to -9 degrees east of the Blue Ridge Mountains
    * -10 to -19 degrees west of and including the Blue Ridge Mountains

Wind Chill Temperature = 35.74 + 0.6215T - 35.75(V^0.16) + 0.4275T(V^0.16)
Where:
T = Air Temperature (in Fahrenheit)
V = Wind Speed (in mph)
^ = raised to a power (exponential)
"""

cold_weather_advisory = False
temperature = float(input('Please enter the temperature in Fahrenheit:'))
wind_speed = int(input('Please enter the wind speed in mph as an integer:'))
wind_chill = (35.74 + 0.6215 * temperature - 35.75 * (wind_speed**0.16)
            + 0.4275 * temperature * (wind_speed**0.16))
print('Please enter your region from the menu below:')
print('E for East of Blue Ridge Mountains:')
print('W for Blue Ridge and areas West:')
region = input()
# decision structure to determine cold weather advisory
if region.upper() == 'E':
    if temperature >= -9 and temperature <= 0:
        cold_weather_advisory = True
    if wind_chill >= -9 and wind_chill <= 0:
        cold_weather_advisory = True
if region.upper() == 'W':
    if (temperature >= -19 and temperature <= -10) \
        or (wind_chill >= -19 and wind_chill <= -10):
         cold_weather_advisory = True
if cold_weather_advisory:
    message = 'Cold Weather Advisory Issued'
else:
    message = 'No Cold Weather Advisory'
print("Temperature", temperature)
print("Wind Speed", wind_speed)
print("Wind Chill", wind_chill)
print(message)
