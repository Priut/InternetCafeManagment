import main
import PageMeniuriCEO
import PageMeniuriAngajat
import tkinter as tk
import tkinter.ttk as ttk
from tkcalendar import Calendar

class PageClient(tk.Frame):
    def __init__(self, master):
        # initializare frame
        tk.Frame.__init__(self, master, width=400, height=400)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        # initializare conexiune baza fe date
        db = main.Data_Base()
        connection = db.connect()
        cursor = connection.cursor()

        button_back = ttk.Button(self)
        button_back.configure(state='normal', text='Inapoi la meniu')
        button_back.grid(column=0, row=0, sticky=tk.W)
        button_back.configure(command=self.back_to_menu)

        # primul label:Adauga un client
        label1 = ttk.Label(self)
        label1.configure(text='             Adauga un nou client!')
        label1.grid(row=0, columnspan=2, column=1, sticky=tk.W)

        # Zona alegere client
        label2 = ttk.Label(self)
        label2.configure(text='Nume')
        label2.grid(column=0, row=1, sticky=tk.W)
        # #Extragere nume clienti si id uri din bd
        self.entry_nume = ttk.Entry(self, width=40)
        self.entry_nume.grid(row=1, column=1, sticky=tk.W)

        label3 = ttk.Label(self)
        label3.configure(text='Prenume')
        label3.grid(column=0, row=2, sticky=tk.W)

        self.entry_prenume = ttk.Entry(self, width=40)
        self.entry_prenume.grid(row=2, column=1, sticky=tk.W)

        label4 = ttk.Label(self)
        label4.configure(text='Data nasterii')
        label4.grid(column=0, row=3, sticky=tk.W)
        self.cal = Calendar(self, selectmode='day',
                            year=2000, month=5,
                            day=22)

        self.cal.grid(row=3, column=1, columnspan=2, sticky=tk.W)

        button_adauga_client = ttk.Button(self)
        button_adauga_client.configure(state='normal', text='Adauga')
        button_adauga_client.grid(column=2, row=4, sticky=tk.W)
        button_adauga_client.configure(command=self.adauga_client)

        connection.commit()
        cursor.close()

    def adauga_client(self):
        db = main.Data_Base()
        connection = db.connect()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO clients(first_name,last_name,birth_date) VALUES ('" + str(
                self.entry_prenume.get()) + "','" + str(
                self.entry_nume.get()) + "',TO_DATE('" + self.cal.get_date() + "','MM/DD/YYYY'))")
        print("S-a adaugat o inregistrare in clients")
        connection.commit()
        cursor.close()

    def back_to_menu(self):
        if self.master.employee_id == 1:
            self.master.switch_frame(PageMeniuriCEO.PageMeniuriCEO)
        else:
            self.master.switch_frame(PageMeniuriAngajat.PageMeniuriAngajat)

