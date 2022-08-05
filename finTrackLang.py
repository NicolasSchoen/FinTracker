
class FinTrackLang:
    """Language-Object containing localised text"""
    
    def __init__(self,lang="en") -> None:
        if(lang=="en"): self.__initializeEN()
        elif(lang=="de"): self.__initializeDE()

    def __initializeEN(self):
        """English Language support"""
        self.mainTitle = "FinTrack"
        self.addEntry = "Add Entry"
        self.addCategory = "Add Category"
        self.exit = "Exit"
        self.load = "Load"
        self.file = "File"

    def __initializeDE(self):
        """German Language support"""
        self.mainTitle = "FinTrack"
        self.addEntry = "Eintrag hinzufügen"
        self.addCategory = "Kategorie erstellen"
        self.exit = "Beenden"
        self.load = "Laden"
        self.file = "Datei"