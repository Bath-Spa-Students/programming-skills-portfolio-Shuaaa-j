''' Intsructions for exercise 7.5
Write a function called describe_city() that accepts the name of a city and its country. 
The function should print a simple sentence, such as Reykjavik is in Iceland. 
Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the default country.'''

# Declaring a function
def describe_city(city, country="UAE"):
    print(f"{city} is in the amazing country of {country}.")

# Calls the function 
describe_city("Reykjavik", "Iceland")
describe_city("Dubai", )  # Uses the default country
describe_city("Manila", "Philippines") 

