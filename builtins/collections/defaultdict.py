from collections import defaultdict
from pprint import pprint

''' List creation example
Given a dictionary of items with tags, create a dictionary consisting of tags as
values and list of items as values.
Default dict will return an empty list if key doesn't exist, allowing append to 
be called on both existing and non-existing keys.
'''

my_places = {
    "Joe's Diner": ['restaurant', 'breakfast', 'lunch', 'dinner'],
    'La Bistro': ['bar', 'restaurant', 'lunch', 'dinner', 'sunday brunch'],
    'Corner Pub': ['bar', 'restaurant', 'lunch', 'dinner'],
    'Hipster Brewing': ['bar']
}

by_tag = defaultdict(list)
for place, tags in my_places.items():
    for tag in tags:
        by_tag[tag].append(place)

pprint(my_places)
print()
pprint(by_tag)
print()

''' Counting example using lambda to return initial value.
Counts tags each place has and number of places with a given tag
'''

counter = defaultdict(lambda: 0)
for place, tags in my_places.items():
    for tag in tags:
        counter[tag] += 1
        counter[place] += 1

pprint(counter)
