"""

Juhusliku numbrikombinatsiooni genereerimiseks.

"""
import random

def juhusliku_loterii_generaator(vähim, suurim, kogus):
    """ See meetod loob juhuslikest numbritest etteantud pikkuse ja vahemikuga listi """
    vastus = []
    while len(vastus) < kogus:
        number = random.randint(vähim, suurim)
        if number not in vastus:
            vastus.append(number)
    return vastus

""" MEETODI TESTIMINE
    
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