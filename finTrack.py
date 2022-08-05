import os
import tkinter as tk
import tkinter.ttk as ttk
import finTrackDao
import finTrackLang

class FinTrackGUI:
    def __init__(self) -> None:
        self.__loadLocalizedTexts()
        self.__initializeDatabase()
        self.__buildUi()

    def __loadLocalizedTexts(self):
        # TODO
        self.txt = finTrackLang.FinTrackLang()

    def __initializeDatabase(self):
        # TODO
        self.dataBase = finTrackDao.FinTrackDAO()

    def __clickedAddEntry(self):
        # TODO
        print("clicked Add Entry!")

    def __clickedAddCategory(self):
        # TODO
        print("clicked Add Category!")

    def __buildUi(self):
        # TODO
        self.app = tk.Tk()
        self.app.title(self.txt.mainTitle)
        self.app.geometry('800x500')
        self.app.iconbitmap(os.path.join(os.path.dirname(__file__),"resources/icon.ico"))

        #Menubar initialization
        self.menubar = tk.Menu(self.app)

        self.filemenu = tk.Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label=self.txt.load)
        self.filemenu.add_command(label=self.txt.exit,command=lambda: self.app.quit())

        self.menubar.add_cascade(label=self.txt.file, menu=self.filemenu)

        self.app.config(menu=self.menubar)



        self.btnAddEntry = ttk.Button(
            self.app,
            text=self.txt.addEntry,
            command=self.__clickedAddEntry
        )
        self.btnAddEntry.grid(
            column=0,
            row=0,
            ipadx=10,
            ipady=10,
            sticky="EW"
        )

        self.btnAddCategory = ttk.Button(
            self.app,
            text=self.txt.addCategory,
            command=self.__clickedAddCategory
        )
        self.btnAddCategory.grid(
            column=0,
            row=1,
            ipadx=10,
            ipady=10,
            sticky="EW"
        )

    def StartUI(self):
        """Starts TK-App"""
        self.app.mainloop()





if __name__ == "__main__":
    print("starting FinTrack")

    finTrackApp = FinTrackGUI()
    finTrackApp.StartUI()
