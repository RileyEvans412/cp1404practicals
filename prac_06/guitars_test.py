"""
CP1404 Practical
Guitar test program.
"""
from prac_06.guitar import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)

print("{}, get_age - Expected 97. Got {}".format(guitar.name, guitar.get_age()))
print("{}, is_vintage - Expected True. Got {}".format(guitar.name, guitar.is_vintage()))

guitar = Guitar("Another Guitar", 2012, 1512.9)

print("{}, get_age - Expected 7. Got {}".format(guitar.name, guitar.get_age()))
print("{}, is_vintage - Expected False. Got {}".format(guitar.name, guitar.is_vintage()))

