"""
Genereeritud piletite salvestamine CSV-faili
"""
import csv
from datetime import *
from pathlib import *

FAIL = Path(__file__).parent/'piletid.csv'

def salvesta_pilet(loto, liik, põhinumbrid, lisanumbrid):
    ''' Lisab ühe pileti faili piletid.csv ja antud fail luuakse, kui seda veel pole'''
    uus_fail = not FAIL.exists()
    with open(FAIL, 'a', newline='', encoding='utf-8-sig') as f:
        kirjutaja = csv.writer(f, delimiter=';')
        if uus_fail:
            kirjutaja.writerow(['Aeg', 'Loto', 'Liik', 'Põhinumbrid', 'Lisanumbrid'])
        kirjutaja.writerow([
            datetime.now().strftime('%H:%M:%S %d-%m-%Y'),
            loto,
            liik,
            ' '.join(map(str, põhinumbrid)),
            ' '.join(map(str, lisanumbrid)),
        ])