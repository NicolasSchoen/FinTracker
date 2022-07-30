
class FinTrackLang:
    """Language-Object containing localised text"""
    
    def __init__(self,lang="en") -> None:
        if(lang=="en"): self.__initializeEN()
        elif(lang=="de"): self.__initializeDE()

    def __initializeEN(self):
        """English Language support"""
        self.mainTitle = "FinTrack"

    def __initializeDE(self):
        """German Language support"""
        self.mainTitle = "FinTrack"