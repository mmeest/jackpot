<div>
  <p align="center">
    <font size="1">Pilt on loodud AI abil</font><br />
    <img src="https://github.com/mmeest/jackpot/blob/main/pic/Logo.png" height="350">
  </p>
</div>

# LotoGen
Rakendus mis genereerib varasemate loosimiste põhjal Bingo, Vikingi ja Eurojackpoti pileti. Kirjutatud Pythonis.

## Sisukord
- [Lühikirjeldus](#lühikirjeldus)
- [Failistruktuur](#failistruktuur)
- [Tehnoloogiad](#tehnoloogiad)
- [Beautiful Soup](#beautiful-soup)
- [CustomTkinter](customtkinter)
- [Alfaversioon](#alfa)
- [Beetaversioon](#beeta)
- [Võimalik edasiarendus](#võimalik-edasiarendus)

## Lühikirjeldus

Antud rakendus loeb Eesti Loto lehelt ette antud loodimiste arvu <br>
lotonumbreid (Bingo, Viking ja Eurojackpot) ning genereerib enim <br>
levinud numbrite põhjal uued loosimisnumbrid.

Kasutame oma rakenduses seniõpitut, näieks massiivid, tsüklid, <br>
tingimuslaused jne. Lisaks sellele on rakendusel kaks suuremat osa, <br>
mis on siis jagatud vastavalt kahe projektikaaslase vahel.

Autorid(progejad):
* Oliver Eesmäe
* Martin Maasik

**GUI** - ülimalt äge ja kaasatõmbav kasutajaliides.
Kasutajaliides kuvab numbrid vastavalt loto standardile:
Bingo - 5 x 5 ruudustik
Viking - 6 põhinumbrit ja 1 lisanumber
Eurojackpot - 5 põhinumbrit ja 2 lisanumbrit

**Scraper** - varasemate loosimistulemuste hankimine vastavalt ette antud numbrile
kui mitu loosimist hangitakse.

## Failistruktuur

| Fail | kirjeldus |
|-|-|
| jp_gui.py | Kasutajaliides andmete sisestamiseks/väljastamiseks |
| main.py | Põhiprogramm |
| jp_scraper.py | Eesti Loto lehelt varasemate loosimiste hankimiseks |
| jp_generator.py | Genereerib loto piletite numbrid |
| jp_random.py | Juhusliku pileti genereerimiseks |
| /pic | Kataloog projektis kasutatavate piltide jaoks |

## Tehnoloogiad

Rakendus on kirjutatud täielikult Pythonis ning kasutajakeskkonnaks
on töölauarakendus(desktop app). 

Versioonihaldusena kasutusel Git ja github.
Repo: https://github.com/mmeest/jackpot

Scraperi tarvis on valitud Beautiful Soup. GUi teegid/tööriistad projektile hetkel veel kinnitamata.

Scraperi võimalikud tööriistad:
* Beautiful Soup - https://beautiful-soup-4.readthedocs.io/en/latest/
* Scrapy - https://www.scrapy.org/
* Playwright - https://playwright.dev/
* Requests - https://pypi.org/project/requests/

GUI tarvis sai valitud Custom Tkinter

GUI võimalikud tööriistad:
* Custom Tkinter - https://customtkinter.tomschimansky.com/  https://github.com/TomSchimansky/CustomTkinter
* Tkinter - https://docs.python.org/3/library/tkinter.html
* PySide6 - https://pypi.org/project/PySide6/

## Beautiful Soup

Thonnyle tuleb paigaldada tööriistad (Tools > Manage packages):

* beautifulsoup4
* requests

Ning need importida

```
from bs4 import BeutyfulSoup
import requests
import json   # päringu vastuste tarvis
```

Kasutatud materjalid:

* Youtube Beautiful Soup 4 Tutorial #2 - Searching and Filtering https://www.youtube.com/watch?v=lOzyQgv71_4
* Beautiful Soup Documentation: https://beautiful-soup-4.readthedocs.io/en/latest/

## CustomTkinter

Thonnyle tuleb paigaldada tööriist customtkinter (Tools > Manage packages)
Ning seejärel see rakendusse importida

```
import customtkinter as ctk
```

Kasutatud materjalid:

* Tkinter ametlik lehekülg: https://customtkinter.tomschimansky.com/
* Youtube - All Customtkinter Widgets Explained FAST [Modern GUI Python Library] https://www.youtube.com/watch?v=lCmHnrX6ZHU
* Youtube - How to Create a Window in CustomTkinter - Python GUI with CustomTkinter https://www.youtube.com/watch?v=Q7_Ts5fa-Vg
* CustomTkinter - A Complete Tutorial https://dev.to/devasservice/customtkinter-a-complete-tutorial-4527
* Modern Tkinter Design With CustomTkinter - video õpetusseeria Youtubes - https://www.youtube.com/watch?v=Y01r643ckfI&list=PLfZw_tZWahjxJl81b1S-vYQwHs_9ZT77f
* Tkinter Designer - veebipõhine tkinter api kujundamine - https://visualtkinter.com/designer?target=ctk

## Alfa

Alfaversioon (Tähtaeg 11.november 2026)

Alfaversioonis peaks rakendus suutma lugeda ja genereerida Viking loto numbrid 
vastavalt varasematele loosimistele ning kuvama need kasutajaliideses.
Kasutajaliideses on loodud minimaalselt selleks vajalik: nupud, tekstiväljad.

## Beeta

Beetaversioon (Tähtaeg 16. detsember 2026)

Beeta versioon on täiendatud ka Bingo ja Eurojackpot loteriidega.

## Võimalik edasiarendus

* Random loterii piletite genereerija
* Võimalus võrrelda oma piletit viimase loosimisega(kas oleks võitnud?)
* Genereeritud numbrite salvestamine ja lugemine (CSV) faili
