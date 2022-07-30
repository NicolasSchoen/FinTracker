import tkinter as tk
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

    def __buildUi(self):
        # initialization of GUI
        # TODO
        self.app = tk.Tk()
        self.app.title(self.txt.mainTitle)

    def StartUI(self):
        """Starts TK-App"""
        self.app.mainloop()





if __name__ == "__main__":
    print("starting FinTrack")

    finTrackApp = FinTrackGUI()
    finTrackApp.StartUI()