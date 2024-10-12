#!/usr/bin/env python3

# Dictionaries
dict_york = {'Address': '100 New Street', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['100 New Street', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    # Create a dictionary from keys and values lists
    return dict(zip(keys, values))

def shared_values(dict1, dict2):
    # Find shared values between two dictionaries
    return set(dict1.values()).intersection(dict2.values())

if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)
