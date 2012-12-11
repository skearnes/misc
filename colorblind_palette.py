def colorblind_friendly():
    """Use a colorblind-friendly palette in matplotlib.
    See http://jfly.iam.u-tokyo.ac.jp/color/#pallet and
        http://code.google.com/p/python-cudtools/
    """
    colors = [
        (230, 159,   0), #  41 orange
        ( 86, 180, 233), # 202 sky blue
        (  0, 158, 115), # 164 bluish green
        (240, 228,  66), #  56 yellow
        (  0, 114, 178), # 202 blue
        (213,  94,   0), #  27 vermillion
        (204, 121, 167), # 326 reddish purple
        (  0,   0,   0), # --- black
    ]

    # normalize
    colors = [ [ i / 255. for i in color ] for color in colors ]

    import matplotlib as mpl
    codes = [mpl.colors.rgb2hex(color) for color in colors]
    mpl.rcParams['axes.color_cycle'] = codes