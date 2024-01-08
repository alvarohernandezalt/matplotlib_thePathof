import matplotlib.pyplot as plt

fig, ax = plt.subplots(1,2)
ax[0].set_title('X0', color='#C6C8CB', fontproperties=font2)
ax[1].set_title('X1', color='#C6C8CB', fontproperties=font2)

# Change the params of both ticks and ticklegend
ax[0].tick_params(axis='x', colors='#C6C8CB')
ax[0].tick_params(axis='y', colors='#C6C8CB')
ax[1].tick_params(axis='x', colors='#C6C8CB')
ax[1].tick_params(axis='y', colors='#C6C8CB')

# Change the color of spines
for spine in 'bottom', 'left', 'top', 'right':
  ax[0].spines[spine].set_color('#C6C8CB')
for spine in 'bottom', 'left', 'top', 'right':
  ax[1].spines[spine].set_color('#C6C8CB')

plt.tight_layout()