import main
import PageMeniuriCEO
import PageMeniuriAngajat
import tkinter as tk
import tkinter.ttk as ttk
import datetime

class PageEch_Ocupate(tk.Frame):
    def __init__(self, master):
        # initializare frame
        tk.Frame.__init__(self, master, width=400, height=400)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        # initializare conexiune baza de date
        db = main.Data_Base()
        connection = db.connect()
        cursor = connection.cursor()

        button_back = ttk.Button(self)
        button_back.configure(state='normal', text='Inapoi la meniu')
        button_back.grid(column=0, row=0, sticky=tk.W)
        button_back.configure(command=self.back_to_menu)

        # primul label:Adauga un client
        label1 = ttk.Label(self)
        label1.configure(text='             Echipamente ocupate')
        label1.grid(row=0, column=1, sticky=tk.W)

        label1 = ttk.Label(self)
        label1.configure(text='             ')
        label1.grid(row=0, column=2, sticky=tk.W)

        rows = cursor.execute("SELECT r.equipment_id_eq, e.type FROM rentals r, equipment e WHERE r.rental_date=to_date(to_char(sysdate, 'DD-MM-YYYY'), 'DD-MM-YYYY') AND r.rental_hour=trunc((sysdate - trunc(sysdate)) * 24) AND r.equipment_id_eq = e.id_eq")
        i=0
        for row in rows:
            label = ttk.Label(self)
            label.configure(text='          '+str(row[1])+'   '+str(row[0]))
            label.grid(column=0, row=i*2+2, sticky=tk.W)

            progress = ttk.Progressbar(self,  length=200, mode='determinate')
            progress.grid(column=1, row=i*2+2, sticky=tk.W)
            now = datetime.datetime.now()
            progress['value'] = now.minute * 100.0 / 60


            label = ttk.Label(self)
            label.configure(text='   ')
            #label.grid(column=0, row=i * 2 +1 , sticky=tk.W)

            label = ttk.Label(self)
            label.configure(text='   ')
            label.grid(column=1, row=i * 2+1, sticky=tk.W)
            i=i+1

        label = ttk.Label(self)
        label.configure(text='   ')
        label.grid(column=1, row=i * 2 + 3, sticky=tk.W)

    def back_to_menu(self):
        if self.master.employee_id == 1:
            self.master.switch_frame(PageMeniuriCEO.PageMeniuriCEO)
        else:
            self.master.switch_frame(PageMeniuriAngajat.PageMeniuriAngajat)

