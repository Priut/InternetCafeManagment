import PageJoc,PageInregistrare, PageClient, PageEchipament, PageInst_St_Joc, PageEch_Ocupate, PageSalariu
import tkinter as tk
import tkinter.ttk as ttk

import PageSuma


class PageMeniuriAngajat(tk.Frame):
    def __init__(self, master):
        # initializare frame
        tk.Frame.__init__(self, master, width=400, height=400)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        label1 = ttk.Label(self)
        label1.configure(text='        ')
        label1.grid(column=0, row=0, sticky=tk.W)

        button_adauga_inregistrare = ttk.Button(self)
        button_adauga_inregistrare.configure(state='normal', text='Adauga Inchiriere', width=20)
        button_adauga_inregistrare.grid(column=1, row=1, sticky=tk.W)
        button_adauga_inregistrare.configure(command=self.deschide_inregistrare)

        label2 = ttk.Label(self)
        label2.configure(text='   ')
        label2.grid(column=2, row=1, sticky=tk.W)

        button_adauga_client = ttk.Button(self)
        button_adauga_client.configure(state='normal', text='Adauga client', width=20)
        button_adauga_client.grid(column=3, row=1, sticky=tk.W)
        button_adauga_client.configure(command=self.deschide_client)

        label3 = ttk.Label(self)
        label3.configure(text='')
        label3.grid(column=0, row=2, sticky=tk.W)

        button_adauga_joc = ttk.Button(self)
        button_adauga_joc.configure(state='normal', text='Adauga joc', width=20)
        button_adauga_joc.grid(column=1, row=3, sticky=tk.W)
        button_adauga_joc.configure(command=self.deschide_joc)

        label4 = ttk.Label(self)
        label4.configure(text='   ')
        label4.grid(column=2, row=3, sticky=tk.W)

        button_adauga_echipament = ttk.Button(self)
        button_adauga_echipament.configure(state='normal', text='Adauga echipament', width=20)
        button_adauga_echipament.grid(column=3, row=3, sticky=tk.W)
        button_adauga_echipament.configure(command=self.deschide_echipament)

        label5 = ttk.Label(self)
        label5.configure(text='')
        label5.grid(column=0, row=4, sticky=tk.W)

        button_adauga_echipament = ttk.Button(self)
        button_adauga_echipament.configure(state='normal', text='Instaleaza/Sterge un joc', width=20)
        button_adauga_echipament.grid(column=1, row=5, sticky=tk.W)
        button_adauga_echipament.configure(command=self.deschide_inst_st_joc)

        label6 = ttk.Label(self)
        label6.configure(text='   ')
        label6.grid(column=2, row=5, sticky=tk.W)

        button_echipamente_ocupate = ttk.Button(self)
        button_echipamente_ocupate.configure(state='normal', text='Echipamente ocupate', width=20)
        button_echipamente_ocupate.grid(column=3, row=5, sticky=tk.W)
        button_echipamente_ocupate.configure(command=self.deschide_echipamente_ocupate)

        label5 = ttk.Label(self)
        label5.configure(text='')
        label5.grid(column=0, row=6, sticky=tk.W)

        button_adauga_echipament = ttk.Button(self)
        button_adauga_echipament.configure(state='normal', text='Vezi salariu',style='Accent.TButton', width=20)
        button_adauga_echipament.grid(column=1, row=7, sticky=tk.W)
        button_adauga_echipament.configure(command=self.deschide_salariu)

        label6 = ttk.Label(self)
        label6.configure(text='   ')
        label6.grid(column=0, row=7, sticky=tk.W)

        button_adauga_echipament = ttk.Button(self)
        button_adauga_echipament.configure(state='normal', text='Suma incasata azi',style='Accent.TButton', width=20)
        button_adauga_echipament.grid(column=3, row=7, sticky=tk.W)
        button_adauga_echipament.configure(command=self.deschide_suma_incasata)

        label7 = ttk.Label(self)
        label7.configure(text='        ')
        label7.grid(column=4, row=8, sticky=tk.W)

    def deschide_inregistrare(self):
        self.master.switch_frame(PageInregistrare.PageInregistrare)

    def deschide_client(self):
        self.master.switch_frame(PageClient.PageClient)

    def deschide_joc(self):
        self.master.switch_frame(PageJoc.PageJoc)

    def deschide_echipament(self):
        self.master.switch_frame(PageEchipament.PageEchipament)

    def deschide_inst_st_joc(self):
        self.master.switch_frame(PageInst_St_Joc.PageInst_St_Joc)

    def deschide_echipamente_ocupate(self):
        self.master.switch_frame(PageEch_Ocupate.PageEch_Ocupate)

    def deschide_salariu(self):
        self.master.switch_frame(PageSalariu.PageSalariu)

    def deschide_suma_incasata(self):
        self.master.switch_frame(PageSuma.PageSuma)

