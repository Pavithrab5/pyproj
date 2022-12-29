import pytest

@pytest.mark.parametrize("a,b,c",[(1,2,3),(6,2,8)])
def test_functionAdd(a,b,c):
    assert a+b==c


@pytest.mark.parametrize("a,b,c",[(1,2,3),(4,2,6)])
def test_functionSub(a,b,c):
    assert c-b==a


@pytest.mark.parametrize("a,b,c",[("pavi","banda","pavibanda")])
def test_functionConcat(a,b,c):
    assert a+b==c
