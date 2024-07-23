import idpalette as idp
import matplotlib.colors as mpc
import pytest


palette_names = idp._palettes().keys()


@pytest.mark.parametrize('name', palette_names)
@pytest.mark.parametrize('n', range(2, 12))
def test_colour_maps(name, n):
    source_colours = idp.idpalette(name, n)
    assert len(source_colours) == n
    cmap = idp.mpl_colour_map(name, n)
    assert cmap.N == n
    cmap_hex = [mpc.to_hex(rgba) for rgba in cmap(range(n))]
    assert len(cmap_hex) == n
    for source, cmap in zip(source_colours, cmap_hex):
        assert source.lower() == cmap.lower()
