import json
import os

class FinTrackLang:
    """Language-Object containing localised text"""

    langFilePath = os.path.join(os.path.dirname(__file__),"resources/lang/en.json")

    englishDict = {
            "LanguageName": "English",
            "abort": "Abort",
            "addCategory": "Add Category",
            "addEntry": "Add Entry",
            "categoryName": "Category Name",
            "entryAmount": "Entry Amount:",
            "entryCategory": "Category:",
            "entryMonthly": "monthly (otherwise yearly):",
            "entryName": "Entry Name:",
            "entryRecurring": "Recurring:",
            "entryTimeStamp": "Date of Entry:",
            "errorAddCategory": "Error When Creating Category",
            "exit": "Exit",
            "file": "File",
            "load": "Load",
            "mainTitle": "FinTrack",
            "options": "Options",
            "save": "Save",
            "tabGraphic": "Graphic",
            "tabTable": "Table"
        }
    

    def __init__(self,lang="en") -> None:
        self.langDict = self.englishDict
        self.currentLanguage = self.langDict["LanguageName"]

        if(not os.path.exists(self.langFilePath)):
            self.__saveJson()

        self.getAllLanguages()
        
        if(lang!="en"): self.__switchLanguage(lang)


    def changeLanguage(self,languageName):
        """Switches Language for Text-Strings"""
        self.__switchLanguage(self.languages[languageName])


    def __switchLanguage(self,lang="en"):

        if(lang in self.languages.values()):
            self.__loadJson(lang)


    def getSelectedLanguage(self):
        return self.currentLanguage


    def getAllLanguages(self):
        self.languages = {}

        fileDir = os.path.join(os.path.dirname(__file__),"resources/lang/")
        onlyfiles = [f for f in os.listdir(fileDir) if os.path.isfile(os.path.join(fileDir, f))]

        for file in onlyfiles:
            with open(os.path.join(fileDir, file), 'r') as f:
                tmpLangDict = json.load(f)
                langShort = file.replace(os.path.join(os.path.dirname(__file__),"resources/lang/"),"")
                langShort = langShort.replace(".json","")
                self.languages[tmpLangDict["LanguageName"]] = langShort

        return self.languages


    def __loadJson(self,lang="en"):
        langFilePath = os.path.join(os.path.dirname(__file__),"resources/lang/"+lang+".json")

        with open(langFilePath, 'r') as f:
            self.langDict = json.load(f)


    def __saveJson(self,lang="en"):
        langFilePath = os.path.join(os.path.dirname(__file__),"resources/lang/"+lang+".json")

        with open(langFilePath, 'w') as f:
            json.dump(self.langDict, f, ensure_ascii=False, indent=4)


    def getText(self,txt):
        """returns Text"""
        return self.langDict[txt]
