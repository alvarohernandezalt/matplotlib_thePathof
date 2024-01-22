with plt.style.context('/content/kChangesMatplotLibStyles.mplstyle'):

  fig = plt.figure(figsize = (7,6.5), facecolor='#9F9F9F')
  ax = plt.axes(facecolor = '#CCCCCC')

  colors = ['#E9530D','#E8961A','#25C066','#2595E8']
  df4.T.plot(ax=ax, clip_on = False, color = colors)

  # Annotate lines
  right_text_style = dict(ha = 'left',
                          fontproperties = font2,
                          fontsize=9,
                          va = 'center')
  left_text_style = dict(ha='right',
                         fontproperties = font2,
                         fontsize=9)

  # Envolvente
  ax.text(2015 - .5, df4.iloc[0,0], 'Envolvente',
          color = colors[0],
          va = 'center',
          **left_text_style)
  ax.text(2023 + .5, df4.iloc[0,-1], f'{(df4.iloc[0,-1] - df4.iloc[0,0]) / 1e6:.1f}M€',
          color = '#C6C8CB',
          **right_text_style)

  # Fachada
  ax.text(2015 - .5, df4.iloc[1,0], 'Fachada',
          color = colors[1],
          va = 'center',
          **left_text_style)
  ax.text(2023 + .5, df4.iloc[1,-1], f'{(df4.iloc[1,-1] - df4.iloc[1,0]) / 1e6:.1f}M€',
          color = '#C6C8CB',
          **right_text_style)

  # Patrimonio
  ax.text(2015 - .5, df4.iloc[2,0], 'Patrimonio',
          color = colors[2],
          va = 'center',
          **left_text_style)
  ax.text(2023 + .5, df4.iloc[2,-1], f'{(df4.iloc[2,-1] - df4.iloc[2,0]) / 1e6:.1f}M€',
          color = '#C6C8CB',
          **right_text_style)

  # Rehabilitacion
  ax.text(2015 - .5, df4.iloc[3,0], 'Rehabilitacion',
          color = colors[3],
          va = 'center',
          **left_text_style)
  ax.text(2023 + .5, df4.iloc[3,-1], f'{(df4.iloc[3,-1] - df4.iloc[3,0]) / 1e6:.1f}M€',
          color = '#C6C8CB',
          **right_text_style)

  t='PRESUPUESTOS KALAM'
  s='Evolución de cantidades presupuestadas por tipologías de 2015-2023. \nEn la derecha el diferencial entre 2015 y 2023'
  title_and_subtitle(t,s, pad = 0.02, fig = fig, ax = ax)

  yticks = range(0, 120000000, 20000000)
  ax.set_yticks(yticks)
  ax.set_ylim(0, 120000000)
  ax.tick_params(axis='y', colors='#9F9F9F')
  for tick in yticks:
    label = '{} M€'.format(tick/1e6)
    ax.text(2019, tick +0.02, label,
            va='bottom',
            ha='center',
            color='#9F9F9F')
    
  ax.legend().set_visible(False)
  ax.yaxis.grid(True, color='#9F9F9F', linestyle='dashed', linewidth = .5)

