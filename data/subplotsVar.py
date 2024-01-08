import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import random

font2 = FontProperties()
font2.set_family('DINPro')
font2.set_weight('bold')

fig = plt.figure(facecolor='#9F9F9F')

tColors = ["#252759", "#202140", "#BF452A", "#D93A2B"]

for i in range(1,10):
    ax = fig.add_subplot(3,3,i)
    for spine in 'bottom', 'left', 'top', 'right':
        ax.spines[spine].set_color(random.choice(tColors))
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_facecolor('#9F9F9F')
    ax.text(0.5,0.5,
                    s=str(i),
                    ha='center',
                    va='center',
                    fontproperties=font2,
                    fontsize=25,
                    color=random.choice(tColors))
    ax.set_title(f'Chart {i}', fontproperties=font2, color=random.choice(tColors))

fig.suptitle('Chart of Charts', fontproperties=font2, color='#C6C8CB', fontsize=13)
plt.tight_layout(rect=(0,0,1,1))