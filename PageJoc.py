import main
import PageMeniuriCEO
import PageMeniuriAngajat
import tkinter as tk
import tkinter.ttk as ttk

class PageJoc(tk.Frame):
    def __init__(self, master):
        # initializare frame
        tk.Frame.__init__(self, master, width=400, height=400)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        button_ok_client = ttk.Button(self)
        button_ok_client.configure(state='normal', text='Inapoi la meniu')
        button_ok_client.grid(column=0, row=0, sticky=tk.W)
        button_ok_client.configure(command=self.back_to_menu)

        # primul label:Adauga o inchiriere
        label2 = ttk.Label(self)
        label2.configure(text='             Adauga un nou joc!')
        label2.grid(row=0, columnspan=2, column=1, sticky=tk.W)

        label1 = ttk.Label(self)
        label1.configure(text='Nume Joc')
        label1.grid(column=0, row=1, sticky=tk.W)

        self.entry_njoc = ttk.Entry(self, width=40)
        self.entry_njoc.grid(row=1, column=1, sticky=tk.W)

        label1 = ttk.Label(self)
        label1.configure(text='Pret')
        label1.grid(column=0, row=2, sticky=tk.W)

        self.entry_pret = ttk.Entry(self, width=40)
        self.entry_pret.grid(row=2, column=1, sticky=tk.W)

        label2 = ttk.Label(self)
        label2.configure(text='Age Restriction')
        label2.grid(column=0, row=3, sticky=tk.W)

        self.__values_age = ['YES', 'NO']
        self.__tkvar_age = tk.StringVar(value='')
        optionmenu = tk.OptionMenu(self, self.__tkvar_age, *self.__values_age, command=None)
        optionmenu.configure(width='36')
        optionmenu.grid(column=1, row=3, sticky=tk.W)

        button_ok_joc = ttk.Button(self)
        button_ok_joc.configure(state='normal', text='Adauga')
        button_ok_joc.grid(column=1, row=4, sticky=tk.W)
        button_ok_joc.configure(command=self.adauga_joc)

    def adauga_joc(self):
        db = main.Data_Base()
        connection = db.connect()
        cursor = connection.cursor()
        if self.entry_pret.get() == '':
            cursor.execute(
                "INSERT INTO games(g_name, age_restriction) VALUES('" + self.entry_njoc.get() + "', '" + self.__tkvar_age.get() + "')")
        else:
            cursor.execute(
                "INSERT INTO games(g_name, price, age_restriction) VALUES('" + self.entry_njoc.get() + "', " + self.entry_pret.get() + ",'" + self.__tkvar_age.get() + "')")

        print("S-a adaugat o inregistrare in games")
        connection.commit()
        cursor.close()

    def back_to_menu(self):
        if self.master.employee_id == 1:
            self.master.switch_frame(PageMeniuriCEO.PageMeniuriCEO)
        else:
            self.master.switch_frame(PageMeniuriAngajat.PageMeniuriAngajat)

