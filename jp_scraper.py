"""

Fail milles toimub scrape'mine ehk veebist info hankimine.
Selleks kasutame request'i ja BeautyfulSoup'i.

Numbrid salvestatakse viite erinevasse listi: Vikingi põhinumbrid, Vikingi lisanumbrid,
Eurojackpot põhinumbrid, Eurojackpot lisanumbrid, Bingo numbrid.

Meetoditele ja muutujatele on lisatud kommentaarid.

NB! Faili sisu võib küll kole välja näha, kuna siia on alles jäätud ka arendusprotsessis
kasutusel olnud pärandkood, selleks, et paremini kogu protsessist pilti luua.

"""

from bs4 import BeautifulSoup
import requests
import json

viking_id = "f74aa656-510d-4356-97d7-8009793e9c1e"
eurojackpot_id = "4c456d40-94b4-4991-ba2b-098a93720357"
bingo_id = "a5af0a39-e911-40e8-a2b1-674c4d46d351"
# keno_id = "ad6ebfa2-d95f-4a37-aa3c-6c04fd5925ea"		# <- Reserveeritud KENO loto arendusele
api_url = "https://api.eestiloto.ee/api/v1/draws"

def küsi_loosimisi(parameetrid):
    """ Abifunktsioon, et koondada korduv kood kokku """
    response = requests.get(api_url, params=parameetrid, timeout=15)
    response.raise_for_status()
    data = response.json()
    return data.get("content", [])

def viimase_loosimise_nr(mängu_id):
    """ Loosimise IDd on vaja päringus kasutatava URLi koostamiseks """
    params = {
        "status": "DRAW_COMPLETED",
        "page": 0,
        "size": 1,
        "sort": "dateTime:desc",
        "gameId": mängu_id
        }    
    loosimised = küsi_loosimisi(params)
    if not loosimised:
        return None										# Selleks et rakendus ei kukuks kokku tüha vastuse puhul
    return loosimised[0]["number"]

"""   PÄRANDMEETOD MILLEGA SAI ALGSELT OTSITUD SUVALISE LOOSIMISE ID KOODI
def loosimise_id(mängu_id, loosinumber):
    # Igal loosimisel on ainulaadne ID mille see funktsioon tagastab
    params = {
        "status": "DRAW_COMPLETED",
        "page": 0,
        "size": 1,
        "gameId": mängu_id,
        "number": loosinumber
        }
    loosimised = küsi_loosimisi(params)
    if not loosimised:									# Tühja vastuse puhul tagastab None
        return None
    return loosimised[0]["id"]
"""

def andmed(loosi_id):
    """ Abifunktsioon kahele numbritagastusfunktsioonile """
    detailne_url = f"{api_url}/{loosi_id}"				# Päringu URL pannakse kokku põhiURList ja unikaalsest loosi IDst
    detailne_vastus = requests.get(detailne_url, timeout=15)
    detailne_vastus.raise_for_status()
    return detailne_vastus.json()

def tagasta_võidunumbrid(loosi_id, numbritüüp):			# Tagastab valikuliselt kas siis põhi- või lisanumbrid(Viking, Euroj.)
    detailne_data = andmed(loosi_id)
    if numbritüüp == "põhinumbrid":
        num = "MAIN-NUMBERS"
    else:
        num = "ADDITIONAL-NUMBERS"
    for stage in detailne_data.get("results", {}).get("stages", []):
        if stage["code"] == num:						# Otsitakse JSON vastusest vastavalt kas põhi- või lisanumbreid
            return stage["winningNumbers"]				# Tagastatakse JSON vastusest vastavad võidunumbrid
    return []

def tagasta_bingo_numbrid(loosi_id):
    """ Funktsioon mis tagastab Bingo loto loosinumbrite listi """
    numbrid = []										# List kuhu koguda kõik selle loosimise sammude numbrid
    detailne_data = andmed(loosi_id)
    for stage in detailne_data.get("results", {}).get("stages", []):
        if stage["code"] == "CORNERS" or stage["code"] == "DIAGONALS" or stage["code"] == "FULL-GRID":
            numbrid.extend(stage["winningNumbers"])
    return numbrid
        
"""   TESTIMISEKS KASUTATUD VÄLJUNDID:
     
print(viimase_loosimise_nr(viking_id))
print(viimase_loosimise_nr(eurojackpot_id))
print(viimase_loosimise_nr(bingo_id))

print(loosimise_id(viking_id, viimase_loosimise_nr(viking_id)))
print(loosimise_id(eurojackpot_id, viimase_loosimise_nr(eurojackpot_id)))
print(loosimise_id(bingo_id, viimase_loosimise_nr(bingo_id)))

print(tagasta_võidunumbrid(loosimise_id(viking_id, viimase_loosimise_nr(viking_id)), "põhinumbrid"))
print(tagasta_võidunumbrid(loosimise_id(viking_id, viimase_loosimise_nr(viking_id)), "lisanumbrid"))
print(tagasta_võidunumbrid(loosimise_id(eurojackpot_id, viimase_loosimise_nr(eurojackpot_id)), "põhinumbrid"))
print(tagasta_võidunumbrid(loosimise_id(eurojackpot_id, viimase_loosimise_nr(eurojackpot_id)), "lisanumbrid"))
print(tagasta_bingo_numbrid(loosimise_id(bingo_id, viimase_loosimise_nr(bingo_id))))

"""

def tulemuste_koguja(kogus, mäng, tüüp=None):
    """ See meetod kogub tsüklitega kokku varasemad loosimised(Bingol on eraldi tsükkel kuna see kasutab eraldi meetodit) ja tagastab need """
    params = {
        "status": "DRAW_COMPLETED",
        "page": 0,
        "size": kogus,
        "sort": "dateTime:desc",
        "gameId": mäng
        }
    
    loosimised = küsi_loosimisi(params)
    tulemus = []
    
    for loosimine in loosimised:
        loosi_id = loosimine["id"]
        
        if tüüp is None:
            numbrid = tagasta_bingo_numbrid(loosi_id)
        else:
            numbrid = tagasta_võidunumbrid(loosi_id, tüüp)
        tulemus.extend(numbrid)
    return tulemus            
        
#viimane_viking_nr = viimase_loosimise_nr(viking_id)
#viimane_viking_id = loosimise_id(viking_id, viimane_viking_nr)
