import tkinter as tk
import tkinter.ttk as ttk

import PageAngajat
import PageAngajatHarnic
import PageConcediaza
import PageDetalii_Angajat
import PageEchipament
import PageJoc
import PageListaAngajati
import PageListaClienti
import PageListaEchipamente
import PageListaJocuri
import PageListaInchirieri
import PageListaSalarii


class PageMeniuriCEO(tk.Frame):
    def __init__(self, master):
        # initializare frame
        tk.Frame.__init__(self, master, width=400, height=400)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        label = ttk.Label(self)
        label.configure(text='        ')
        label.grid(column=0, row=0, sticky=tk.W)

        button_adauga_joc = ttk.Button(self)
        button_adauga_joc.configure(state='normal', text='Adauga joc', width=20)
        button_adauga_joc.grid(column=1, row=1, sticky=tk.W)
        button_adauga_joc.configure(command=self.deschide_joc)

        label = ttk.Label(self)
        label.configure(text='   ')
        label.grid(column=2, row=3, sticky=tk.W)

        button_adauga_echipament = ttk.Button(self)
        button_adauga_echipament.configure(state='normal', text='Adauga echipament', width=20)
        button_adauga_echipament.grid(column=3, row=1, sticky=tk.W)
        button_adauga_echipament.configure(command=self.deschide_echipament)

        label = ttk.Label(self)
        label.configure(text='')
        label.grid(column=0, row=2, sticky=tk.W)

        button_adauga_joc = ttk.Button(self)
        button_adauga_joc.configure(state='normal', text='Adauga angajat', width=20)
        button_adauga_joc.grid(column=1, row=3, sticky=tk.W)
        button_adauga_joc.configure(command=self.deschide_angajat)

        button_adauga_echipament = ttk.Button(self)
        button_adauga_echipament.configure(state='normal', text='Modifica detalii angajat', width=20)
        button_adauga_echipament.grid(column=3, row=3, sticky=tk.W)
        button_adauga_echipament.configure(command=self.deschide_detalii_angajat)

        label = ttk.Label(self)
        label.configure(text='')
        label.grid(column=0, row=4, sticky=tk.W)

        button_concediaza = ttk.Button(self)
        button_concediaza.configure(state='normal', text='Concediaza angajat', width=20)
        button_concediaza.grid(column=1, row=5, sticky=tk.W)
        button_concediaza.configure(command=self.deschide_concediaza)

        button_harnic = ttk.Button(self)
        button_harnic.configure(state='normal', text='Cel mai harnic angajat!', width=20)
        button_harnic.grid(column=3, row=5, sticky=tk.W)
        button_harnic.configure(command=self.deschide_angajat_harnic)

        label = ttk.Label(self)
        label.configure(text='        ')
        label.grid(column=0, row=6, sticky=tk.W)

        button_lista_angajati = ttk.Button(self)
        button_lista_angajati.configure(state='normal', text='Lista angajati', style='Accent.TButton', width=20)
        button_lista_angajati.grid(column=1, row=7, sticky=tk.W)
        button_lista_angajati.configure(command=self.deschide_lista_angajat)

        button_lista_clienti = ttk.Button(self)
        button_lista_clienti.configure(state='normal', text='Lista clienti', style='Accent.TButton', width=20)
        button_lista_clienti.grid(column=3, row=7, sticky=tk.W)
        button_lista_clienti.configure(command=self.deschide_lista_clienti)

        label = ttk.Label(self)
        label.configure(text='        ')
        label.grid(column=0, row=8, sticky=tk.W)

        button_lista_echipamente = ttk.Button(self)
        button_lista_echipamente.configure(state='normal', text='Lista echipamente', style='Accent.TButton', width=20)
        button_lista_echipamente.grid(column=1, row=9, sticky=tk.W)
        button_lista_echipamente.configure(command=self.deschide_lista_echipamente)

        button_lista_jocuri = ttk.Button(self)
        button_lista_jocuri.configure(state='normal', text='Lista jocuri', style='Accent.TButton', width=20)
        button_lista_jocuri.grid(column=3, row=9, sticky=tk.W)
        button_lista_jocuri.configure(command=self.deschide_lista_jocuri)

        label = ttk.Label(self)
        label.configure(text='        ')
        label.grid(column=0, row=10, sticky=tk.W)

        button_lista_inchirieri = ttk.Button(self)
        button_lista_inchirieri.configure(state='normal', text='Lista inchirieri', style='Accent.TButton', width=20)
        button_lista_inchirieri.grid(column=1, row=11, sticky=tk.W)
        button_lista_inchirieri.configure(command=self.deschide_lista_inchirieri)

        button_salarii = ttk.Button(self)
        button_salarii.configure(state='normal', text='Lista salarii', style='Accent.TButton', width=20)
        button_salarii.grid(column=3, row=11, sticky=tk.W)
        button_salarii.configure(command=self.deschide_lista_salarii)

        label = ttk.Label(self)
        label.configure(text='        ')
        label.grid(column=0, row=12, sticky=tk.W)

        label = ttk.Label(self)
        label.configure(text='        ')
        label.grid(column=4, row=0, sticky=tk.W)

    def deschide_joc(self):
        self.master.switch_frame(PageJoc.PageJoc)

    def deschide_echipament(self):
        self.master.switch_frame(PageEchipament.PageEchipament)

    def deschide_angajat(self):
        self.master.switch_frame(PageAngajat.PageAngajat)

    def deschide_detalii_angajat(self):
        self.master.switch_frame(PageDetalii_Angajat.PageDetalii_Angajat)

    def deschide_angajat_harnic(self):
        self.master.switch_frame(PageAngajatHarnic.PageAngajatHarnic)

    def deschide_concediaza(self):
        self.master.switch_frame(PageConcediaza.PageConcediaza)

    def deschide_lista_angajat(self):
        self.master.switch_frame(PageListaAngajati.PageListaAngajati)

    def deschide_lista_clienti(self):
        self.master.switch_frame(PageListaClienti.PageListaClienti)

    def deschide_lista_echipamente(self):
        self.master.switch_frame(PageListaEchipamente.PageListaEchipamente)

    def deschide_lista_jocuri(self):
        self.master.switch_frame(PageListaJocuri.PageListaJocuri)

    def deschide_lista_inchirieri(self):
        self.master.switch_frame(PageListaInchirieri.PageListaInchirieri)

    def deschide_lista_salarii(self):
        self.master.switch_frame(PageListaSalarii.PageListaSalarii)



