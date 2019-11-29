#Assignment 4a
#Use a dictionary to store information about a person you know. 
# Store their first name, last name, age, and the city in which they live. 
# You should have keys such as first_name, last_name, age, and city. 
# Print each piece of information stored in your dictionary. 
# Add a new key value pair about qualification then update the qualification 
# value to high academic level then delete it.
#Author: Salman Moin
#Date: 29-Nov-2019 

my_dict = {'first_name':'Imran', 'last_name':'Khan', 'age':'62', 'City':'Islamabad'}
print(my_dict.values())

# adding new key/value pair for 'qualification'
my_dict['qualification'] = 'Masters in Polictical Science'
for x, y in my_dict.items():
    print(x, y)

# deleting key 'qualification'
my_dict.pop('qualification')
for x, y in my_dict.items():
    print(x, y)


