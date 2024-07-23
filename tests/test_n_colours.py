import idpalette as idp
import pytest


palette_names = idp._palettes().keys()


@pytest.mark.parametrize('name', palette_names)
@pytest.mark.parametrize('n', range(1, 12))
def test_gradient_bounds_equal_palette_bounds(name, n):
    # Each palette contains at least 4 colours.
    colours = idp.idpalette(name)
    assert len(colours) > 3
    # We should always get the requested number of colours.
    n_colours = idp.idpalette(name, n)
    assert len(n_colours) == n
    if n > len(colours):
        # If we ask for more colours than are defined, we should receive a
        # gradient that begins and ends with the same colours as the base
        # palette.
        assert n_colours[0] == colours[0]
        assert n_colours[-1] == colours[-1]
    else:
        # Otherwise, we should receive the first N colours from the base
        # palette.
        assert n_colours == colours[:n]


@pytest.mark.parametrize('name', palette_names)
def test_n_equals_zero(name):
    assert len(idp.idpalette(name, 0)) == 0
