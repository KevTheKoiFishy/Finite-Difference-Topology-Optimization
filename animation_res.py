import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from   matplotlib.animation import FuncAnimation

# Create initial data
data = pd.read_feather("sim_results.feather").values
data = np.log10(data)

with open("sim_settings.json", "r") as set_json:
    settings = json.loads(set_json.read())
sim_dims = settings["dim"]

lower = np.max(np.min(data), 0)
upper = np.max(data)

print(f"Data Bounds: [{lower}, {upper}]")

# Set up the figure and initial imshow plot
fig, ax = plt.subplots()
im = ax.imshow(data[0].reshape(sim_dims), vmin = lower, vmax = upper, cmap='RdPu', animated=True)
fig.colorbar(im)
frame_text = ax.text(0, 1.05, '', transform=ax.transAxes, ha='left', va='top') # Text object for frame number

# Define the update function for each frame
def update(frame):
    new_data = data[frame].reshape(sim_dims)
    im.set_array(new_data)
    frame_text.set_text(f'Frame: {frame}')

    return [im]

# Create the animation
ani = FuncAnimation(fig, update, frames=np.unique(np.uint32(np.logspace(0, np.log10(len(data)), 200)))[:-1], interval=10, blit=False)

# Show the animation
plt.show()