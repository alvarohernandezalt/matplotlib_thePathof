from matplotlib.font_manager import FontProperties

def set_font_properties(font, family, style, variant, weight, stretch, size):
    """
    Set font properties.
    
    Parameters
    ----------
        font : FontProperties
        Font properties.            
        family : str
        Font family.
        style : str
        Font style.
        variant : str
        Font variant.
        weight : str or int
        Font weight.    
        stretch : str
        Font stretch.
        size : int
        Font size.
        Returns
        -------
        dict
        Font properties.
            
    """
    font.set_family(family)
    font.set_style(style)
    font.set_variant(variant)
    font.set_weight(weight)
    font.set_stretch(stretch)
    font.set_size(size)

    return {
        'name': font.get_name(),
        'family': font.get_family(),
        'style': font.get_style(),
        'variant': font.get_variant(),
        'weight': font.get_weight(),
        'stretch': font.get_stretch(),
        'size': font.get_size(),
    }

