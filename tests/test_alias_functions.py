import idpalette as idp
import pytest


@pytest.mark.parametrize('n', range(2, 12))
def test_acefa(n):
    assert idp.acefa(n) == idp.idpalette('acefa', n)


@pytest.mark.parametrize('n', range(2, 12))
def test_iddu(n):
    assert idp.iddu(n) == idp.idpalette('iddu', n)


@pytest.mark.parametrize('n', range(2, 12))
def test_idem(n):
    assert idp.idem(n) == idp.idpalette('idem', n)
