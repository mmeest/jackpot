<div>
  <p align="center">
    <font size="1">Pilt on loodud AI abil</font><br />
    <img src="https://github.com/mmeest/jackpot/blob/main/pic/Logo.png" height="350">
  </p>
</div>

# LotoGen
Rakendus mis genereerib varasemate loosimiste põhjal Bingo, Vikingi ja Eurojackpoti pileti. Kirjutatud Pythonis.

## Sisukord
- [Lühikirjeldus](#luhikirjeldus)
- [Failistruktuur](#failistruktuur)
- [Alfaversioon](#alfa)
- [Beetaversioon](#beeta)
- [Võimalik edasiarendus](#võimalik-edasiarendus)

## Lühikirjeldus

Antud rakendus loeb Eesti Loto lehelt ette antud loodimiste arvu lotonumbreid
(Bingo, Viking ja Eurojackpot) ning genereerib enim levinud numbrite põhjal uued loosimisnumbrid.

Kasutame oma rakenduses seniõpitut, näieks massiivid, tsüklid, tingimuslaused jne.
Lisaks sellele on rakendusel kaks suuremat osa, mis on siis jagatud vastavalt kahe
projektikaaslase vahel.

GUI - ülimalt äge ja kaasatõmbav kasutajaliides.
Kasutajaliides kuvab numbrid vastavalt loto standardile:
Bingo - 5 x 5 ruudustik
Viking - 6 põhinumbrit ja 1 lisanumber
Eurojackpot - 5 põhinumbrit ja 2 lisanumbrit

Scraper - varasemate loosimistulemuste hankimine vastavalt ette antud numbrile
kui mitu loosimist hangitakse.

## Failistruktuur

| Fail | kirjeldus |
|-|-|
| gui.py | Kasutajaliides andmete sisestamiseks/väljastamiseks |
| main.py | Põhiprogramm |
| scraper.py | Eesti Loto lehelt varasemate loosimiste hankimiseks |
| generator.py | Genereerib loto piletite numbrid |
| random.py | Juhusliku pileti genereerimiseks |

## Alfa

Alfaversioon (11.november)

Alfaversioonis peaks rakendus suutma lugeda ja genereerida Viking loto numbrid 
vastavalt varasematele loosimistele ning kuvama need kasutajaliideses.
Kasutajaliideses on loodud minimaalselt selleks vajalik: nupud, tekstiväljad.

## Beeta

Beeta versioon on täiendatud ka Bingo ja Eurojackpot loteriidega.

## Võimalik edasiarendus

* Random loterii piletite genereerija
* Võimalus võrrelda oma piletit viimase loosimisega(kas oleks võitnud?)
* Genereeritud numbrite salvestamine ja lugemine (CSV) faili
