import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import wishart, chi2

fig, ax = plt.figure(figsize = (12, 6), facecolor='#9F9F9F'), plt.axes(facecolor='#9F9F9F')

# Change the params of both ticks and ticklegend
ax.tick_params(axis='x', colors='#C6C8CB')
ax.tick_params(axis='y', colors='#C6C8CB')

# Change the color of spines
for spine in 'bottom', 'left', 'top', 'right':
  ax.spines[spine].set_color('#C6C8CB')

ax.set_xlim(0.0,8.0)
ax.set_ylim(0,0.3)

x = np.linspace(1e-5, 8, 100)
w = wishart.pdf(x, df=3, scale=1); w[:5]

ax.plot(x,w,color='#EBBD2A', linewidth=2)
ax.set_title('Wishart Random Variable', color='#C6C8CB', fontproperties=font2, fontsize=12)

# Set a point
z = 3.3
pdfz= wishart.pdf(z, df=3, scale=1)
ax.plot([z,z],
       [0,pdfz],
       color='#EB452A',
       linestyle='dashed')
ax.plot(z,pdfz,color='#EB452A',marker='.',)
ax.text(z + .1, pdfz,
        s=f'z = {z}', color='#C6C8CB')

# Fill the area
x_vals = np.linspace(0, z, 100)
pdfx_vals = wishart.pdf(x_vals, df=3, scale=1); w[:5]
ax.fill_between(x_vals,
                np.zeros(100),
                pdfx_vals,
                color='#EBA62A',
                alpha=.5)