from random import randrange
from ai import tah_pocitace_bez_strategie, tah_pocitace_strategie_vlevo, tah_pocitace_strategie_vpravo, tah, tah_pocitace
from piskvorky_strategie import vyhodnot, tah_hrace
import pytest

def test_vyhodnot():
    assert vyhodnot("xxx-----------------") == "x"
def test_vyhodnot2():
    assert vyhodnot("oxoxoxoxoxoxoxoxoxox") == "!"
def test_tah():
    assert tah("--------------------", 5, 'o') == '-----o--------------'
def test_tah_pocitace_bez_strategie():
    with pytest.raises(ValueError):
        tah_pocitace_bez_strategie('oxoxoxoxoxoxoxoxoxox', 'o')

def test_tah_pocitace_strategie_vlevo():
    assert tah_pocitace_strategie_vlevo('-oox----------------', 'o', '-oo') == 'ooox----------------'
def test_tah_pocitace_strategie_vlevo2():
    with pytest.raises(ValueError):
        tah_pocitace_strategie_vlevo('oxoxoxoxoxoxoxoxoxox', 'o', '-oo')

def test_tah_pocitace_strategie_vpravo():
    assert tah_pocitace_strategie_vpravo('xoo-----------------', 'o', 'oo-') == 'xooo----------------'
def test_tah_pocitace_strategie_vpravo2():
    with pytest.raises(ValueError):
        tah_pocitace_strategie_vpravo('oxoxoxoxoxoxoxoxoxox', 'o', 'oo-')

def test_tah_pocitace():
    assert tah_pocitace('-----x---oo---------', 'o') == '-----x--ooo---------'





