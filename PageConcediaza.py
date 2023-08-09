import main
import PageMeniuriCEO
import PageMeniuriAngajat
import tkinter as tk
import tkinter.ttk as ttk


class PageConcediaza(tk.Frame):
    def __init__(self, master):
        # initializare frame
        tk.Frame.__init__(self, master, width=400, height=400)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)
        self.__values = []
        self.ids = []

        # initializare conexiune baza de date
        db = main.Data_Base()
        connection = db.connect()
        cursor = connection.cursor()

        # buton pentru a te intoarce la meniul principal
        button_back = ttk.Button(self)
        button_back.configure(state='normal', text='Inapoi la meniu')
        button_back.grid(column=0, row=0, sticky=tk.W)
        button_back.configure(command=self.back_to_menu)

        # label titlu
        label1 = ttk.Label(self)
        label1.configure(text='   Concediaza un angajat')
        label1.grid(row=0, column=1, sticky=tk.W)

        label2 = ttk.Label(self)
        label2.configure(text='Nume angajat')
        label2.grid(row=1, column=0, sticky=tk.W)

        rows = cursor.execute(
            "SELECT id_em,first_name ||' '|| last_name FROM employees WHERE hours_worked is not NULL AND id_em != 1 ORDER BY id_em ASC")
        for row in rows:
            self.__values.append(str(row[1]))
        self.__tkvar = tk.StringVar(self, '')

        angajati_menu = tk.OptionMenu(self, self.__tkvar, *self.__values)
        angajati_menu.configure(width='40')
        angajati_menu.grid(row=1, column=1)

        button_back = ttk.Button(self)
        button_back.configure(state='normal', text='Concediaza')
        button_back.grid(column=1, row=2, sticky=tk.W)
        button_back.configure(command=self.concediaza)

        label6 = ttk.Label(self)
        label6.configure(text='     ')
        label6.grid(row=0, column=2, sticky=tk.W)

        connection.commit()
        cursor.close()

    def back_to_menu(self):
        if self.master.employee_id == 1:
            self.master.switch_frame(PageMeniuriCEO.PageMeniuriCEO)
        else:
            self.master.switch_frame(PageMeniuriAngajat.PageMeniuriAngajat)

    def concediaza(self):
        db = main.Data_Base()
        connection = db.connect()
        cursor = connection.cursor()
        cursor.execute("UPDATE employees SET hours_worked=null WHERE first_name||' '||last_name='"+self.__tkvar.get()+
                       "'")
        connection.commit()
        cursor.close()

