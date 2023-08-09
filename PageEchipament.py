import main
import PageMeniuriCEO
import PageMeniuriAngajat
import tkinter as tk
import tkinter.ttk as ttk

class PageEchipament(tk.Frame):
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
        label2.configure(text='             Adauga un nou echipament!')
        label2.grid(row=0, columnspan=2, column=1, sticky=tk.W)

        label1 = ttk.Label(self)
        label1.configure(text='Tip')
        label1.grid(column=0, row=1, sticky=tk.W)

        self.__values_type = ['PC', 'XBOX']
        self.__tkvar_type = tk.StringVar(value='')
        optionmenu1 = tk.OptionMenu(self, self.__tkvar_type, *self.__values_type, command=None)
        optionmenu1.configure(width='36')
        optionmenu1.grid(column=1, row=1, sticky=tk.W)

        label2 = ttk.Label(self)
        label2.configure(text='Nr Joysticks')
        label2.grid(column=0, row=2, sticky=tk.W)

        self.__values_nj = ['0', '2', '4']
        self.__tkvar_nj = tk.StringVar(value='')
        optionmenu2 = tk.OptionMenu(self, self.__tkvar_nj, *self.__values_nj, command=None)
        optionmenu2.configure(width='36')
        optionmenu2.grid(column=1, row=2, sticky=tk.W)

        label3 = ttk.Label(self)
        label3.configure(text='Age Restriction')
        label3.grid(column=0, row=3, sticky=tk.W)

        self.__values_age = ['YES', 'NO']
        self.__tkvar_age = tk.StringVar(value='')
        optionmenu = tk.OptionMenu(self, self.__tkvar_age, *self.__values_age, command=None)
        optionmenu.configure(width='36')
        optionmenu.grid(column=1, row=3, sticky=tk.W)

        label4 = ttk.Label(self)
        label4.configure(text='RAM')
        label4.grid(column=0, row=4, sticky=tk.W)

        self.entry_ram = ttk.Entry(self, width=40)
        self.entry_ram.grid(row=4, column=1, sticky=tk.W)

        label5 = ttk.Label(self)
        label5.configure(text='Procesor')
        label5.grid(column=0, row=5, sticky=tk.W)

        self.__values_processor = ['Intel Core I5', 'Intel Core I7', 'Intel Pentium III']
        self.__tkvar_processor = tk.StringVar(value='')
        optionmenu = tk.OptionMenu(self, self.__tkvar_processor, *self.__values_processor, command=None)
        optionmenu.configure(width='36')
        optionmenu.grid(column=1, row=5, sticky=tk.W)

        label6 = ttk.Label(self)
        label6.configure(text='Spatiu stocare')
        label6.grid(column=0, row=6, sticky=tk.W)

        self.entry_storage = ttk.Entry(self, width=40)
        self.entry_storage.grid(row=6, column=1, sticky=tk.W)

        label7 = ttk.Label(self)
        label7.configure(text='Placa video')
        label7.grid(column=0, row=7, sticky=tk.W)

        self.__values_gc = ['GeForce RTX 3070', 'GeForce RTX 3080', 'AMD Radeon']
        self.__tkvar_gc = tk.StringVar(value='')
        optionmenu = tk.OptionMenu(self, self.__tkvar_gc, *self.__values_gc, command=None)
        optionmenu.configure(width='36')
        optionmenu.grid(column=1, row=7, sticky=tk.W)

        button_ok_joc = ttk.Button(self)
        button_ok_joc.configure(state='normal', text='Adauga')
        button_ok_joc.grid(column=1, row=8, sticky=tk.W)
        button_ok_joc.configure(command=self.adauga_echipament)

    def adauga_echipament(self):
        cost = 10 + int(self.__tkvar_nj.get()) * 1.0 / 2 * 5
        db = main.Data_Base()
        connection = db.connect()
        cursor = connection.cursor()
        eq_id = 0
        cursor.execute(
            "INSERT INTO equipment(type, price_h, no_joysticks, age_restriction) VALUES('" + self.__tkvar_type.get() + "', " + str(
                cost) + "," + self.__tkvar_nj.get() + ", '" + self.__tkvar_age.get() + "')")
        eq_ids = cursor.execute("SELECT MAX(id_eq) FROM equipment")
        for id in eq_ids:
            eq_id = id[0]
        cursor.execute(
            "INSERT INTO equipment_details(equipment_id_eq, ram, processor,storage,graphics_card) VALUES(" + str(
                eq_id) + "," + self.entry_ram.get() + ", '" + self.__tkvar_processor.get() + "', " + self.entry_storage.get() + ",'" + self.__tkvar_gc.get() + "')")
        print("S-a adaugat o inregistrare in equipment si in equipment_details")
        connection.commit()
        cursor.close()

    def back_to_menu(self):
        if self.master.employee_id == 1:
            self.master.switch_frame(PageMeniuriCEO.PageMeniuriCEO)
        else:
            self.master.switch_frame(PageMeniuriAngajat.PageMeniuriAngajat)

