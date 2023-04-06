#!/usr/bin/env python
# coding: utf-8

# In[21]:


# Plot temperature data with points for each year
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))
ax[0].step(
    temp_data["DATE"],
    temp_data["TAVG"],
    linestyle="solid",
    color="orange",
    where="mid",
    label="Temperature",
)
ax[0].set_xlabel("Year")
ax[0].set_ylabel("(°F)")
ax[0].set_title("Average temperature & precipitation in New York for each year")
ax[0].grid(True)
ax[0].legend(loc="upper left")

# Plot precipitation data with points for each year
ax[1].step(
    temp_data["DATE"],
    temp_data["PRCP"],
    linestyle="solid",
    color="green",
    where="mid",
    label="Precipitation",
)
ax[1].set_xlabel("Year")
ax[1].set_ylabel(" (in)")
ax[1].grid(True)
ax[1].legend(loc="upper left")

# Plot temperature trend data on the left axis with points for each decade
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
temp_mean = temp_data.groupby((temp_data["DATE"] / 10) * 10).mean()
ax[1, 0].plot(temp_mean["DATE"], temp_mean["PRCP"], "s-b")
ax[1, 0].set_xlabel("Year")
ax[1, 0].set_ylabel(" (in)")
ax[1, 0].set_title("Precipitation trends")
ax[1, 0].grid(True)

# Plot temperature trend data on the left axis with points for each decade
temp_mean = temp_data.groupby((temp_data["DATE"]/ 10) * 10).mean()
ax[1, 1].plot(temp_mean["DATE"], temp_mean["TAVG"], "s-r")
ax[1, 1].set_xlabel("Year")
ax[1, 1].set_ylabel("(°F)")
ax[1, 1].set_title("Temperature trends")
ax[1, 1].grid(True)


# Save the figure
plt.savefig("mosaic_temp_precip.png")


# In[ ]:




