# CustomTkinter:  pip install customtkinter
import customtkinter as ctk
import tkinter as tk
# Pillow:  pip install pillow - piltide kasutamiseks
from PIL import Image
from jp_generator import *
from jp_random import juhusliku_loterii_generaator
from tkinter import messagebox
from jp_salvesta import *
from jp_statistika import *

""" konstandid """
THEME_BG = "#163d6d"
THEME_FG = "#1a1a1a"
THEME_ACCENT = "#2a7de1"
VALGE = "#ffffff"
HELESININE = "#b9f3f7"
KOLLANE = "#fcf84e"
HELEHALL = "#eec1c9"
TUMEHALL = "#c9707f"
TUMELILLA = "#281c5e"
THEME_FONT_FAMILY = "Helvetica"
THEME_FONT_SIZE = 12 
X = 1.4		# <--- muutuja rakenduse laiuse muutmiseks
Y = 1.4		# <--- muutuja rakenduse kõrguse muutmiseks
MAX_LOOSIMISI = 50		# <--- suurim lubatud loosimiste arv

NUPU_KUJUNDUS = {
    "fg_color": THEME_ACCENT,
    "text_color": VALGE,
    "width": 150 * X,
    "height": 30 * Y
    }
V_JA_E_KUJUNDUS = {
    "text_color": THEME_FG,
    "border_width": 2,
    "corner_radius": 3,
    "width": 24 * X,
    "height": 20 * Y
    }
B_KUJUNDUS = {
    "text_color": THEME_FG,
    "border_width": 2,
    "corner_radius": 3,
    "width": 28 * X,
    "height": 28 * Y
    }

def apply_theme(root):
    """Apply the project theme to a window. CustomTkinter styles per widget,
    so the widgets themselves carry the rest of the colours."""
    root.configure(fg_color=THEME_BG)

class Application:
    def __init__(self, root):
        self.root = root
        
        laius = int(550 * X)
        kõrgus = int(550 * Y)
        
        root.title("LotoGen")
        root.geometry(f"{laius}x{kõrgus}")
        root.update_idletasks()
        root.resizable(False, False)
        root.geometry(
            f"+{(root.winfo_screenwidth() - laius) // 2}"
            f"+{(root.winfo_screenheight() - kõrgus) // 2}"
        )
        apply_theme(root)
        
        """ Fondi loomine """
        self.nupu_font = ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE)

        """ NUPUD """
        self.label8 = ctk.CTkLabel(root, text="Lotonumbrid eelnevate looside põhjal", text_color="#faf76b", font=ctk.CTkFont(family="Helvetica", size=8), width=X*135, height=Y*20)
        self.label8.place(x=X*21, y=Y*150)        
        self.button1 = ctk.CTkButton(root, text="Genereeri", command=self.on_button1, font=self.nupu_font, **NUPU_KUJUNDUS)
        self.button1.place(x=X*18, y=Y*177)
        self.label9 = ctk.CTkLabel(root, text="Juhuslike lotonumbrite genereerimine", text_color="#faf76b", font=ctk.CTkFont(family="Helvetica", size=8), width=X*135, height=Y*20)
        self.label9.place(x=X*21, y=Y*220)        
        self.button2 = ctk.CTkButton(root, text="Juhuslik", command=self.on_button2, font=self.nupu_font, **NUPU_KUJUNDUS)
        self.button2.place(x=X*18, y=Y*247)
        self.label10 = ctk.CTkLabel(root, text="Viimaste tulemustega võrdlemine", text_color="#faf76b", font=ctk.CTkFont(family="Helvetica", size=8), width=X*135, height=Y*20)
        self.label10.place(x=X*21, y=Y*290)        
        self.button3 = ctk.CTkButton(root, text="Kontrolli", command=self.on_button3, font=self.nupu_font, **NUPU_KUJUNDUS)
        self.button3.place(x=X*18, y=Y*317)
        self.label11 = ctk.CTkLabel(root, text='Enim esinenud Vikingi numbrid', text_color='#faf76b', font=ctk.CTkFont(family='Helvetica', size=8), width=X*135, height=Y*20)
        self.label11.place(x=X*21, y=Y*360)
        self.button4 = ctk.CTkButton(root, text='Statistika', command=self.on_button4, font=self.nupu_font, **NUPU_KUJUNDUS)
        self.button4.place(x=X*18, y=Y*387)

        """ Teksti sisend """
        self.entry1 = ctk.CTkEntry(root, fg_color=VALGE, text_color=THEME_FG, font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), corner_radius=3, width=X*54, height=Y*30)
        self.entry1.place(x=X*60, y=Y*66)

        """ RAAMID """
        self.frame1 = ctk.CTkFrame(root, fg_color="#FFF", border_width=X*2, corner_radius=13, width=X*370, height=Y*510)
        self.frame1.place(x=X*156, y=Y*20)
        self.frame2 = ctk.CTkFrame(self.frame1, fg_color="#EEE", border_width=X*2, width=X*170, height=Y*180)
        self.frame2.place(x=X*15, y=Y*10)
        self.frame4 = ctk.CTkFrame(self.frame1, fg_color="#EEE", border_width=X*2, width=X*170, height=Y*180)
        self.frame4.place(x=X*190, y=Y*10)
        self.frame5 = ctk.CTkFrame(self.frame1, fg_color=TUMELILLA, border_width=X*2, width=X*250, height=Y*300)
        self.frame5.place(x=X*60, y=Y*200)

        """ PILDID """
        self.image1_image = ctk.CTkImage(Image.open("pic/lotogen.png"), size=(130*X, 30*Y))
        self.image1 = ctk.CTkLabel(root, text="", image=self.image1_image, width=X*130, height=Y*30)
        self.image1.place(x=X*20, y=Y*20)
        self.image4_image = ctk.CTkImage(Image.open("pic/vl_logo.png"), size=(130*X, 60*Y))
        self.image4 = ctk.CTkLabel(self.frame2, text="", image=self.image4_image, width=X*130, height=Y*60)
        self.image4.place(x=X*20, y=Y*10)
        self.image5_image = ctk.CTkImage(Image.open("pic/ej_logo.jpg"), size=(130*X, 60*Y))
        self.image5 = ctk.CTkLabel(self.frame4, text="", image=self.image5_image, width=X*130, height=Y*60)
        self.image5.place(x=X*21, y=Y*10)
        self.image6_image = ctk.CTkImage(Image.open("pic/bingo.jpg"), size=(130*X, 60*Y))
        self.image6 = ctk.CTkLabel(self.frame5, text="", image=self.image6_image, width=X*130, height=Y*60)
        self.image6.place(x=X*60, y=Y*11)

        """ SILDID """
        self.label1 = ctk.CTkLabel(root, text="Loosimiste hulk", text_color="#faf76b", font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), width=X*114, height=Y*33)
        self.label1.place(x=X*30, y=Y*99)
        self.label2 = ctk.CTkLabel(self.frame2, text="Vikinglotto põhinumbrid:", text_color=TUMELILLA, font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), width=X*147, height=Y*27)
        self.label2.place(x=X*12, y=Y*68)
        self.label3 = ctk.CTkLabel(self.frame4, text="Eurojackpot põhinumbrid:", text_color=TUMELILLA, font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), width=X*150, height=Y*27)
        self.label3.place(x=X*12, y=Y*66)
        self.label4 = ctk.CTkLabel(self.frame5, text="Bingo  loto numbrid:", text_color=HELEHALL, font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), width=X*135, height=Y*27)
        self.label4.place(x=X*58, y=Y*80)
        self.label5 = ctk.CTkLabel(self.frame2, text="Vikinglotto lisanumber:", text_color=TUMELILLA, font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), width=X*147, height=Y*27)
        self.label5.place(x=X*13, y=Y*120)
        self.label6 = ctk.CTkLabel(self.frame4, text="Eurojackpot lisanumbrid:", text_color=TUMELILLA, font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), width=X*150, height=Y*27)
        self.label6.place(x=X*10, y=Y*121)

        """ Vikingi põhinumbrid """
        self.text1 = ctk.CTkTextbox(self.frame2, fg_color=VALGE, font=self.nupu_font, **V_JA_E_KUJUNDUS)
        self.text1.place(x=X*10, y=Y*96)
        self.text2 = ctk.CTkTextbox(self.frame2, fg_color=VALGE, font=self.nupu_font, **V_JA_E_KUJUNDUS)
        self.text2.place(x=X*35, y=Y*96)
        self.text3 = ctk.CTkTextbox(self.frame2, fg_color=VALGE, font=self.nupu_font, **V_JA_E_KUJUNDUS)
        self.text3.place(x=X*60, y=Y*96)
        self.text4 = ctk.CTkTextbox(self.frame2, fg_color=VALGE, font=self.nupu_font, **V_JA_E_KUJUNDUS)
        self.text4.place(x=X*85, y=Y*96)
        self.text5 = ctk.CTkTextbox(self.frame2, fg_color=VALGE, font=self.nupu_font, **V_JA_E_KUJUNDUS)
        self.text5.place(x=X*110, y=Y*96)
        self.text6 = ctk.CTkTextbox(self.frame2, fg_color=VALGE, font=self.nupu_font, **V_JA_E_KUJUNDUS)
        self.text6.place(x=X*135, y=Y*96)
        
        """ Vikingi lisanumber """
        self.text7 = ctk.CTkTextbox(self.frame2, fg_color=HELESININE, font=self.nupu_font, **V_JA_E_KUJUNDUS)
        self.text7.place(x=X*71, y=Y*148)

        """ Eurojackpot põhinumbrid """
        self.text8 = ctk.CTkTextbox(self.frame1, fg_color=VALGE, font=self.nupu_font, **V_JA_E_KUJUNDUS)
        self.text8.place(x=X*200, y=Y*105)
        self.text9 = ctk.CTkTextbox(self.frame1, fg_color=VALGE, font=self.nupu_font, **V_JA_E_KUJUNDUS)
        self.text9.place(x=X*230, y=Y*105)
        self.text10 = ctk.CTkTextbox(self.frame1, fg_color=VALGE, font=self.nupu_font, **V_JA_E_KUJUNDUS)
        self.text10.place(x=X*260, y=Y*105)
        self.text11 = ctk.CTkTextbox(self.frame1, fg_color=VALGE, font=self.nupu_font, **V_JA_E_KUJUNDUS)
        self.text11.place(x=X*290, y=Y*105)
        self.text12 = ctk.CTkTextbox(self.frame1, fg_color=VALGE, font=self.nupu_font, **V_JA_E_KUJUNDUS)
        self.text12.place(x=X*320, y=Y*105)
        
        """ Eurojackpot lisanumbrid """
        self.text13 = ctk.CTkTextbox(self.frame1, fg_color=KOLLANE, font=self.nupu_font, **V_JA_E_KUJUNDUS)
        self.text13.place(x=X*245, y=Y*158)
        self.text14 = ctk.CTkTextbox(self.frame1, fg_color=KOLLANE, font=self.nupu_font, **V_JA_E_KUJUNDUS)
        self.text14.place(x=X*275, y=Y*158)
        
        """ BINGO numbrid """
        """ B """
        self.text15 = ctk.CTkTextbox(self.frame5, fg_color=TUMEHALL,  font=self.nupu_font, **B_KUJUNDUS)
        self.text15.place(x=X*45, y=Y*143)
        self.text16 = ctk.CTkTextbox(self.frame5, fg_color=HELEHALL, font=self.nupu_font, **B_KUJUNDUS)
        self.text16.place(x=X*45, y=Y*173)
        self.text17 = ctk.CTkTextbox(self.frame5, fg_color=HELEHALL, font=self.nupu_font, **B_KUJUNDUS)
        self.text17.place(x=X*45, y=Y*203)
        self.text18 = ctk.CTkTextbox(self.frame5, fg_color=HELEHALL, font=self.nupu_font, **B_KUJUNDUS)
        self.text18.place(x=X*45, y=Y*233)
        self.text19 = ctk.CTkTextbox(self.frame5, fg_color=TUMEHALL, font=self.nupu_font, **B_KUJUNDUS)
        self.text19.place(x=X*45, y=Y*263)
        """ I """
        self.text20 = ctk.CTkTextbox(self.frame5, fg_color=HELEHALL, font=self.nupu_font, **B_KUJUNDUS)
        self.text20.place(x=X*75, y=Y*143)
        self.text21 = ctk.CTkTextbox(self.frame5, fg_color=TUMEHALL, font=self.nupu_font, **B_KUJUNDUS)
        self.text21.place(x=X*75, y=Y*173)
        self.text22 = ctk.CTkTextbox(self.frame5, fg_color=HELEHALL, font=self.nupu_font, **B_KUJUNDUS)
        self.text22.place(x=X*75, y=Y*203)
        self.text23 = ctk.CTkTextbox(self.frame5, fg_color=TUMEHALL, font=self.nupu_font, **B_KUJUNDUS)
        self.text23.place(x=X*75, y=Y*233)
        self.text24 = ctk.CTkTextbox(self.frame5, fg_color=HELEHALL, font=self.nupu_font, **B_KUJUNDUS)
        self.text24.place(x=X*75, y=Y*263)
        """ N """
        self.text25 = ctk.CTkTextbox(self.frame5, fg_color=HELEHALL, font=self.nupu_font, **B_KUJUNDUS)
        self.text25.place(x=X*105, y=Y*143)
        self.text26 = ctk.CTkTextbox(self.frame5, fg_color=HELEHALL, font=self.nupu_font, **B_KUJUNDUS)
        self.text26.place(x=X*105, y=Y*173)
        self.text27 = ctk.CTkTextbox(self.frame5, fg_color=TUMEHALL, font=self.nupu_font, **B_KUJUNDUS)
        self.text27.place(x=X*105, y=Y*203)
        self.text28 = ctk.CTkTextbox(self.frame5, fg_color=HELEHALL, font=self.nupu_font, **B_KUJUNDUS)
        self.text28.place(x=X*105, y=Y*233)
        self.text29 = ctk.CTkTextbox(self.frame5, fg_color=HELEHALL, font=self.nupu_font, **B_KUJUNDUS)
        self.text29.place(x=X*105, y=Y*263)
        """ G """
        self.text30 = ctk.CTkTextbox(self.frame5, fg_color=HELEHALL, font=self.nupu_font, **B_KUJUNDUS)
        self.text30.place(x=X*135, y=Y*143)
        self.text31 = ctk.CTkTextbox(self.frame5, fg_color=TUMEHALL, font=self.nupu_font, **B_KUJUNDUS)
        self.text31.place(x=X*135, y=Y*173)
        self.text32 = ctk.CTkTextbox(self.frame5, fg_color=HELEHALL, font=self.nupu_font, **B_KUJUNDUS)
        self.text32.place(x=X*135, y=Y*203)
        self.text33 = ctk.CTkTextbox(self.frame5, fg_color=TUMEHALL, font=self.nupu_font, **B_KUJUNDUS)
        self.text33.place(x=X*135, y=Y*233)
        self.text34 = ctk.CTkTextbox(self.frame5, fg_color=HELEHALL, font=self.nupu_font, **B_KUJUNDUS)
        self.text34.place(x=X*135, y=Y*263)
        """ O """
        self.text35 = ctk.CTkTextbox(self.frame5, fg_color=TUMEHALL, font=self.nupu_font, **B_KUJUNDUS)
        self.text35.place(x=X*165, y=Y*143)
        self.text36 = ctk.CTkTextbox(self.frame5, fg_color=HELEHALL, font=self.nupu_font, **B_KUJUNDUS)
        self.text36.place(x=X*165, y=Y*173)
        self.text37 = ctk.CTkTextbox(self.frame5, fg_color=HELEHALL, font=self.nupu_font, **B_KUJUNDUS)
        self.text37.place(x=X*165, y=Y*203)
        self.text38 = ctk.CTkTextbox(self.frame5, fg_color=HELEHALL, font=self.nupu_font, **B_KUJUNDUS)
        self.text38.place(x=X*165, y=Y*233)
        self.text39 = ctk.CTkTextbox(self.frame5, fg_color=TUMEHALL, font=self.nupu_font, **B_KUJUNDUS)
        self.text39.place(x=X*165, y=Y*263)
        
    def tühjenda_väljad(self):
        self.text1.delete(0.0, 'end')
        self.text2.delete(0.0, 'end')
        self.text3.delete(0.0, 'end')
        self.text4.delete(0.0, 'end')
        self.text5.delete(0.0, 'end')
        self.text6.delete(0.0, 'end')
        self.text7.delete(0.0, 'end')
    
    def loe_loosimiste_arv(self):
        '''Loeb loosimiste arvu tühjalt väljalt ja kontrollib seda. Vea korral tagastab None'''
        try:
            arv = int(self.entry1.get())
        except ValueError:
            messagebox.showinfo('LotoGen', 'Loosimiste väljale tuleb sisestada täisarv!')
            return None
        if arv < 1 or arv > MAX_LOOSIMISI:
            messagebox.showinfo('LotoGen', f'Loosimiste arv peab jääma vahemikku 1 kuni {MAX_LOOSIMISI}!')
            return None
        return arv
    
    def loe_pilet(self):
        '''Loeb Vikingi numbrid tekstiväljadelt: (põhinumbrid, lisanumbrid)'''
        väljad = [self.text1, self.text2, self.text3, self.text4, self.text5, self.text6, self.text7]
        numbrid = [väli.get('0.0', 'end').strip() for väli in väljad]
        return numbrid [:6], numbrid[6:]

    def on_button1(self):
        """ Loto generaatori nupp """
        """ Kontrollime kas loosimiste arvu väljale sisestati täisarv """
        arv = self.loe_loosimiste_arv()
        if arv is None:
            return
        try:
            tulemused(arv, self)
        except Exception as viga:
            messagebox.showerror('LotoGen', f'Numbrite hankimine ebaõnnestus: {viga}')
            return
        põhi, lisa = self.loe_pilet()
        salvesta_pilet('Viking', 'Statistika', põhi, lisa)
    
    def on_button2(self):
        """ Juhusliku kombinatsiooni genereerimise nupp """
        põhi = juhusliku_loterii_generaator(1, 48, 6)
        lisa = juhusliku_loterii_generaator(1, 5, 1)
        väljad = [self.text1, self.text2, self.text3, self.text4, self.text5, self.text6, self.text7]
        self.tühjenda_väljad()
        for väli, nr in zip(väljad, põhi + lisa):
            väli.insert('end', str(nr))
        salvesta_pilet('Viking', 'Juhuslik', põhi, lisa)
        

    def on_button3(self):
        """ Tulemuse võrdlemise nupp viimase lotoga """
        pass
    
    def on_button4(self):
        '''Statistika nupp'''
        arv = self.loe_loosimiste_arv()
        if arv is None:
            return
        try:
            tulemus = sagedasemad(arv)
        except Exception as viga:
            messagebox.showerror('LotoGen', f'Andmete hankimine ebaõnnestus: {viga}')
            return
        read = [f'{nr} - {kord} korda' for nr, kord in tulemus]
        messagebox.showinfo('Enim esinenud Vikingi numbrid', '\n'.join(read))


