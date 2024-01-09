import os
import matplotlib
from matplotlib import font_manager
import shutil
import glob

# Get the current config directory
config_dir = matplotlib.get_configdir()

# Append your font directory to the config directory
font_dir = os.path.join(config_dir, "fonts", "otf")

# Check if the font directory exists, if not, create it
if not os.path.exists(font_dir):
    os.makedirs(font_dir)

# Path to your font directory
your_font_dir = "C:/Users/ÁlvaroHernández/Documents/GitHub/matplotlib_thePathof/fonts/DINPro"

# Copy all OTF font files to the font directory
for font_file in glob.glob(os.path.join(your_font_dir, "*.otf")):
    shutil.copy(font_file, font_dir)

# Delete the existing font cache
font_cache_path = font_manager.get_cachedir()
font_list_cache = os.path.join(font_cache_path, 'fontlist-v310.json')
if os.path.exists(font_list_cache):
    os.remove(font_list_cache)