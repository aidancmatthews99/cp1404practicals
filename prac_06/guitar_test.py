from prac_06.guitar import Guitar

lindsay_guitar = Guitar('Gibson L-5 CES', 1922, 16035.4)
print(lindsay_guitar)
print(lindsay_guitar.get_age())
print(lindsay_guitar.is_vintage())

another_guitar = Guitar('Tanglewood', 2012, 345.63)
print(another_guitar)
print(another_guitar.get_age())
print(another_guitar.is_vintage())