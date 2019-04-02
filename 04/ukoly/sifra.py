plaintext = input('Zadej text k zasifrovani: ')
key = int(input('Zadej cislo, ktere text zasifruje: '))
seznam_plaintext = list(plaintext) #vytvoreni seznamu znaku
seznam_ciphertext = []
seznam_ciphertext_cislo = []
seznam_plaintext_cisla = []

#prevedu vsechny znaky v seznamu na cisla. Vytvorim seznam puvodniho textu v cislech
for znak in seznam_plaintext:
    cislo = ord(znak)
    seznam_plaintext_cisla.append(cislo)


#zmenim pismena o key, ostatni znaky necham nezmenene a pridam do seznamu seznam_ciphertext_cislo
for cislo in seznam_plaintext_cisla:
    if cislo >= 65 and cislo <= 90: # pro velka pismena abecedy (65-A...90=Z)
        cislo_key = cislo + key
        posun_velka = cislo_key % 90 # hodi zbytek celociselneho deleni 90. 90 proto, protoze je to cislo pro posledni znak abecedy Z
        if cislo_key <= 90:  #to znamena, ze posun probehne v ramci jedne abecedy, neprechazi zpatky pres A
            cipher_cislo = cislo_key
        else:
            cipher_cislo = 64 + posun_velka #pokud se jde znovu pres A. K 64 (A-1) pridam zbytek celociselneho deleni
        seznam_ciphertext_cislo.append(cipher_cislo)
    elif cislo >= 97 and cislo <= 122: # pro pismena male abecedy (a-97 - z-122), ostatni postup, stejny jak pro velka pismena
        cislo_key = cislo + key
        posun_mala = cislo_key % 122
        if cislo_key <= 122:
            cipher_cislo = cislo_key
        else:
            cipher_cislo = 96 + posun_mala
        seznam_ciphertext_cislo.append(cipher_cislo)
    else:
        seznam_ciphertext_cislo.append(cislo) #ostatni znaky prida do seznamu nezmenene

#seznam_cifertext_cislo na seznam_cifretext
for cipher_cisla in seznam_ciphertext_cislo:
    cipher_znak = chr(cipher_cisla)
    seznam_ciphertext.append(cipher_znak)


#seznam_cifretext prevedu pomoci join zpatky na retezec a ten vytisknu
ciphertext = ''.join(seznam_ciphertext)

print('Tvuj puvodni text: ' + plaintext)
print('Tvuj zasifrovany text: ' + ciphertext)