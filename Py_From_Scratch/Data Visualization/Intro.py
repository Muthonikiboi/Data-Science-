import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample data as you already have
np.random.seed(40)

data = {
    "Month": ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    "Sales": np.random.randint(200, 500, 6),
    "Customers": np.random.randint(50, 200, 6),
    "Profit": np.random.randint(50, 150, 6)
}

data1 = {
    "Month": ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    "Sales": np.random.randint(400, 1000, 6),
    "Customers": np.random.randint(300, 500, 6),
    "Profit": np.random.randint(150, 350, 6)
}

# Creating DataFrames
df = pd.DataFrame(data)
df_2 = pd.DataFrame(data1)

# Plotting
plt.figure(figsize=(10, 7))

# Convert 'Month' to a list to avoid the issue
plt.plot(
    df['Month'].tolist(),   # Convert to list
    df['Sales'],            # Sales values
    color='b',              # Blue color for the plot
    marker='o',             # Circle markers
    linestyle='-', 
    label='Sales (Data 1)'
)

plt.plot(
    df_2['Month'].tolist(), # Convert to list
    df_2['Sales'],          # Sales values
    color='r',              # Red color for the plot
    marker='o',             # Circle markers
    linestyle='-', 
    label='Sales (Data 2)'
)

# Adding labels and title
plt.title('Sales vs Month') 
plt.xlabel('Months') 
plt.ylabel('Sales') 
plt.legend()  # Show the legend

plt.show()
