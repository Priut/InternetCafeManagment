import main
import PageMeniuriCEO
import PageMeniuriAngajat
import tkinter as tk
import tkinter.ttk as ttk


class PageListaSalarii(tk.Frame):
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

        tree = ttk.Treeview(self, column=("ID", "Employee Name", "Payment/H", "Hours Worked", "Salary"),
                            show='headings', height=5)
        tree.column("# 1", anchor='center', width=35)
        tree.heading("# 1", text="ID")
        tree.column("# 2", anchor='center', width=100)
        tree.heading("# 2", text="Employee Name")
        tree.column("# 3", anchor='center', width=100)
        tree.heading("# 3", text="Payment/H")
        tree.column("# 4", anchor='center', width=95)
        tree.heading("# 4", text="Hours Worked")
        tree.column("# 5", anchor='center', width=95)
        tree.heading("# 5", text="Salary")

        rows = cursor.execute("SELECT id_em, first_name||' '||last_name, payment_h, hours_worked, payment_h * hours_worked FROM employees ORDER BY id_em")
        for row in rows:
            tree.insert('', 'end', text="1", values=(row[0], row[1], row[2], row[3], row[4]))

        tree.grid(row=1, column=0, columnspan=2, sticky=tk.W)

        connection.commit()
        cursor.close()

    def back_to_menu(self):
        if self.master.employee_id == 1:
            self.master.switch_frame(PageMeniuriCEO.PageMeniuriCEO)
        else:
            self.master.switch_frame(PageMeniuriAngajat.PageMeniuriAngajat)