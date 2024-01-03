import matplotlib.dates as mdates

fig, ax = plt.figure(figsize = (24, 6), facecolor='#9F9F9F'), plt.axes(facecolor='#9F9F9F')

# Change the params of both ticks and ticklegend
ax.tick_params(axis='x', colors='#C6C8CB')
ax.tick_params(axis='y', colors='#C6C8CB')

# Define formatter for date
xformatter = mdates.DateFormatter('%d-%m')

# Change the color of spines
for spine in 'bottom', 'left', 'top', 'right':
  ax.spines[spine].set_color('#C6C8CB')


df = df_clean.drop(columns=['ESTADO_SEGUIMIENTO','cambiadoSeguimientoLast', 'OP_NOMBRE', 'TIPOLOGIA'])
df['Importe_MAX'] = df['Importe_MAX'].replace({'€': '', ',': '.'}, regex=True).astype(float)

ax.plot(df.Created, df.Importe_MAX);

ax.legend().set_visible(False)
ax.set_xlabel('Created Time', color='#C6C8CB', fontproperties=font2);
ax.xaxis.set_major_formatter(xformatter)