#app en python

import pandas as pd
import numpy as np
import plotly.express as px

# Sample data
data = {'Category': ['A', 'B', 'C', 'D'],
        'Value': [10, 15, 7, 12]}
df = pd.DataFrame(data)

# Create the bar chart
fig = px.bar(df, x='Category', y='Value', title='Sample Bar Chart')

# Show the plot
fig.show()