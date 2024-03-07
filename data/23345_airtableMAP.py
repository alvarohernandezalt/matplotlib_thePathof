import matplotlib.ticker as mtick

# Values
years = ['AIR + NOLOCO(25)**', 'AIR + NOLOCO(15)*', 'AIRTABLE', 'MYSQL + NODB + NOLOCO***']
profits = [24060, 15600, 42000, 11000]

fig, ax = plt.figure(figsize = (10, 6), facecolor='#C6C8CB'), plt.axes(facecolor='#C6C8CB')

# Change the params of both ticks and ticklegend
ax.tick_params(axis='x', colors='#5F5F5F')
ax.tick_params(axis='y', colors='#5F5F5F')

# Change the color of spines
for spine in 'bottom', 'left', 'top', 'right':
    ax.spines[spine].set_color('#9F9F9F')

# Create bar chart
bars = plt.bar(years, profits, color='#E9530D')

# Labels and title
plt.xlabel('Opciones', color='#5F5F5F', fontproperties=font2)
plt.ylabel('Coste Anual($) | 50 usuarios', color='#5F5F5F', fontproperties=font2)
plt.title('Opciones al impacto de la subida de costes de Airtable (50 Usuarios)', color='#5F5F5F', fontproperties=font2, fontsize=12)

# Format y-axis as currency
fmt = '{x:,.0f} €'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

# Calculate proportional value
proportional_value = max(profits) * 0.05  # 5% of the maximum y-value

# Add values on top of each bar
for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval - proportional_value, '{:,.0f} €'.format(yval).replace(',', '.'), ha='center', va='bottom', color='#C6C8CB', fontsize=12)

plt.savefig('impactoAirtable_50.svg', bbox_inches='tight')