#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import matplotlib.pyplot as plt

# Load temperature and precipitation data from CSV files
temp_data = pd.read_csv("NY.csv")


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6), layout="constrained")

# Plot extreme minimum temperatures for each year. Lowest daily minimum temperature for the
# year. Given in Fahrenheit.
ax1.step(
    temp_data["DATE"],
    temp_data["EMNT"],
    "-2",
    
    where="mid",
    label="lowest temp",
)
ax1.set_xlabel("Year")
ax1.set_ylabel(" (°F)")
ax1.set_title("Extreme minimum temperature for each year")
ax1.grid(True)
ax1.legend()
ax1.legend(loc="upper left")

# Plot data with number of days with snow depth >= 1 inch/25 millimeters
temp_mean = temp_data.groupby((temp_data["DATE"] // 10) * 10).mean()
ax2.bar(
    temp_mean["DATE"],
    temp_mean["DSND"],
    linestyle="solid",
    color="yellow",
    width=5,
    label="AVG for decade",
)
ax2.set_xlabel("Year")
ax2.set_ylabel("Num of days")
ax2.set_title("Avg num of days with snow depth >= 1 inch for each decade")
ax2.grid(True)
ax2.legend()
ax1.set_facecolor('black')
ax2.set_facecolor('black')

# Save the figure
plt.savefig("snow_and_extreme_temp_days.png")


# In[ ]:




