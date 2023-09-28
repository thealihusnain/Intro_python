import numpy as np

# create a two array with different variable 
arr_1 = np.array([9,3,5,6,78,2])
arr_2 = np.array([9,3,7,5,78,2])

# rearrange the list into the colums stack.
arrange_colum = np.column_stack((arr_1,arr_2))
print(arrange_colum)

# rearrange the list into the row stack
arrange_rom = np.row_stack((arr_1,arr_2))
print(arrange_rom)

# use the roll method in numpy
arr_1[1] = np.roll(arr_1[1],1)

print ("use the roll method in list :",arr_1)



import numpy as np
np_2d = np.array([[2,3],[4,5]])    
print(np_2d[-2,1])



