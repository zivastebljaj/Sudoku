import tkinter as tk
import model as m

ODMIK = 15
ROB = 30
VISINA = 300
SIRINA = 300

class Sudoku:

    def __init__(self, okno):
        self.okno = okno
        self.okno.title('Sudoku')
        self.vrstica = None
        self.stolpec = None
        self.igra = m.Igra().ustvari_zacetno_plosco()
        self.pripravi_graficni_vmesnik()

    def pripravi_graficni_vmesnik(self):
        self.plosca = tk.Canvas(width=VISINA , height=SIRINA)
        self.plosca.grid(row=0, column=0)
        self.narisi_mrezo()
        self.prikazi_stevilke()
        self.plosca.bind('<Button-1>', self.klik)
        self.plosca.bind('<Key>', self.vpis)
        self.plosca.bind('<BackSpace>', self.izbris)
        prikaz_gumbov = tk.Frame(okno)
        prikaz_gumbov.grid(row='1', column='0')
        self.preizkus = tk.Button(prikaz_gumbov,
                                  text='Preveri',
                                  command=self.prikazi_oznako)
        self.preizkus.grid(row='1', column='1')
        self.nova_igra = tk.Button(prikaz_gumbov,
                                   text='Nova igra',
                                   command=self.ponastavi)
        self.nova_igra.grid(row='1', column='0')
        prikaz_oznake = tk.Frame(okno)
        prikaz_oznake.grid(row='2', column='0')
        self.oznaka = tk.Label(prikaz_oznake, text='')
        self.oznaka.grid(row='0', column='0')
        
    def prikazi_oznako(self):
        prikaz_oznake = tk.Frame(okno)
        prikaz_oznake.grid(row='2', column='0')
        if m.Igra().preveri_pravilnost(self.igra):
            self.oznaka = tk.Label(prikaz_oznake, text=':)')
            self.oznaka.grid(row='0', column='0')
        else:
            self.oznaka = tk.Label(prikaz_oznake, text=':(')     
            self.oznaka.grid(row='0', column='0')

    def narisi_mrezo(self):        
        for i in range(10):
            if i % 3 == 0:
                barva = 'black'
            else:
                barva = 'gray'
            x1 = ODMIK + i * ROB
            y1 = ODMIK
            x2 = ODMIK + i * ROB
            y2 = VISINA - ODMIK
            self.plosca.create_line(x1, y1, x2, y2, fill=barva)
            x1 = ODMIK
            y1 = ODMIK + i * ROB
            x2 = SIRINA - ODMIK
            y2 = ODMIK + i * ROB
            self.plosca.create_line(x1, y1, x2, y2, fill=barva)

    def prikazi_stevilke(self):
        self.plosca.delete('stevilke')
        for i in range(9):
            for j in range(9):
                x = ODMIK + j * ROB + ROB / 2
                y = ODMIK + i * ROB + ROB / 2
                vrednost = self.igra[i][j]
                self.plosca.create_text(x, y,
                                        text=vrednost,
                                        tags='stevilke')

    def klik(self, event):
        x, y = event.x, event.y
        if ODMIK < x < SIRINA - ODMIK and ODMIK < y < VISINA - ODMIK:
            self.plosca.focus_set()
            self.vrstica = (y  - ODMIK)// ROB
            self.stolpec = (x - ODMIK) // ROB
            self.oznaci_kvadratek()
        else:
            self.plosca.delete('okvir')


    def oznaci_kvadratek(self):
        self.plosca.delete('okvir')
        x1 = ODMIK + self.stolpec * ROB + 1
        y1 = ODMIK + self.vrstica * ROB + 1
        x2 = ODMIK + (self.stolpec + 1) * ROB - 1
        y2 = ODMIK + (self.vrstica + 1) * ROB - 1
        self.plosca.create_rectangle(x1, y1, x2, y2,
                                     outline='red',
                                     tags='okvir')

    def vpis(self, event):
        vrstica = self.vrstica
        stolpec = self.stolpec
        if event.char in '123456789' and self.igra[vrstica][stolpec] == None:
            self.igra[vrstica][stolpec] = int(event.char)
            self.prikazi_stevilke()

    def izbris(self, event):
        self.igra[self.vrstica][self.stolpec] = None
        self.prikazi_stevilke()

    def ponastavi(self):
        self.igra = m.Igra().ustvari_zacetno_plosco()
        self.pripravi_graficni_vmesnik()


okno = tk.Tk()
moj_program = Sudoku(okno)
okno.mainloop()
                                
