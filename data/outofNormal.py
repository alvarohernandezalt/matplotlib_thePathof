import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties  
from matplotlib.patches import ConnectionPatch

fig = plt.figure(figsize=(7,6), facecolor='#9F9F9F')

# Generate random data
n = 200
x = np.random.normal(size = n)
y = np.random.normal(size = n)
z = np.concatenate([np.array([4]), 1- x[1:]**2])

ax12 = fig.add_subplot(2,2,(1,2), facecolor='#9F9F9F')
ax12.scatter(x,y,alpha = 0.5, color='#EBA62A')
ax12.tick_params(axis='x', colors='#C6C8CB')
ax12.tick_params(axis='y', colors='#C6C8CB')
for spine in 'bottom', 'left', 'top', 'right':
    ax12.spines[spine].set_color('#C6C8CB')

ax3 = fig.add_subplot(2,2,3, facecolor='#9F9F9F')
ax3.scatter(x,z,alpha = 0.5, color='#EBA62A')
ax3.tick_params(axis='x', colors='#C6C8CB')
ax3.tick_params(axis='y', colors='#C6C8CB')
for spine in 'bottom', 'left', 'top', 'right':
    ax3.spines[spine].set_color('#C6C8CB')

ax4 = fig.add_subplot(2,2,4, facecolor='#9F9F9F')
ax4.scatter(y,z,alpha = 0.5, color='#EBA62A')
ax4.tick_params(axis='x', colors='#C6C8CB')
ax4.tick_params(axis='y', colors='#C6C8CB')
for spine in 'bottom', 'left', 'top', 'right':
    ax4.spines[spine].set_color('#C6C8CB')

con = ConnectionPatch(
    xyA = (x[0], y[0]),
    coordsA = ax12.transData,
    xyB = (x[0], z[0]),
    coordsB = ax3.transData,
    arrowstyle = '<|-|>',
    shrinkA = 2,
    shrinkB = 0,
    color = '#C6C8CB')
fig.add_artist(con)

con = ConnectionPatch(
    xyA = (x[0], y[0]),
    coordsA = ax12.transData,
    xyB = (y[0], z[0]),
    coordsB = ax4.transData,
    arrowstyle = '<|-|>',
    shrinkA = 2,
    shrinkB = 0,
    color = '#C6C8CB')
fig.add_artist(con)

ax12.set_xlabel('$x$', color = '#C6C8CB')
ax12.set_ylabel('$y$', color = '#C6C8CB')

ax3.set_xlabel('$x$', color = '#C6C8CB')
ax3.set_ylabel('$z$', color = '#C6C8CB')

ax4.set_xlabel('$y$', color = '#C6C8CB')
ax4.set_ylabel('$z$', color = '#C6C8CB')

fig.suptitle('Out of Normal', fontproperties=font2, color='#C6C8CB', fontsize=13)

plt.tight_layout();