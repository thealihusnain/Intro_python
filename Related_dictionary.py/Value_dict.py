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