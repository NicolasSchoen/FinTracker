import os
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk
import finTrackDao
import finTrackLang

class AddEntryWindow:
    def __init__(self,context) -> None:
        self.context = context
        self.newWindow = tk.Toplevel(context.app)
        self.newWindow.title(context.txt.addEntry)
        self.newWindow.geometry("400x200")
        #self.newWindow.rowconfigure(0,weight=1)
        self.newWindow.columnconfigure(0,weight=1)

        self.newWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.entrAddEntryName = ttk.Entry(self.newWindow,justify='center')
        self.entrAddEntryName.grid(
            column=0,
            row=0,
            ipady=5,
            padx=10,
            pady=2,
            sticky="EW"
        )
        self.entrAddEntryName.focus()

        self.btnCreateEntry = ttk.Button(self.newWindow,text=context.txt.addEntry,command=self.clickAddEntry)
        self.btnCreateEntry.grid(
            column=0,
            row=1,
            ipady=5,
            padx=10,
            pady=2,
            sticky="EW"
        )

        btnAbort = ttk.Button(self.newWindow,text=context.txt.abort,command=self.closeWindow)
        btnAbort.grid(
            column=0,
            row=2,
            ipady=5,
            padx=10,
            pady=2,
            sticky="EW"
        )

    def closeWindow(self):
        self.context.btnAddEntry.configure(state='normal')
        self.newWindow.destroy()

    def clickAddEntry(self):
        #TODO
        self.closeWindow()

class AddCategoryWindow:
    def __init__(self,context) -> None:
        self.context = context
        self.newWindow = tk.Toplevel(context.app)
        self.newWindow.title(context.txt.addCategory)
        self.newWindow.geometry("400x200")
        self.newWindow.columnconfigure(0,weight=1)

        self.newWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.entrAddCategoryName = ttk.Entry(self.newWindow,justify='center')
        self.entrAddCategoryName.grid(
            column=0,
            row=0,
            ipady=5,
            padx=10,
            pady=2,
            sticky="EW"
        )
        self.entrAddCategoryName.focus()

        self.btnCreateCategory = ttk.Button(self.newWindow,text=context.txt.addCategory,command=self.clickAddCategory)
        self.btnCreateCategory.grid(
            column=0,
            row=1,
            ipady=5,
            padx=10,
            pady=2,
            sticky="EW"
        )

        self.btnAbort = ttk.Button(self.newWindow,text=context.txt.abort,command=self.closeWindow)
        self.btnAbort.grid(
            column=0,
            row=2,
            ipady=5,
            padx=10,
            pady=2,
            sticky="EW"
        )

    def closeWindow(self):
        self.context.btnAddCategory.configure(state='normal')
        self.newWindow.destroy()
        
    def clickAddCategory(self):
        categoryName = str(self.entrAddCategoryName.get())

        success = self.context.dataBase.addCategory(categoryName)
        if(success[0]): self.closeWindow()
        if(not success[0]):
            messagebox.showinfo(self.context.txt.errorAddCategory,success[1])

class FinTrackGUI:
    def __init__(self):
        self.__loadLocalizedTexts()
        self.__initializeDatabase()
        self.__buildUi()

    def __loadLocalizedTexts(self,lang="en"):
        # TODO
        self.txt = finTrackLang.FinTrackLang(lang=lang)

    def __initializeDatabase(self):
        # TODO
        self.dataBase = finTrackDao.FinTrackDAO()

    def __clickedAddEntry(self):
        self.btnAddEntry.configure(state='disabled')
        AddEntryWindow(self)

    def __clickedAddCategory(self):
        self.btnAddCategory.configure(state='disabled')
        AddCategoryWindow(self)

    def __buildUi(self):
        # TODO
        self.app = tk.Tk()
        self.app.title(self.txt.mainTitle)
        self.app.geometry('800x500')
        self.app.iconbitmap(os.path.join(os.path.dirname(__file__),"resources/icon.ico"))
        self.app.columnconfigure(1,weight=1)
        self.app.rowconfigure(0,weight=1)

        #Menubar initialization
        self.menubar = tk.Menu(self.app)

        self.filemenu = tk.Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label=self.txt.save)
        self.filemenu.add_command(label=self.txt.load)
        self.filemenu.add_command(label=self.txt.options)
        self.filemenu.add_command(label=self.txt.exit,command=lambda: self.app.quit())

        self.menubar.add_cascade(label=self.txt.file, menu=self.filemenu)

        self.app.config(menu=self.menubar)


        self.frameMain = tk.Frame(self.app)
        self.frameMain.grid(
            column=0,
            row=0,
            sticky="N"
        )

        self.frameInfo = tk.Frame(self.app)
        self.frameInfo.grid(
            column=1,
            row=0,
            sticky="NSEW"
        )
        self.frameInfo.columnconfigure(0,weight=1)
        self.frameInfo.rowconfigure(0,weight=1)

        self.tabControl = ttk.Notebook(self.frameInfo)

        self.tabGraphic = ttk.Frame(self.tabControl) #TODO

        self.tabTable = ttk.Frame(self.tabControl) #TODO

        self.tabControl.add(self.tabGraphic, text=self.txt.tabGraphic)
        self.tabControl.add(self.tabTable, text=self.txt.tabTable)

        self.tabControl.grid(
            column=0,
            row=0,
            sticky="NSEW"
        )


        self.btnAddEntry = ttk.Button(
            self.frameMain,
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
            self.frameMain,
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
