import json
import matplotlib.pyplot as plt
import numpy as np
from   matplotlib.animation import FuncAnimation

# Create initial data
with open("sim_results.json", "r") as res:
    data = np.array(json.loads(res.read()))

lower = np.min(data)
upper = np.max(data)
print(upper)

print(f"Data Bounds: [{lower}, {upper}]")

# Set up the figure and initial imshow plot
fig, ax = plt.subplots()
im = ax.imshow(data[0], vmin = lower, vmax = upper, cmap='RdPu', animated=True)
fig.colorbar(im)
frame_text = ax.text(0, 1.05, '', transform=ax.transAxes, ha='left', va='top') # Text object for frame number

# Define the update function for each frame
def update(frame):
    new_data = data[frame]
    im.set_array(new_data)
    frame_text.set_text(f'Frame: {frame}')

    return [im]

# Create the animation
ani = FuncAnimation(fig, update, frames=range(0, len(data), 10), interval=10, blit=False)

# Show the animation
plt.show()