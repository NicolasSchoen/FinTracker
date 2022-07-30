import tkinter as tk
import finTrackDao

class FinTrackGUI:
    def __init__(self) -> None:
        self.InitializeDatabase()
        self.BuildUi()

    def BuildUi(self):
        # initialization of GUI
        # TODO
        self.app = tk.Tk()

    def StartUI(self):
        self.app.mainloop()

    def InitializeDatabase(self):
        # TODO
        self.dataBase = finTrackDao.FinTrackDAO()





if __name__ == "__main__":
    print("starting FinTrack")

    finTrackApp = FinTrackGUI()