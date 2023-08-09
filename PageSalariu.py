import main
import PageMeniuriCEO
import PageMeniuriAngajat
import tkinter as tk
import tkinter.ttk as ttk


class PageSalariu(tk.Frame):
    def __init__(self, master):
        # initializare frame
        tk.Frame.__init__(self, master, width=400, height=400)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

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
        label1.configure(text='   Detaliile tale de plata!')
        label1.grid(row=0, column=1, sticky=tk.W)

        label2 = ttk.Label(self)
        label2.configure(text='Numarul de ore lucrate')
        label2.grid(row=1,  column=0, sticky=tk.W)

        label3 = ttk.Label(self)
        label3.configure(text='Plata pe ora')
        label3.grid(row=2, column=0, sticky=tk.W)

        label3 = ttk.Label(self)
        label3.configure(text='Salariu acumulat')
        label3.grid(row=3, column=0, sticky=tk.W)
        rows=cursor.execute("SELECT hours_worked FROM employees WHERE id_em="+str(self.master.employee_id))
        for row in rows:
            label4 = ttk.Label(self)
            label4.configure(text='              '+str(row[0]))
            label4.grid(row=1, column=1, sticky=tk.W)

        rows = cursor.execute("SELECT payment_h FROM employees WHERE id_em=" + str(self.master.employee_id))
        for row in rows:
            label4 = ttk.Label(self)
            label4.configure(text='              '+str(row[0]))
            label4.grid(row=2, column=1, sticky=tk.W)

        rows = cursor.execute("SELECT payment_h*hours_worked FROM employees WHERE id_em=" + str(self.master.employee_id))
        for row in rows:
            label4 = ttk.Label(self)
            label4.configure(text='              '+str(row[0]))
            label4.grid(row=3, column=1, sticky=tk.W)

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
