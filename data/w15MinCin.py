"""
Before plotting we are going to create a small dataset.
With temporary stats of the Week 15 NFL game:
Minnesota Vikings at Cincinnaty Bengals
16/12/2023
3:05 pm ET
"""
import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib.ticker import MultipleLocator   

minVikings_colors = ['#4F2683', '#FFC62F']
cinBengals_colors = ['#FB4F14', '#000000']

runningStats = {
    'Name': ['T.Chandler', 'N.Mullens', 'K.Nwangwu', 'C.Brown', 'J.Mixon', 'T.Williams'],
    'Runs': [16, 3, 1, 5, 4, 1],
    'Yards': [87, 5, 1, 14, 23, 10]
}

df = pd.DataFrame(runningStats)

# Add a column with the average yards per run
df['Avg'] = round(df['Yards']/df['Runs'], 1)
# Asign teams
df['Team'] = ['Min','Min','Min','Cin','Cin','Cin']

df['colors_1'] = df['Team'].apply(lambda x: minVikings_colors[0] if x == 'Min' else cinBengals_colors[0])
df['colors_2'] = df['Team'].apply(lambda x: minVikings_colors[1] if x == 'Min' else cinBengals_colors[1])


print(df)

fig, ax = plt.figure(figsize=(10,4), facecolor='#9F9F9F'), plt.axes(facecolor='#9F9F9F')

df['Avg'].plot.barh(ax = ax,
             color = df['colors_1'],
             edgecolor= df['colors_2'],
             linewidth = 2,
             width = 0.7)

plt.rcParams['font.family'] = 'Century Gothic'

for spine in 'bottom', 'left', 'top', 'right':
  ax.spines[spine].set_color('#E1DCE7')

xlim0, xlim1 = 0, round(df['Avg'].max()) + 1
ax.set_xlim([xlim0 , xlim1])
ax.set_xticks(range(xlim0, xlim1 + 1))
# Change both the ticks and ticklabels color
ax.tick_params(axis='x', colors='#E1DCE7')

ax.xaxis.set_minor_locator(MultipleLocator(1/10))
df['Avg'].plot.barh(ax=ax,
                    color=df['colors_1'],
                    edgecolor=df['colors_2'],
                    linewidth=1,
                    width=0.7, # Increase this value to make the bars wider
                    zorder=2)  

ax.yaxis.set_tick_params(length=0, which='major', rotation = 0)
ax.set_yticklabels(df['Name'], color='#E1DCE7')

ax.xaxis.grid(True, which='major', color='#E1DCE7', linestyle='-', zorder=1)
ax.xaxis.grid(True, which='minor', color='#E1DCE7', linestyle='--', linewidth=0.3, zorder=1)

ax.xaxis.set_tick_params(length=2, which='minor', color='#D1CBD7')
ax.set_xlabel('Yards per Run', color='#E1DCE7', loc='right')
ax.set_title('Vikings at Bengals: Running Game', 
             color='#E1DCE7', 
             pad=10, # Added some padding to separate from top spine
             loc='Left', # Moving title to the left
             fontproperties='Century Gothic'
             ) 
# Add another title in the right side
ax.set_title('16/12/2023 15:06 ET',
             color='#E1DCE7',
             loc='right',
             pad=10,
             fontsize=10,
             fontproperties='Century Gothic')
# Adding the average number for each player
for i, v in enumerate(df['Avg']):
    ax.text(v - 0.2, i, str(round(v, 2)), color='#E1DCE7', va='center', ha='right', 
            fontsize=9, zorder=4, fontproperties='Century Gothic')
for i, team in enumerate(df['Team']):
    ax.text(0.1, i, team, color= '#E1DCE7', va='center', ha='left', 
            fontsize=9,  zorder=4, fontproperties='Century Gothic')

# Save the vector PDF
plt.savefig('runsAVG_SomeText.pdf')
