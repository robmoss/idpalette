import idpalette as idp
import pytest


palette_names = idp._palettes().keys()
invalid_names = ['acef', 'idddu', 'idm', 'lshtm']


@pytest.mark.parametrize('name', invalid_names)
def test_invalid_palette_name(name):
    with pytest.raises(ValueError):
        idp.idpalette(name)


@pytest.mark.parametrize('name', palette_names)
def test_invalid_number_negative(name):
    with pytest.raises(ValueError):
        idp.idpalette(name, n=-1)


@pytest.mark.parametrize('name', palette_names)
def test_invalid_number_type(name):
    with pytest.raises(TypeError):
        idp.idpalette(name, n='1')
