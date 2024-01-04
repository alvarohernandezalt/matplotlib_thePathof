import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import wishart, chi2
from scipy.integrate import quad
from matplotlib.ticker import FuncFormatter


fig, ax = plt.figure(figsize = (12, 6), facecolor='#9F9F9F'), plt.axes(facecolor='#9F9F9F')

# Change the params of both ticks and ticklegend
ax.tick_params(axis='x', colors='#C6C8CB')
ax.tick_params(axis='y', colors='#C6C8CB')

# Change the color of spines
for spine in 'bottom', 'left', 'top', 'right':
  ax.spines[spine].set_color('#C6C8CB')

ax.set_xlim(0.0,8.0)
ax.set_ylim(0,0.3)

formatter = FuncFormatter(lambda x, pos: "{:.2f}".format(x))
ax.xaxis.set_major_formatter(formatter)

scale_matrix = np.array([[1]])

x = np.linspace(1e-5, 8, 100)
w = wishart.pdf(x, df=3, scale=scale_matrix); w[:5]

ax.plot(x,w,color='#EBBD2A', linewidth=2)
ax.set_title('Wishart Random Variable', color='#C6C8CB', fontproperties=font2, fontsize=12)

# Set a point
z = 3.30
pdfz= wishart.pdf(z, df=3, scale=scale_matrix)
ax.plot([z,z],
       [0,pdfz],
       color='#EB452A',
       linestyle='dashed')
ax.plot(z,pdfz,color='#EB452A',marker='.',)
ax.text(z + .1, pdfz,
        s='z = {:.2f}'.format(z), color='#C6C8CB', size = 11)

# Fill the area
x_vals = np.linspace(1e-5, z, 100)
pdfx_vals = wishart.pdf(x_vals, df=3, scale=scale_matrix); w[:5]
ax.fill_between(x_vals,
                np.zeros(100),
                pdfx_vals,
                color='#EBA62A',
                alpha=.5)

# Calculate the area and put a text with its value
def pdf(x):
  return wishart.pdf(x, df=3, scale=scale_matrix)

area, error = quad(pdf, 1e-5, z)

ax.text(z/2, pdfz/2,
        s='{:.2f}'.format(area),
        fontproperties=font2, # you need to declare the fontproperties first
        size = 11,
        color='#C6C8CB',
        ha='center');

# Existing code
ax2 = ax.twinx()  # Create a second y-axis

# Calculate the areas for all z values and plot them
areas = [quad(pdf, 1e-5, z_val)[0] for z_val in x]
ax2.plot(x, areas, color='blue', linestyle='dashed')

# Set the y-label for the second y-axis
ax2.set_ylabel('Area under the curve', color='blue')


# Calculate the scaling factor
scale_factor =  0.65 / 0.13918138075553632 

# Get the current y-limits of the primary axis
ymin, ymax = ax.get_ylim()

# Set the y-limits of the secondary axis using the scaling factor
ax2.set_ylim(ymin * scale_factor, ymax * scale_factor)

plt.savefig('WishartRandomVariable.pdf', bbox_inches='tight')
