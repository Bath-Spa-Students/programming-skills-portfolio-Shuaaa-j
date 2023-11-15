''' Instructions for exercise 5.4
Make a dictionary containing three major rivers and the country each river runs through. 
One key-value pair might be 'nile': 'egypt'.
* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
* Use a loop to print the name of each river included in the dictionary.
* Use a loop to print the name of each country included in the dictionary.'''

# Defines the dictionary
rivers = {
    "Yangtze": "China",
    "Yenisey": "Siberia",
    "Nile": "Egypt"
}

# Print a sentence about each river, it's names, and respective countries
for river, country in rivers.items():
    print(f"The magnificent {river} river runs through {country}.")

print("\nNames of rivers:")
for river in rivers.keys():
    print(river)

print("\nNames of countries:")
for country in rivers.values():
    print(country)
