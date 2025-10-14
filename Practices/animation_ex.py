import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Create initial data
data = np.random.rand(10, 10)

# Set up the figure and initial imshow plot
fig, ax = plt.subplots()
im = ax.imshow(data, cmap='viridis', animated=True)

# Define the update function for each frame
def update(frame):
    # Modify the data for the current frame
    new_data = np.sin(frame / 10.0) * np.random.rand(10, 10) + np.cos(frame / 5.0)
    im.set_array(new_data)
    return [im]

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

# Show the animation
plt.show()