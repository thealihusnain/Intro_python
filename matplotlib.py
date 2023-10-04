# importing packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# load data from the local system
df = pd.read_csv(r'C:\Users\CNS\Documents\working_data\company_sales_data.csv')

Total_units=df['total_units']
Total_profit = df['total_profit']

plt.plot(Total_profit,Total_units)
plt.show()