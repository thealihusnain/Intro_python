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
print(f"Capital of the {Country_Name} Country is :",Get_capital)