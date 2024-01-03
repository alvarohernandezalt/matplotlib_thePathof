import pandas as pd
import matplotlib.pyplot as plt

# Let's use some timebased data
url = "https://raw.githubusercontent.com/alvarohernandezalt/matplotlib_thePathof/main/data/hrp_state.csv"
df = pd.read_csv(url)
df

import matplotlib.dates as mdates
import matplotlib.ticker as ticker

fig, ax = plt.figure(figsize = (12, 6), facecolor='#9F9F9F'), plt.axes(facecolor='#9F9F9F')

# Change the params of both ticks and ticklegend
ax.tick_params(axis='x', colors='#C6C8CB')
ax.tick_params(axis='y', colors='#C6C8CB')

# Define formatter for date
xformatter = mdates.DateFormatter('%d-%m-%y')
ax.xaxis.set_major_locator(mdates.DayLocator(bymonthday=[1]))

# Define a custom formatter function
def custom_formatter(x, pos):
    return format(int(x), ',').replace(',', '.')
ax.yaxis.set_major_formatter(ticker.FuncFormatter(custom_formatter))


# Change the color of spines
for spine in 'bottom', 'left', 'top', 'right':
  ax.spines[spine].set_color('#C6C8CB')



df['Importe_MAX'] = df['Importe_MAX'].replace({'€': '', ',': '.'}, regex=True).astype(float)

df.set_index('fecha_RRR').plot(ax=ax)
ax.legend().set_visible(False)


ax.set_xlabel('Modified Day', color='#C6C8CB', fontproperties=font2);
ax.xaxis.set_major_formatter(xformatter)