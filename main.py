import tkinter as tk
import tkinter.ttk as ttk
import cx_Oracle
import StartPage


class Data_Base:
    def connect(self):
        connection = cx_Oracle.connect(user="BD044", password="Parolastudent",
                                       dsn="bd-dc.cs.tuiasi.ro:1539/orcl",
                                       encoding="UTF-8")
        return connection


class SampleApp(tk.Tk):
    def __init__(self):
        # Import the tcl file
        tk.Tk.__init__(self)
        self.tk.call('source', 'D:/An3Sem1/BD/TemaDeCasa/Forest-ttk-theme-master/forest-dark.tcl')
        self.employee_id = 0

        # Set the theme with the theme_use method
        ttk.Style().theme_use('forest-dark')
        self._frame = None
        self.switch_frame(StartPage.StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
