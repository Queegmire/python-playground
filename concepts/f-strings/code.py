''' F-strings with classes and __repr__
USing the !r modifier at the end of a variable will make it use __repr__
instead of __str__
'''

class City:
    def __init__(self, name, location, population):
        self.name = name
        self.location = location
        self.population = population

    def __str__(self):
        return f"The city of {self.name} in {self.location} has {self.population} residents."

    def __repr__(self):
        args = ', '.join([repr(self.name), repr(self.location), repr(self.population)])
        return f'City({args})'


city = City('Seattle', 'Washington', 800_000)

print(f'{city}')
print()
print(f'{city!r}')
