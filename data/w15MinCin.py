"""
Before plotting we are going to create a small dataset.
With temporary stats of the Week 15 NFL game:
Minnesota Vikings at Cincinnaty Bengals
16/12/2023
3:05 pm ET
"""
import pandas as pd 

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

df['Avg'].plot.barh(ax = ax,
             color = df['colors_1'],
             edgecolor= df['colors_2'],
             linewidth = 3,
             width = .7)  # Increase this value to make the bars wider

