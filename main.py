"""

Rakenduse põhifail mis kutsub välja kasutajakeskkonna(GUI) failis(jp_gui.py) oleva meetodi(run_app())

Antud projekti näol on tegemist lotopiletite(Bingo, Eurojackpot, Viking) generaatoriga.
Selleks tõmmatakse Eesti Loto(eestiloto.ee) lehelt soovitud loosimiste arv varasemaid tulemusi
ning genereeritakse enimlevinud numbrite põhjal uued piletid.

"""
from jp_gui import *

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")				# Saab seadistada kasutama ka vastavalt op süsteemi valikut
    root = ctk.CTk()
    app = Application(root)
    root.mainloop()
