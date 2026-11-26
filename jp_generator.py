"""

Lotonumbrite genereerija, sisendandmetena kasutab scraperit ja väljastab tulemuse GUIsse

"""

from jp_scraper import *
from jp_random import juhusliku_loterii_generaator, BINGO_VAHEMIKUD
from collections import Counter
from random import randint

# loosimiste_arv = 1

def enim_esinev_nr(sisend):
    """ Meetod mis otsib tulemustest enim levinud numbri """
    max_sagedus = 0
    max_nr = None
    
    for nr in sisend:
        sagedus = sisend.count(nr)
        if sagedus > max_sagedus:
            max_sagedus = sagedus
            max_nr = nr
    return (max_nr, max_sagedus)

def eemalda_element_listist(sisend, element):
    """ Meetod mis eemaldab listist valitud kindla(d) elemendi(d) """
    for el in sisend:
        if el == element:
            sisend.remove(el)
            
def täida_tulemuste_list(sisend, kogus, vähim, suurim):
    """ Tagastab 'kogus' enim esinenud erinevat numbrit """
    numbrid = [arv for arv, sagedus in Counter(sisend).most_common(kogus)]
    return täienda(numbrid, kogus, vähim, suurim)

def tükelda_bingo(sisend):
    """ Meetod mis jaotab BINGO loosimise numbrid veergude kaupa(1-15, 16-30 jne.) """
    vastus = [[],[],[],[],[]]
    for el in sisend:
        if el < 16:
            vastus[0].append(el)
        elif el < 31:
            vastus[1].append(el)
        elif el < 46:
            vastus[2].append(el)
        elif el < 61:
            vastus[3].append(el)
        else:
            vastus[4].append(el)
    return vastus            

#vastus = tulemuste_koguja(loosimiste_arv, viking_id, "põhinumbrid")
#vastus_2 = tulemuste_koguja(loosimiste_arv, bingo_id)

#print(vastus)
#print(vastus_2)

#print(enim_esinev_nr(vastus))
#print(enim_esinev_nr(vastus_2))

#print(enim_esinev_nr(tulemuste_koguja(loosimiste_arv, bingo_id)))
_sagedused = None

def hangi_sagedused():
    return _sagedused

def _jäta_sagedused_meelde(*nimekirjad):
    global _sagedused
    loendur = Counter()
    for nimekiri in nimekirjad:
        for nr in nimekiri:
            loendur[int(nr)] += 1
    _sagedused = [loendur.get(n, 0) for n in range(1, 76)]

def täienda(numbrid, kogus, vähim, suurim):
    '''Kui statistikast jääb nt numbreid puudu, siis see lisab samas vahemikus arvu'''
    while len(numbrid) < kogus:
        nr = randint(vähim, suurim)
        if nr not in numbrid:
            numbrid.append(nr)
    return numbrid

def tulemused(loosimiste_arv):
    
    """ Järgnevalt kogume kokku valitud arvu loosimiste numbreid erinevatelt lotodelt: """
    v_põhi = tulemuste_koguja(loosimiste_arv, viking_id, "põhinumbrid")
    v_lisa = tulemuste_koguja(loosimiste_arv, viking_id, "lisanumbrid")
    e_põhi = tulemuste_koguja(loosimiste_arv, eurojackpot_id, "põhinumbrid")
    e_lisa = tulemuste_koguja(loosimiste_arv, eurojackpot_id, "lisanumbrid")
    bingo_alg = tulemuste_koguja(loosimiste_arv, bingo_id)
    _jäta_sagedused_meelde(v_põhi, v_lisa, e_põhi, e_lisa, bingo_alg)

    bingo_read = tükelda_bingo(bingo_alg)
    
    """ Järgnevalt genereerime uue pileti numbrid kõigile lotodele: """
    viking_põhi = täida_tulemuste_list(v_põhi, 6, 1, 48)
    viking_lisa = täida_tulemuste_list(v_lisa, 1, 1, 5)
    euro_põhi = täida_tulemuste_list(e_põhi, 5, 1, 50)
    euro_lisa = täida_tulemuste_list(e_lisa, 2, 1, 12)
    bingo_B = täida_tulemuste_list(bingo_read[0], 5, 1, 15)
    bingo_I = täida_tulemuste_list(bingo_read[1], 5, 16, 30)
    bingo_N = täida_tulemuste_list(bingo_read[2], 5, 31, 45)
    bingo_G = täida_tulemuste_list(bingo_read[3], 5, 46, 60)
    bingo_O = täida_tulemuste_list(bingo_read[4], 5, 61, 75)
    
    '''Paneme numbrid vastavatesse väljadesse'''
    viking = viking_põhi + viking_lisa
    euro = euro_põhi + euro_lisa
    bingo =  bingo_B + bingo_I + bingo_N + bingo_G + bingo_O
    
    return viking, euro, bingo 
    
    """ Järgnevlat talletame viimase loosimise numbrid erinevatelt lotodelt: """
    '''viimane_v_põhi = tulemuste_koguja(1, viking_id, "põhinumbrid")
    viimane_v_lisa = tulemuste_koguja(1, viking_id, "lisanumbrid")
    viimane_e_põhi = tulemuste_koguja(1, eurojackpot_id, "põhinumbrid")
    viimane_e_lisa = tulemuste_koguja(1, eurojackpot_id, "lisanumbrid")
    viimane_bingo_alg = tulemuste_koguja(1, bingo_id)
     
    app.text1.insert('end', viking_põhi[0])
    app.text2.insert('end', viking_põhi[1])
    app.text3.insert('end', viking_põhi[2])
    app.text4.insert('end', viking_põhi[3])
    app.text5.insert('end', viking_põhi[4])
    app.text6.insert('end', viking_põhi[5])
    app.text7.insert('end', viking_lisa[0])'''

#print(v_põhi)
#print(v_lisa)
#print(e_põhi)
#print(e_lisa)
#print(bingo_alg)
#print(bingo_read)

""" Prindime välja saadud tulemused: """
"""
print(f"Viking loto põhinumbrid on: {viking_põhi}")
print(f"Viking loto lisanumbrid on: {viking_lisa}")
print(f"Eurojcakpot põhinumbrid on: {euro_põhi}")
print(f"Eurojackpot lisanumbrid on: {euro_lisa}")
print(f"Bingo loto B-veeru numbrid on: {bingo_B}")
print(f"Bingo loto I-veeru numbrid on: {bingo_I}")
print(f"Bingo loto N-veeru numbrid on: {bingo_N}")
print(f"Bingo loto G-veeru numbrid on: {bingo_G}")
print(f"Bingo loto O-veeru numbrid on: {bingo_O}")
"""

""" Järgnevalt genereerime juhuslikud lotonumbrid """
"""
v_rand_põhi = juhusliku_loterii_generaator(1, 48, 6)
v_rand_lisa = juhusliku_loterii_generaator(1, 5, 1)
e_rand_põhi = juhusliku_loterii_generaator(1, 50, 5)
e_rand_lisa = juhusliku_loterii_generaator(1, 12, 2)
b_rand = []
b_rand.append(juhusliku_loterii_generaator(1, 15, 5))
b_rand.append(juhusliku_loterii_generaator(16, 30, 5))
b_rand.append(juhusliku_loterii_generaator(31, 45, 5))
b_rand.append(juhusliku_loterii_generaator(46, 60, 5))
b_rand.append(juhusliku_loterii_generaator(61, 75, 5))

print(v_rand_põhi)
print(v_rand_lisa)
print(e_rand_põhi)
print(e_rand_lisa)
print(b_rand)
"""
