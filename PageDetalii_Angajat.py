import main
import PageMeniuriCEO
import PageMeniuriAngajat
import tkinter as tk
import tkinter.ttk as ttk

class PageDetalii_Angajat(tk.Frame):
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


        label1 = ttk.Label(self)
        label1.configure(text='             Modifica detaliile unui angajat!')
        label1.grid(row=0, columnspan=2, column=1, sticky=tk.W)

        label2 = ttk.Label(self)
        label2.configure(text='Angajat')
        label2.grid(column=0, row=1, sticky=tk.W)

        # #Extragere nume angajati si id uri din bd
        self.__tkvar_angajati = tk.StringVar(value='')
        self.__values_angajati = []
        self.angajati_ids = []

        rows = cursor.execute("SELECT id_em,first_name ||' '|| last_name FROM employees")
        for row in rows:
            self.__values_angajati.append(str(row[1]))
            self.angajati_ids.append(row[0])

        optionmenu1 = tk.OptionMenu(self, self.__tkvar_angajati, *self.__values_angajati)
        optionmenu1.configure(width='36')
        optionmenu1.grid(column=1, row=1, sticky=tk.W)

        button_ok_client = ttk.Button(self)
        button_ok_client.configure(state='normal', text='OK')
        button_ok_client.grid(column=2, row=1, sticky=tk.W)
        button_ok_client.configure(command=self.ok_angajat)

        connection.commit()
        cursor.close()

    def ok_angajat(self):

        db = main.Data_Base()
        connection = db.connect()
        cursor = connection.cursor()
        # Zona alegere client
        label2 = ttk.Label(self)
        label2.configure(text='Nume')
        label2.grid(column=0, row=2, sticky=tk.W)
        # #Extragere nume clienti si id uri din bd
        self.entry_nume = ttk.Entry(self, width=40)
        self.entry_nume.grid(row=2, column=1, sticky=tk.W)

        label3 = ttk.Label(self)
        label3.configure(text='Prenume')
        label3.grid(column=0, row=3, sticky=tk.W)

        self.entry_prenume = ttk.Entry(self, width=40)
        self.entry_prenume.grid(row=3, column=1, sticky=tk.W)

        label4 = ttk.Label(self)
        label4.configure(text='Plata pe ora')
        label4.grid(column=0, row=4, sticky=tk.W)

        self.entry_plata = ttk.Entry(self, width=40)
        self.entry_plata.grid(row=4, column=1, sticky=tk.W)

        label5 = ttk.Label(self)
        label5.configure(text='Job ID')
        label5.grid(column=0, row=5, sticky=tk.W)

        self.entry_job = ttk.Entry(self, width=40)
        self.entry_job.grid(row=5, column=1, sticky=tk.W)

        rows = cursor.execute("SELECT first_name, last_name, payment_h, job_id FROM employees WHERE id_em="
                              + str(self.angajati_ids[self.__values_angajati.index(self.__tkvar_angajati.get())]))
        text = ''
        for row in rows:
            text = "Nume vechi: " + str(row[1]) + "\nPrenume vechi: " + str(row[0]) + "\nSalariu vechi: " + str(
                row[2]) + \
                   "\nJob vechi: " + str(row[3])
        label6 = ttk.Label(self)
        label6.configure(text=text)
        label6.grid(column=1, row=6, sticky=tk.W)

        button_adauga_angajat = ttk.Button(self)
        button_adauga_angajat.configure(state='normal', text='Modifica')
        button_adauga_angajat.grid(column=2, row=7, sticky=tk.W)
        button_adauga_angajat.configure(command=self.modifica_angajat)

    def modifica_angajat(self):
        db = main.Data_Base()
        connection = db.connect()
        cursor = connection.cursor()
        cursor.execute("COMMIT")  # se incheie orice tranzactie existenta inainte
        cursor.execute("SET TRANSACTION NAME 'employee_update'")
        if self.entry_prenume.get() != '':
            cursor.execute("UPDATE employees SET first_name = '" + self.entry_prenume.get() + "' WHERE id_em=" + str(
                self.angajati_ids[self.__values_angajati.index(self.__tkvar_angajati.get())]))
            print("S-a modificat prenumele unui angajat")
        if self.entry_nume.get() != '':
            cursor.execute("UPDATE employees SET last_name = '" + self.entry_nume.get() + "' WHERE id_em=" + str(
                self.angajati_ids[self.__values_angajati.index(self.__tkvar_angajati.get())]))
            print("S-a modificat numele unui angajat")
        if self.entry_plata.get() != '':
            cursor.execute("UPDATE employees SET payment_h = " + self.entry_plata.get() + " WHERE id_em=" + str(
                self.angajati_ids[self.__values_angajati.index(self.__tkvar_angajati.get())]))
            print("S-a modificat salariul unui angajat")
        if self.entry_job.get() != '':
            cursor.execute("UPDATE employees SET job_id = '" + self.entry_job.get() + "' WHERE id_em=" + str(
                self.angajati_ids[self.__values_angajati.index(self.__tkvar_angajati.get())]))
            print("S-a modificat jobul unui angajat")
        cursor.execute("COMMIT")  # incheie tranzactia prin replicarea schimabrilor
        cursor.close()

    def back_to_menu(self):
        if self.master.employee_id == 1:
            self.master.switch_frame(PageMeniuriCEO.PageMeniuriCEO)
        else:
            self.master.switch_frame(PageMeniuriAngajat.PageMeniuriAngajat)

