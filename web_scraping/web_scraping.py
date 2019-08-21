import requests
from bs4 import BeautifulSoup
import time

URL = "https://en.wikipedia.org"
START = "/wiki/Special:Random"


def remove_brackets(paragraph):
    """Najde zavorky a text, ktery je v nich odstrani. Index najde prvni vyskyt ( a vrati hodnotu a pak index ) najde konec.
    to co je mezitim dal del. Pak chci ale aby to proslo znovu, jestli to najde dalsi (). A bide to delat tak dlouho dokud
    tam ta zavorka bude. Metody Index"""
    while True:
        try:
            paragraph = paragraph[0:paragraph.index("(")] + paragraph[paragraph.index(")")+2:-1]
        except ValueError:
            pass
        try:
            paragraph = paragraph[0:paragraph.index("[")] + paragraph[paragraph.index("]")+1:-1]
        except ValueError:
            break
    return paragraph
    
def download_page(URL, new_page):
    response = requests.get(URL + new_page)
    response.raise_for_status()
    html_text = BeautifulSoup(response.text, "html.parser")
    return html_text

def najdi_titulek(html_text):
    """Najde titulek v HTML kódu. Titulek je v elementu s identifikátorem
    `firstHeading`. Budeme předpokládat, že tento element vždycky existuje.

    Funkce vrátí titulek jako řetězec.
    """
    titulek = html_text.find(id="firstHeading").text
    print(titulek)

def najdi_odkaz(html_text):
    main_text = html_text.find(class_="mw-parser-output")
    main_text_p = main_text.find_all("p")
    for p in main_text_p:
        main_text_p_a = p.find_all("a")
        '''print(p.text)'''
        '''print(remove_brackets(str(p.text)))'''
        for hyperlink in main_text_p_a:
            '''print(hyperlink)'''
            href = hyperlink.get("href")
            if '/wiki/' in href:
                return href


def stahuj(new_page):
    visited = []
    while True:
        if new_page in visited:
            break
        visited.append(new_page)
        # 1. Stáhni stránku
        html_text = download_page(URL, new_page)
        najdi_titulek(html_text)
        new_page = najdi_odkaz(html_text)
        # 2. Napiš titulek
        # 3. Vytáhni další odkaz
        if not new_page:
            break

        time.sleep(1)

if __name__ == "__main__":
    stahuj(START)

