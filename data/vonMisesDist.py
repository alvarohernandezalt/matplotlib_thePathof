import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties  
from matplotlib.patches import ConnectionPatch
import matplotlib.gridspec as gridspec
from matplotlib.ticker import FuncFormatter

font2 = FontProperties()
font2.set_family('DINPro')
font2.set_weight('bold')

fig = plt.figure(figsize=(12,6),facecolor='#9F9F9F')

formatter = FuncFormatter(lambda x, pos: "{:.1f}".format(x))

spec = gridspec.GridSpec(ncols=4,
                         nrows=2,
                         figure=fig)

# Generate smaples of the probability density for the von Mises distribution
mu, kappa = 0.0, 10.0 # Mean and Dispersion
x = np.random.vonmises(mu, kappa, 1000)
y = x**3 + np.random.vonmises(mu, kappa, 1000)

ax1 = fig.add_subplot(spec[0, 0:3], facecolor='#9F9F9F')
ax1.plot(x,y,
         linestyle='None',
         marker='.',
         alpha=0.5,
         color='#E8C16D')
ax1.tick_params(axis='x', colors='#C6C8CB')
ax1.tick_params(axis='y', colors='#C6C8CB')
for spine in 'bottom', 'left', 'top', 'right':
    ax1.spines[spine].set_color('#C6C8CB')

ax1.xaxis.set_major_formatter(formatter)
ax1.yaxis.set_major_formatter(formatter)

ax2 = fig.add_subplot(spec[1, 0:3], sharex = ax1, facecolor='#9F9F9F')
ax2.hist(y, orientation='vertical', bins=50, color='#E8C16D')
ax2.invert_yaxis()
ax2.tick_params(axis='x', colors='#C6C8CB')
ax2.tick_params(axis='y', colors='#C6C8CB')
for spine in 'bottom', 'left', 'top', 'right':
    ax2.spines[spine].set_color('#C6C8CB')

ax2.xaxis.set_major_formatter(formatter)
ax2.yaxis.set_major_formatter(formatter)

ax3 = fig.add_subplot(spec[0, 3:4], sharey = ax1, facecolor='#9F9F9F')
ax3.hist(x, orientation='horizontal', bins=50, color='#E8C16D')
ax3.tick_params(axis='x', colors='#C6C8CB')
ax3.tick_params(axis='y', colors='#C6C8CB')
for spine in 'bottom', 'left', 'top', 'right':
    ax3.spines[spine].set_color('#C6C8CB')

ax3.xaxis.set_major_formatter(formatter)
ax3.yaxis.set_major_formatter(formatter)

fig.suptitle('von Mises Distribution', fontproperties=font2, color='#C6C8CB', fontsize=13, x=0.5, y=0.98)

plt.tight_layout()
plt.savefig('vonMisesDist.pdf', bbox_inches='tight');