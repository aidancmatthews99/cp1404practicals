from prac_06.guitar import Guitar

guitars = []
print('My guitars!')
guitar_name = input("Name: ")

while guitar_name != '':
    guitar_year = int(input('Year: '))
    guitar_cost = float(input('Cost: '))
    guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
    print(guitars[-1], 'added\n')
    guitar_name = input('Name: ')

print('These are my guitars: ')
for i, guitar in enumerate(guitars, 1):
    vintage_string = ' (vintage)' if guitar.is_vintage() else ''
    print("Guitar {}: {guitar.name} ({guitar.year}), worth ${guitar.cost:.2f}{}".format(i, vintage_string,
                                                                                        guitar=guitar,))
