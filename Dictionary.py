import numpy as np

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']


# Get the index of the germany from the countries list
Get_index = countries.index('norway')

# Store the Country name 
Country_Name = countries[Get_index]

# Now findout the capital of germany in capitals list
Get_capital = capitals[Get_index]

# Print out the captials of the germany
# print(f"Capital of the {Country_Name} Country is :",Get_capital)

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys and value in europe
key_europ = europe.keys()
value_of_key_europ = europe.values()
print("key and value of the europ dict :", key_europ ,value_of_key_europ)

# Print out value that belongs to key 'norway'
print(europe['norway'])

for key,value in europe.items():

    print(f"{key} of the value is : ",value)


# how to print al the values of a dictionary in python?
europe_ = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
for key,value in europe_.items():
    print(value)