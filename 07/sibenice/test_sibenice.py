
from sibenice_funkce import vyber_slova, kolikrat_ve_slove, vloz_pismeno, vyhodnot_prubeh_hry

def test_vyhodnot_prubeh_hry():
    assert vyhodnot_prubeh_hry('---', 4) == 'pokracuj'
    assert vyhodnot_prubeh_hry('pes', 4) == 'vyhra'
    assert vyhodnot_prubeh_hry('p-s', 10) == 'prohra'

def test_vyber_slova():
    assert vyber_slova() == 'pes' or 'balon' or 'mispule'

def test_vloz_pismeno():
    assert vloz_pismeno('---', 's', 'pes', 1) == '--s'
    assert vloz_pismeno('---', 'o', 'oko', 2) == 'o-o'

def test_kolikrat_ve_slove():
    assert kolikrat_ve_slove('o', 'oko') == 2
