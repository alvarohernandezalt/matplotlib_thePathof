"""
This Python script is primarily focused on 
importing various libraries and modules 
that are commonly used for data analysis and visualization.
"""

import pandas as pd     
import numpy as np  
import math  
import random  

from scipy import stats  


import matplotlib as mpl 
import matplotlib.pyplot as plt   
import matplotlib.animation as animation  
import matplotlib.colors as mcolors  
import matplotlib.dates as mdates  
import matplotlib.ticker as mticker  

from matplotlib.ticker import MultipleLocator
from matplotlib import font_manager  
from matplotlib.patches import Polygon  
from matplotlib.patches import Rectangle  
from matplotlib.patches import ConnectionPatch  



"""
This method converts the matplotlib figure to a vectorized image.
So we can change the scale of the image without loss of quality.
"""
# Import matplotlib_inline
from matplotlib_inline.backend_inline import set_matplotlib_formats
# Set the format to SVG. The vectorized image is saved in the background.
set_matplotlib_formats('svg')

# Alternative way:
# %config InlineBackend.figure_format = 'svg'