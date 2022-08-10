
class FinTrackLang:
    """Language-Object containing localised text"""
    
    def __init__(self,lang="en") -> None:
        if(lang=="en"): self.__initializeEN()
        elif(lang=="de"): self.__initializeDE()

    def __initializeEN(self):
        """English Language support"""
        self.abort = "Abort"
        self.addCategory = "Add Category"
        self.addEntry = "Add Entry"
        self.categoryName = "Category Name"
        self.entryAmount = "Entry Amount:"
        self.entryCategory = "Category:"
        self.entryMonthly = "monthly (otherwise yearly):"
        self.entryName = "Entry Name:"
        self.entryRecurring = "Recurring:"
        self.entryTimeStamp = "Date of Entry:"
        self.errorAddCategory = "Error When Creating Category"
        self.exit = "Exit"
        self.file = "File"
        self.load = "Load"
        self.mainTitle = "FinTrack"
        self.options = "Options"
        self.save = "Save"
        self.tabGraphic = "Graphic"
        self.tabTable = "Table"

    def __initializeDE(self):
        """German Language support"""
        self.abort = "Abbrechen"
        self.addCategory = "Kategorie erstellen"
        self.addEntry = "Eintrag hinzufügen"
        self.categoryName = "Kategoriename"
        self.entryAmount = "Betrag des Eintrags:"
        self.entryCategory = "Kategorie:"
        self.entryMonthly = "monatlich (sonst jährlich):"
        self.entryName = "Name des Eintrags:"
        self.entryRecurring = "Wiederholend:"
        self.entryTimeStamp = "Datum des Eintrags:"
        self.errorAddCategory = "Fehler bei Erstellung neuer Kategorie"
        self.exit = "Beenden"
        self.file = "Datei"
        self.load = "Laden"
        self.mainTitle = "FinTrack"
        self.options = "Optionen"
        self.save = "Speichern"
        self.tabGraphic = "Grafik"
        self.tabTable = "Tabelle"