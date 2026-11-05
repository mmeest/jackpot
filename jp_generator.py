"""

Lotonumbrite genereerija, sisendandmetena kasutab scraperit ja väljastab tulemuse GUIsse

"""

from jp_scraper import *
from jp_random import juhusliku_loterii_generaator
from jp_gui import *

# loosimiste_arv = 1

def enim_esinev_nr(sisend):
    """ Meetod mis otsib tulemustest einm levinud numbri """
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
            
def täida_tulemuste_list(list, kogus):
    """ Käib läbi etteantud numbri loosimisi ja tagastab kõigi nende loosimiste numbrite järjendi """
    vastus = []
    number = None
    for i in range(kogus):
        number = enim_esinev_nr(list)[0]
        vastus.append(number)
        eemalda_element_listist(list, number)
    return vastus

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

def tulemused(loosimiste_arv, app):
    app.text1.delete(0.0, 'end')
    app.text2.delete(0.0, 'end')
    app.text3.delete(0.0, 'end')
    app.text4.delete(0.0, 'end')
    app.text5.delete(0.0, 'end')
    app.text6.delete(0.0, 'end')
    app.text7.delete(0.0, 'end')
    
    """ Järgnevlat kogume kokku valitud arvu loosimiste numbreid erinevatelt lotodelt: """
    v_põhi = tulemuste_koguja(loosimiste_arv, viking_id, "põhinumbrid")
    v_lisa = tulemuste_koguja(loosimiste_arv, viking_id, "lisanumbrid")
    e_põhi = tulemuste_koguja(loosimiste_arv, eurojackpot_id, "põhinumbrid")
    e_lisa = tulemuste_koguja(loosimiste_arv, eurojackpot_id, "lisanumbrid")
    bingo_alg = tulemuste_koguja(loosimiste_arv, bingo_id)

    bingo_read = tükelda_bingo(bingo_alg)
    
    """ Järgnevalt genereerime uue pileti numbrid kõigile lotodele: """
    viking_põhi = täida_tulemuste_list(v_põhi, 6)
    viking_lisa = täida_tulemuste_list(v_lisa, 1)
    euro_põhi = täida_tulemuste_list(e_põhi, 5)
    euro_lisa = täida_tulemuste_list(e_lisa, 2)
    bingo_B = täida_tulemuste_list(bingo_read[0], 5)
    bingo_I = täida_tulemuste_list(bingo_read[1], 5)
    bingo_N = täida_tulemuste_list(bingo_read[2], 5)
    bingo_G = täida_tulemuste_list(bingo_read[3], 5)
    bingo_O = täida_tulemuste_list(bingo_read[4], 5)
    
    """ Järgnevlat talletame viimase loosimise numbrid erinevatelt lotodelt: """
    viimane_v_põhi = tulemuste_koguja(1, viking_id, "põhinumbrid")
    viimane_v_lisa = tulemuste_koguja(1, viking_id, "lisanumbrid")
    viimane_e_põhi = tulemuste_koguja(1, eurojackpot_id, "põhinumbrid")
    viimane_e_lisa = tulemuste_koguja(1, eurojackpot_id, "lisanumbrid")
    viimane_bingo_alg = tulemuste_koguja(1, bingo_id)
     
    app.text1.insert(tk.END, viking_põhi[0])
    app.text2.insert(tk.END, viking_põhi[1])
    app.text3.insert(tk.END, viking_põhi[2])
    app.text4.insert(tk.END, viking_põhi[3])
    app.text5.insert(tk.END, viking_põhi[4])
    app.text6.insert(tk.END, viking_põhi[5])
    app.text7.insert(tk.END, viking_lisa[0])

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
