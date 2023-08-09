import main
import tkinter as tk
import tkinter.ttk as ttk
import PageMeniuriCEO,PageMeniuriAngajat


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(0, weight=10)
        self.columnconfigure(0, weight=2)
        db = main.Data_Base()
        self.__values = []
        self.ids = []
        connection = db.connect()
        cursor = connection.cursor()
        cursor.execute("UPDATE EMPLOYEES SET hours_worked=0 WHERE TO_CHAR(SYSDATE,'DD')='01'")
        rows = cursor.execute("SELECT id_em,first_name ||' '|| last_name FROM employees WHERE hours_worked is not NULL ORDER BY id_em ASC")
        for row in rows:
            self.__values.append(str(row[1]))
            self.ids.append(row[0])
        labelgol1 = ttk.Label(self)
        labelgol1.configure(anchor='n', text='           ')
        labelgol1.grid(row=0, column=0)

        labelgol2 = ttk.Label(self)
        labelgol2.configure(anchor='n', text='           ')
        labelgol2.grid(row=0, column=3)

        label = ttk.Label(self)
        label.configure(anchor='n', text='Va rugam selectati angajatul')
        label.grid(row=1, column=1)
        self.__tkvar = tk.StringVar(self, 'Ioana Prioteasa')

        labelgol3 = ttk.Label(self)
        labelgol3.configure(anchor='n', text='           ')
        labelgol3.grid(row=2, column=0)
        labelgol4 = ttk.Label(self)
        labelgol4.configure(anchor='n', text='           ')
        labelgol4.grid(row=3, column=0)

        angajati_menu = tk.OptionMenu(self, self.__tkvar, *self.__values)
        angajati_menu.configure(width='40')
        angajati_menu.grid(row=4, column=1)

        labelgol5 = ttk.Label(self)
        labelgol5.configure(anchor='n', text='           ')
        labelgol5.grid(row=5, column=0)
        labelgol6 = ttk.Label(self)
        labelgol6.configure(anchor='n', text='           ')
        labelgol6.grid(row=6, column=0)

        button = ttk.Button(self, style='Accent.TButton', command=self.selectie_angajat)
        button.configure(text='OK')
        button.grid(row=7, column=1)

        connection.commit()
        cursor.close()

    def selectie_angajat(self):
        db = main.Data_Base()
        connection = db.connect()
        cursor = connection.cursor()

        self.master.employee_id = self.ids[self.__values.index(self.__tkvar.get())]
        if self.master.employee_id == 1:
            self.master.switch_frame(PageMeniuriCEO.PageMeniuriCEO)
        else:
            self.master.switch_frame(PageMeniuriAngajat.PageMeniuriAngajat)

        cursor.execute("UPDATE EMPLOYEES SET hours_worked=hours_worked+8 WHERE id_em=" + str(self.master.employee_id))
        connection.commit()
        cursor.close()

