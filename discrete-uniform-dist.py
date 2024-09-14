import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import randint

# Streamlit app title
st.title("Discrete Uniform Distribution")

# User input for range of values (low and high for uniform distribution)
low = st.slider("Select the lower bound (inclusive)", min_value=1, max_value=50, value=1, step=1)
high = st.slider("Select the upper bound (exclusive)", min_value=2, max_value=100, value=10, step=1)

# Generate discrete uniform distribution (randint) pmf values
x = np.arange(low, high)
pmf = [1 / (high - low) for _ in x]

# Plot the Discrete Uniform Distribution PMF
fig, ax = plt.subplots()
ax.bar(x, pmf, color='lightgreen')
ax.set_title(f'Discrete Uniform Distribution PMF (low = {low}, high = {high})')
ax.set_xlabel('Value')
ax.set_ylabel('PMF')
ax.set_ylim(0, 1)
ax.grid(True)

# Display the plot in Streamlit
st.pyplot(fig)

# Show the PMF values
st.write("PMF values:")
st.write(dict(zip(x, pmf)))
