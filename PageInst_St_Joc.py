import main
import PageMeniuriCEO
import PageMeniuriAngajat
import tkinter as tk
import tkinter.ttk as ttk

class PageInst_St_Joc(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=400, height=400)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        button_back = ttk.Button(self)
        button_back.configure(state='normal', text='Inapoi la meniu')
        button_back.grid(column=0, row=0, sticky=tk.W)
        button_back.configure(command=self.back_to_menu)

        label1 = ttk.Label(self)
        label1.configure(text='Operatiunea dorita')
        label1.grid(column=0, row=1, sticky=tk.W)

        self.__values_o = ['Instalare', 'Stergere']
        self.__tkvar_o = tk.StringVar(value='')
        optionmenu = tk.OptionMenu(self, self.__tkvar_o, *self.__values_o, command=None)
        optionmenu.configure(width='40')
        optionmenu.grid(column=1, row=1, sticky=tk.W)

        button_ok_o = ttk.Button(self)
        button_ok_o.configure(state='normal', text='OK')
        button_ok_o.grid(column=2, row=1, sticky=tk.W)
        button_ok_o.configure(command=self.ok_o)

    def ok_o(self):
        if self.__tkvar_o.get() == 'Instalare':
            self.instaleaza()
        elif self.__tkvar_o.get() == 'Stergere':
            self.sterge()

    def back_to_menu(self):
        if self.master.employee_id == 1:
            self.master.switch_frame(PageMeniuriCEO.PageMeniuriCEO)
        else:
            self.master.switch_frame(PageMeniuriAngajat.PageMeniuriAngajat)

    def instaleaza(self):
        db = main.Data_Base()
        connection = db.connect()
        cursor = connection.cursor()

        label1 = ttk.Label(self)
        label1.configure(text='Echipament')
        label1.grid(column=0, row=2, sticky=tk.W)

        self.__values_idEch = []
        self.eq_ids = []
        age_res = cursor.execute("SELECT e.id_eq ,e.type FROM equipment e ORDER BY e.id_eq ASC")
        for row in age_res:
            self.__values_idEch.append(str(row[0]) + '  ' + str(row[1]))
            self.eq_ids.append(row[0])
        self.__tkvar_idEch = tk.StringVar(value='')
        optionmenu1 = tk.OptionMenu(self, self.__tkvar_idEch, *self.__values_idEch, command=None)
        optionmenu1.configure(width='40')
        optionmenu1.grid(column=1, row=2, sticky=tk.W)

        button_ok_e = ttk.Button(self)
        button_ok_e.configure(state='normal', text='OK')
        button_ok_e.grid(column=2, row=2, sticky=tk.W)
        button_ok_e.configure(command=self.ok_e)

        connection.commit()
        cursor.close()

    def ok_e(self):
        db = main.Data_Base()
        connection = db.connect()
        cursor = connection.cursor()

        label1 = ttk.Label(self)
        label1.configure(text='Joc')
        label1.grid(column=0, row=3, sticky=tk.W)
        self.__values_game = []
        self.game_ids = []
        games = cursor.execute(
            "SELECT g.g_name, g.id_game FROM games g, equipment e WHERE g.age_restriction = e.age_restriction AND e.id_eq=" +
            str(self.eq_ids[self.__values_idEch.index(self.__tkvar_idEch.get())]) +
            "AND g.id_game not in(SELECT f.games_id_game FROM games_eq_fk f WHERE f.equipment_id_eq =" + str(
                self.eq_ids[self.__values_idEch.index(self.__tkvar_idEch.get())]) + ")")
        for game in games:
            self.__values_game.append(str(game[0]))
            self.game_ids.append((game[1]))
        self.__tkvar_game = tk.StringVar(value='')
        optionmenu1 = tk.OptionMenu(self, self.__tkvar_game, *self.__values_game, command=None)
        optionmenu1.configure(width='40')
        optionmenu1.grid(column=1, row=3, sticky=tk.W)

        button_instaleaza = ttk.Button(self)
        button_instaleaza.configure(state='normal', text='Adauga')
        button_instaleaza.grid(column=1, row=4, sticky=tk.W)
        button_instaleaza.configure(command=self.adauga_instalare)

        connection.commit()
        cursor.close()

    def adauga_instalare(self):
        db = main.Data_Base()
        connection = db.connect()
        cursor = connection.cursor()
        id_echipament = self.__tkvar_idEch.get().split(" ")[0]
        cursor.execute("INSERT INTO games_eq_fk VALUES(" + str(
            self.game_ids[self.__values_game.index(self.__tkvar_game.get())]) + "," + id_echipament + ")")
        print("S-a adaugat o inregistrare in games_eq_fk")
        connection.commit()
        cursor.close()

    def sterge(self):
        db = main.Data_Base()
        connection = db.connect()
        cursor = connection.cursor()

        label1 = ttk.Label(self)
        label1.configure(text='Echipament')
        label1.grid(column=0, row=2, sticky=tk.W)

        self.__values_idEch2 = []
        self.eq_ids2 = []
        age_res = cursor.execute("SELECT e.id_eq ,e.type FROM equipment e ORDER BY e.id_eq ASC")
        for row in age_res:
            self.__values_idEch2.append(str(row[0]) + '  ' + str(row[1]))
            self.eq_ids2.append(row[0])
        self.__tkvar_idEch2 = tk.StringVar(value='')
        optionmenu1 = tk.OptionMenu(self, self.__tkvar_idEch2, *self.__values_idEch2, command=None)
        optionmenu1.configure(width='40')
        optionmenu1.grid(column=1, row=2, sticky=tk.W)

        button_ok_e = ttk.Button(self)
        button_ok_e.configure(state='normal', text='OK')
        button_ok_e.grid(column=2, row=2, sticky=tk.W)
        button_ok_e.configure(command=self.ok_e_sterge)

        connection.commit()
        cursor.close()

    def ok_e_sterge(self):
        db = main.Data_Base()
        connection = db.connect()
        cursor = connection.cursor()

        label1 = ttk.Label(self)
        label1.configure(text='Joc')
        label1.grid(column=0, row=3, sticky=tk.W)

        self.__values_game2 = []
        self.game_ids2 = []
        games = cursor.execute(
            "SELECT g.g_name, g.id_game FROM games g, games_eq_fk e WHERE e.equipment_id_eq="
            + str(self.eq_ids2[self.__values_idEch2.index(self.__tkvar_idEch2.get())]) +
            " AND g.id_game=e.games_id_game")
        for game in games:
            self.__values_game2.append(str(game[0]))
            self.game_ids2.append((game[1]))
        self.__tkvar_game2 = tk.StringVar(value='')
        optionmenu1 = tk.OptionMenu(self, self.__tkvar_game2, *self.__values_game2, command=None)
        optionmenu1.configure(width='40')
        optionmenu1.grid(column=1, row=3, sticky=tk.W)

        button_instaleaza = ttk.Button(self)
        button_instaleaza.configure(state='normal', text='Sterge')
        button_instaleaza.grid(column=1, row=4, sticky=tk.W)
        button_instaleaza.configure(command=self.adauga_stergere)

        connection.commit()
        cursor.close()

    def adauga_stergere(self):
        db = main.Data_Base()
        connection = db.connect()
        cursor = connection.cursor()
        id_echipament = self.__tkvar_idEch2.get().split(" ")[0]
        cursor.execute("DELETE FROM games_eq_fk WHERE games_id_game=" + str(
            self.game_ids2[self.__values_game2.index(self.__tkvar_game2.get())])
                       + " AND equipment_id_eq=" + id_echipament)
        print("S-a sters din games_eq_fk")
        connection.commit()
        cursor.close()

