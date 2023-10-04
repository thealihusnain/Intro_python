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
# ---------------------------------------------------------------------------------------------------------------------------------
# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital': 'rome','po;ulation':59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)

