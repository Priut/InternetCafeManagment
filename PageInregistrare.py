import main
import PageMeniuriCEO
import PageMeniuriAngajat
import tkinter as tk
import tkinter.ttk as ttk

class PageInregistrare(tk.Frame):
    def __init__(self, master):
        # initializare frame
        tk.Frame.__init__(self, master, width=400, height=400)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        # initializare conexiune baza fe date
        db = main.Data_Base()
        self.__values_nClient = []
        self.client_ids = []
        connection = db.connect()
        cursor = connection.cursor()

        button_back = ttk.Button(self)
        button_back.configure(state='normal', text='Inapoi la meniu')
        button_back.grid(column=0, row=0, sticky=tk.W)
        button_back.configure(command=self.back_to_menu)

        # primul label:Adauga o inchiriere
        label1 = ttk.Label(self)
        label1.configure(text='             Adauga o noua inchiririere!')
        label1.grid(row=0, columnspan=2, column=1, sticky=tk.W)

        # Zona alegere client
        label2 = ttk.Label(self)
        label2.configure(text='Client')
        label2.grid(column=0, row=1, sticky=tk.W)

        # #Extragere nume clienti si id uri din bd
        self.__tkvar_nClient = tk.StringVar(value='')

        rows = cursor.execute("SELECT id_client,first_name ||' '|| last_name FROM clients")
        for row in rows:
            self.__values_nClient.append(str(row[1]))
            self.client_ids.append(row[0])

        optionmenu1 = tk.OptionMenu(self, self.__tkvar_nClient, *self.__values_nClient, command=None)
        optionmenu1.configure(width='40')
        optionmenu1.grid(column=1, row=1, sticky=tk.W)

        button_ok_client = ttk.Button(self)
        button_ok_client.configure(state='normal', text='OK')
        button_ok_client.grid(column=2, row=1, sticky=tk.W)
        button_ok_client.configure(command=self.ok_client)

        label3 = ttk.Label(self)
        label3.configure(text='')
        label3.grid(column=0, row=2, sticky=tk.W)

        connection.commit()
        cursor.close()

    def ok_client(self):
        self.client_id = self.client_ids[self.__values_nClient.index(self.__tkvar_nClient.get())]
        db = main.Data_Base()
        connection = db.connect()
        cursor = connection.cursor()

        label3 = ttk.Label(self)
        label3.configure(text='ID Echipament')
        label3.grid(column=0, row=3, sticky=tk.W)

        self.__values_idEch = []
        self.eq_ids = []
        age_res = cursor.execute("SELECT e.id_eq ,e.type FROM equipment e, clients c WHERE c.id_client = " + str(
            self.client_id) + " AND ((TRUNC(months_between(sysdate, c.birth_date) / 12) <18 AND e.age_restriction = 'YES')OR(TRUNC(months_between(sysdate, c.birth_date) / 12) >18 AND e.age_restriction = 'NO'))" +
                                 "AND e.id_eq NOT IN(SELECT equipment_id_eq FROM rentals WHERE rental_date=to_date(to_char(sysdate, 'DD-MM-YYYY'), 'DD-MM-YYYY') AND rental_hour=trunc((sysdate - trunc(sysdate)) * 24) )")
        for row in age_res:
            self.__values_idEch.append(str(row[0]) + '  ' + str(row[1]))
            self.eq_ids.append(row[0])
        self.__tkvar_idEch = tk.StringVar(value='')
        optionmenu3 = tk.OptionMenu(self, self.__tkvar_idEch, *self.__values_idEch, command=None)
        optionmenu3.configure(width='40')
        optionmenu3.grid(column=1, row=3, sticky=tk.W)

        button_ok_eq = ttk.Button(self)
        button_ok_eq.configure(state='normal', text='OK')
        button_ok_eq.grid(column=2, row=3, sticky=tk.W)
        button_ok_eq.configure(command=self.ok_eq)

        label3 = ttk.Label(self)
        label3.configure(text='')
        label3.grid(column=0, row=4, sticky=tk.W)

        connection.commit()
        cursor.close()

    def ok_eq(self):

        button_adauga_inchiriere = ttk.Button(self)
        button_adauga_inchiriere.configure(state='normal', text='Adauga')
        button_adauga_inchiriere.grid(column=1, columnspan=2, row=5, sticky=tk.W)
        button_adauga_inchiriere.configure(command=self.adauga_inchiriere)
        message1 = tk.Message(self)
        db = main.Data_Base()
        connection = db.connect()
        cursor = connection.cursor()
        costs=cursor.execute("SELECT price_h FROM equipment WHERE id_eq="+str(self.eq_ids[self.__values_idEch.index(self.__tkvar_idEch.get())]))

        for cost in costs:
            pret = tk.StringVar(value='                 Pretul este de: ' + str(int(cost[0])) + ' lei')
            message1.configure(font=('TkSmallCaptionFont',15), justify='center',
                           text='                 Pretul este de: ' + str(int(cost[0])) + ' lei',
                           textvariable=pret)
            message1.configure(width='1000')
            message1.grid(columnspan=2, row=6, sticky=tk.W)

        connection.commit()
        cursor.close()

    def adauga_inchiriere(self):
        db = main.Data_Base()
        connection = db.connect()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO rentals(clients_id_client,employees_id_em,equipment_id_eq,rental_date,rental_hour) VALUES (" + str(
                self.client_id) + "," + str(self.master.employee_id) + "," + str(
                self.eq_ids[self.__values_idEch.index(self.__tkvar_idEch.get())]) + ",DEFAULT,DEFAULT)")
        print("S-a adaugat o inregistrare in rentals!")
        connection.commit()
        cursor.close()

    def back_to_menu(self):
        if self.master.employee_id == 1:
            self.master.switch_frame(PageMeniuriCEO.PageMeniuriCEO)
        else:
            self.master.switch_frame(PageMeniuriAngajat.PageMeniuriAngajat)



