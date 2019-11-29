#Assignment 4b
#Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
# Create a dictionary of information about each city and include the country that the city is in, 
# its approximate population, and one fact about that city. The keys for each city’s 
# dictionary should be something like country, population, and fact. 
# Print the name of each city and all of the information you have stored about it.
#Author: Salman Moin
#Date: 29-Nov-2019 

# difining three dictionaries for each city in an array
cities = {
    0: {
        'city_name':'New York',
        'country': 'USA',
        'population': '8.6 million',
        'fact': 'Business hub of USA'
    },
    1: {
        'city_name':'Dubai',
        'country': 'UAE',
        'population': '3.1 million',
        'fact': 'Tourism'
    },
    2: {
        'city_name':'Karachi',
        'country': 'Pakistan',
        'population': '14.9 million',
        'fact': 'Noise and pollution'
    }
}

# Printing all values in cities dictionary
for city_id, city_info in cities.items():
    print("\nCity ID:", city_id)
    
    for key in city_info:
        print(key + ':', city_info[key])






