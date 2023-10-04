# how to print al the values of a dictionary in python?
europe = {
    'spain':'madrid', 
    'france':'paris', 
    'germany':'berlin', 
    'norway':'oslr'
    }

# disply the value of dictionary to get the function values
value_disp = europe.values()
print(value_disp)

for key,value in europe.items():
    print(value)

# how to get a list of all the keys from a python dictionary?
list_of_key = list(europe.keys())

print(list_of_key)

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe

print('italy' in europe)
# Add poland to europe
europe['poland'] = 'warsaw'

# Print europe
print(europe)



# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia
europe.pop('australia')


# Print europe
print(europe)
# --------------------------------------------------------------------------------------------- add one dictionary to another dictionary ---------------------------------------------------
# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital': 'rome','population':59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)

# -------------------------------------- pandas libery use ---------------------------------------------------------------

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {
    'country': names,
    'drives_right':dr,
    'cars_per_cap':cpc
}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

# -------------------------------------------------------------

import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)



# ------------------------------------------------------------------------------------------------------

# Import cars data
import pandas as pd
company_sales_data = pd.read_csv('company_sales_data.csv', index_col = 0)

# Print out country column as Pandas Series
print(company_sales_data['total_profit'])

# Print out country column as Pandas DataFrame
# print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(company_sales_data[['total_units','total_profit']])