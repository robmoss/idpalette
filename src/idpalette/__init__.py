"""
Colour palettes based on the ACEFA, IDDU, and IDEM logos.
"""

__all__ = ['idpalette', 'acefa', 'idem', 'iddu', 'mpl_colour_map']


def _palettes():
    """
    Return a dictionary that maps palette names to lists of colours
    (represented as hexadecimal strings).
    """
    acefa_base = ['#262261', '#247aa7', '#84b5cc', '#ddebf0']
    acefa_extra = ['#eb008b']
    idem_base = ['#262261', '#1d4d79', '#178793', '#00a79e']
    idem_extra = ['#58b4ac', '#acd3d0', '#e6e7e8']
    iddu_base = ['#262261', '#27aae1', '#662d91', '#ee3a89']
    iddu_extra = ['#d0d2d3']
    return {
        'acefa_official': acefa_base,
        'acefa': acefa_base + acefa_extra,
        'idem_official': idem_base,
        'idem': idem_base + idem_extra,
        'iddu_official': iddu_base,
        'iddu': iddu_base + iddu_extra,
    }


def idpalette(name, n=None):
    """
    Return a list of colours from the specified palette, represented as
    hexadecimal strings.

    :param name: The palette name, must be one of ``'acefa_official'``,
        ``'acefa'``, ``'idem_official'``, ``'idem'``, ``'iddu_official'``,
        ``'iddu'``.
    :param n: The number of colours to return. By default, all colours in the
        palette are returned. If ``n`` is larger than the number of colours in
        the palette, intermediate colours will be interpolated.
    """
    try:
        colours = _palettes()[name]
    except KeyError as e:  # UNCOV
        raise ValueError(f'Invalid palette name {name}') from e
    if n is None:
        return colours
    elif not isinstance(n, int):
        raise TypeError(f'n must be None or an integer, not {type(n)}')
    elif n < 0:
        raise ValueError('n must be non-negative')
    elif n <= len(colours):
        return colours[:n]
    else:
        from mizani.palettes import gradient_n_pal

        # Alternatively, np.linspace(0, 1, num=n)
        xs = [x / (n - 1) for x in range(n)]
        return gradient_n_pal(colours)(xs)
        raise NotImplementedError()


def acefa(n=None):
    """
    An alias for ``idpalette('acefa', n=None)``.
    """
    return idpalette('acefa', n=n)


def idem(n=None):
    """
    An alias for ``idpalette('idem', n=None)``.
    """
    return idpalette('idem', n=n)


def iddu(n=None):
    """
    An alias for ``idpalette('iddu', n=None)``.
    """
    return idpalette('iddu', n=n)


def mpl_colour_map(name, n=None):
    """
    Return a list of colours from the specified palette, represented as a
    matplotlib Colormap instance.

    :param name: The palette name, must be one of ``'acefa_official'``,
        ``'acefa'``, ``'idem_official'``, ``'idem'``, ``'iddu_official'``,
        ``'iddu'``.
    :param n: The number of colours to return. By default, all colours in the
        palette are returned. If ``n`` is larger than the number of colours in
        the palette, intermediate colours will be interpolated.
    Return a
    """
    import matplotlib.colors as mpc

    colours = idpalette(name, n=n)
    n = len(colours)
    rgba = [mpc.to_rgba(c) for c in colours]
    return mpc.LinearSegmentedColormap.from_list(name, rgba, N=n)
