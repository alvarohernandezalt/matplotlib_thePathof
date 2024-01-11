def title_and_subtitle(title, subtitle = '', pad = 0.1, fig = None, ax = None):
    """
    This function adds a centered title and subtitle to a plot.
    Four parameters: title, subtitle, pad, and fig, ax.
    1. title. Required parameter
    2. subtitle. By default empty (optional)
    3. pad. By default 0.1 (optional)
          It controls the padding between texts
    4. fig. By Default None (optional)
    5. ax.  By Default None (optional)

    If ax = None -> ax = plt.gca
    The gca function stands for "Get Current Axes". 
    It returns the current Axes instance on the current figure.
    If no current figure exists, a new one is created with a single subplot.       
  
    If fig = None -> fig = plt.gcf
    The gcf function stands for "Get Current Figure". 
    It returns the current Axes instance on the current figure.
    If no current figure exists, a new one is created with a single subplot.

    """
    if ax == None:
        ax = plt.gca()
    if fig == None:
        fig = plt.gcf()
    fig.canvas.draw()

    top_of_figure = 1 #axes coordinates

    # Calculate the position of the top of the frist x-axis tick label in axes space
    # Useful for positioning other elements on the plot relative to the ticks labels
    tick0 = ax.get_xticklabels()[0]
    top_of_ticklabels = tick0.get_window_extent().transformed(ax.transAxes.inverted()).y1
    top_of_figure = max([top_of_ticklabels, top_of_figure])

    # Create subtitle
    if subtitle:
        subt = ax.text(0.5, top_of_figure + pad,
                   s = subtitle,
                   ha='center',
                   va='bottom',
                   fontproperties=font2,
                   size='11',
                   transform=ax.transAxes)
        # update top_of_figure to top of subtitle
        top_of_figure = subt.get_window_extent().transformed(ax.transAxes.inverted()).y1

    # Create title
    ax.text(0.5, top_of_figure + pad,
            s = title,
            ha='center',
            va='bottom',
            fontproperties=font2,
            size='14',
            transform=ax.transAxes)
    