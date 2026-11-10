'''
Enim esinenud numbrite statistika.
'''
from collections import Counter
from jp_scraper import tulemuste_koguja, viking_id

def sagedasemad(loosimiste_arv, mitu=10):
    ''' Tagastab listi (number, mitu_korda) enim esinenud Vikingi põhinumbritest '''
    numbrid = tulemuste_koguja(loosimiste_arv, viking_id, 'põhinumbrid')
    return Counter(numbrid).most_common(mitu)