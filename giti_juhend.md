# Giti lühiõpetus 

## 1. Giti paigaldamine

Laadi Git alla ja paigalda:
https://git-scm.com/

## 2. Giti versiooni kontrollimine

Vajuta `Win + R`, kirjuta `cmd` ja vajuta Enter.

Kontrolli, kas Git on olemas:

```bash
git --version
```

Kui kuvatakse Giti versioon, on paigaldamine õnnestunud.

## 3. Repositooriumi arvutisse laadimine

Kasutame näiteks seda repositooriumi:

https://github.com/mmeest/jackpot.git

Giti on mugav kasutada käsurealt (Command Prompt ehk CMD).

Selleks:
1. Ava Windows Exploreris kataloog, kuhu soovid repositooriumi laadida.
2. Kliki kataloogi aadressireal.
3. Kirjuta `cmd` ja vajuta Enter.
4. Avanenud käsureale kirjuta:

```bash
git clone https://github.com/mmeest/jackpot.git
```

Nüüd laaditakse repositoorium koos Giti ajalooga sinu arvutisse.

Liigu loodud projekti kataloogi:

```bash
cd jackpot
```

## 4. Uue arendusharu (branch) loomine

Kui soovid projektis midagi muuta, loo kõigepealt uus arendusharu.

Enne uue haru loomist uuenda olemasolevat `main` haru:

```bash
git checkout main
git pull
```

Olemasolevate kohalike harude kontrollimine:

```bash
git branch
```

Kuvab kõik kohalikud harud ja näitab tärniga (`*`) haru, millel sa hetkel asud.

Näiteks loome uue arendusharu nimega `tulemuste_kontrollimine`.

```bash
git checkout -b tulemuste_kontrollimine
```

Selle käsuga luuakse uus haru ja Git lülitub automaatselt sellele.

Haru nimes ei tohi kasutada tühikuid.

## 5. Muudatuste kontrollimine

Kui oled oma arendusharus midagi muutnud ja soovid näha, milliseid faile muudeti, kasuta:

```bash
git status
```

Git kuvab muudetud ja lisatud failid ning näitab, millised muudatused ootavad lisamist järgmisesse commit'i.

## 6. Muudatuste ettevalmistamine üleslaadimiseks

Kui oled oma arendusega rahul, tuleb muudatused esmalt lisada commit'i jaoks.

Selleks on kaks võimalust.

**A. Lisad ühe konkreetse faili:**

```bash
git add minufail.py
```

**B. Lisad kõik muudetud ja uued failid:**

```bash
git add .
```

Pärast seda saad kontrollida hetkeseisu:

```bash
git status
```

Lisatud failid kuvatakse tavaliselt roheliselt. See tähendab, et need on järgmise commit'i jaoks ette valmistatud, kuid pole veel Git'i ajalukku salvestatud.

## 7. Muudatuste commit'imine

Salvestame muudatused Git'i ajalukku.

Lisada tuleb ka lühike kirjeldus muudatuste kohta:

```bash
git commit -m "Muutsin tulemuste kontrolli kiiremaks"
```

Pärast seda võid kontrollida hetkeseisu:

```bash
git status
```

Kui kõik muudatused said commit'itud, kuvatakse tavaliselt teade:

`nothing to commit, working tree clean`

See tähendab, et kõik muudatused on kohalikult salvestatud.

## 8. Muudatuste üleslaadimine GitHubi

Laadime oma arendusharu GitHubi:

```bash
git push -u origin tulemuste_kontrollimine
```

See käsk:
- Laadib arendusharu GitHubi.
- Loob GitHubis vastava haru, kui seda veel pole.
- Seob kohaliku haru GitHubi haruga (upstream).

Edaspidi piisab samas harus muudatuste üleslaadimiseks käsust:

```bash
git push
```

## 9. Pull Requesti (PR) loomine

Pärast arendusharu üleslaadimist tuleb GitHubis luua Pull Request.

Pull Requesti abil saad teha ettepaneku liita oma arendusharu (`tulemuste_kontrollimine`) põhiharuga (`main`).

Kui muudatused on üle vaadatud ja kõik on korras, liidetakse arendusharu `main` haruga.

NB! Pull Requesti ei looda automaatselt käsuga `git push`. See tuleb GitHubis eraldi luua.

## 10. Olemasolevate harude vahel liikumine

Harude vahel liikumiseks kasuta käsku:

```bash
git checkout HARU_NIMI
```

Näiteks põhiharule liikumiseks:

```bash
git checkout main
```

Uue haru loomisel tasub alati kõigepealt liikuda `main` harusse ja laadida alla värskeim kood:

```bash
git checkout main
git pull
```

Seejärel loo uus arendusharu:

```bash
git checkout -b uus_arendus
```

---

## Olulisemad Giti käsud kokkuvõtlikult

| Käsk | Milleks kasutatakse |
|---|---|
| `git clone URL` | Repositooriumi arvutisse laadimine |
| `git pull` | Uusimate muudatuste allalaadimine |
| `git branch` | Kohalike harude vaatamine |
| `git checkout main` | Haru vahetamine |
| `git checkout -b nimi` | Uue haru loomine |
| `git status` | Muudatuste kontrollimine |
| `git add .` | Kõigi muudatuste lisamine commit'i jaoks |
| `git commit -m "kirjeldus"` | Muudatuste salvestamine Git'i ajalukku |
| `git push` | Muudatuste üleslaadimine GitHubi |
