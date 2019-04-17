
from sibenice_funkce import vyber_slova, je_pismeno_ve_slove, vloz_pismeno, vyhodnot_prubeh_hry

def test_vyhodnot_prubeh_hry():
    assert vyhodnot_prubeh_hry('---', 4) == 'pokracuj'
    assert vyhodnot_prubeh_hry('pes', 4) == 'vyhra'
    assert vyhodnot_prubeh_hry('p-s', 10) == 'prohra'

def test_vyber_slova():
    assert vyber_slova() == 'pes' or 'balon' or 'mispule'

def test_je_pismeno_ve_slove():
    assert je_pismeno_ve_slove('s', 'pes') == True
    assert je_pismeno_ve_slove('l', 'pes') == False

def test_vloz_pismeno():
    assert vloz_pismeno('---', 's', 'pes') == '--s'