"""
table.py
Author: ITP 150 Ashlee Raya
Date Created: 6/18/2026
This program calculates the number of mosaic tiles needed to cover a round
table for a DIY furniture project. When carpenters and craftsman estimate
materials to order, they apply a waste factor to order more than they need
realizing that mistakes are made during construction and materials may be
defective. The waste factor for this project is 20 %.
"""

import math

WASTE_FACTOR = .20  # Declare the WASTE_FACTOR as a constant

# getting input from the user
print('Please enter the diameter of the table in inches:')
table_diameter = float(input())
tile_length = float(input('Please enter the length of the tile in inches:\n'))
tile_width = float(input('Please enter the width of the tile in inches:\n'))

# calculating the area of a table
radius = table_diameter / 2
table_area = math.pi * radius ** 2

# calculating the area of a tile
tile_area = tile_length * tile_width

# calculating the approximate number of tiles needed
approx_tiles_needed = table_area / tile_area

# rounding up because you can't buy a fraction of a tile
minimum_tiles_needed = math.ceil(approx_tiles_needed)

# applying the waste factor to the minimum tiels needed for the final tiles needed
tiles_needed = math.ceil(minimum_tiles_needed * (1 + WASTE_FACTOR)) 

print('Project Details')
print('Table Diameter:' , table_diameter)
print('Table Area:' , table_area)
print('Tile Length:' , tile_length)
print('Tile Width:' , tile_width)
print('Tile Area:' , tile_area)
print('Tiles Needed:' , tiles_needed)