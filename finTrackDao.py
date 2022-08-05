
class FinTrackDAO:
    """Data-Access-Object to handle usage of Database"""
    
    def __init__(self) -> None:
        # TODO
        self.__loadDatabase()
        pass

    def __loadDatabase(self):
        # TODO
        pass

    def addExpense(self,amount,timeStamp,recurring=False,category=None):
        """Add new Expense to Database
        Parameters:
            -amount: Amount of expense
            -recurring: single expense or recurring expenses
            -category: Category of expense"""
        # TODO
        pass

    def addIncome(self,amount,timeStamp,recurring=False):
        """Add new Income
        Parameters:
            -amount: Amount of income
            -recurring: single income or recurring income"""
        # TODO
        pass

    def addCategory(self,categoryName):
        """Add new Category for Expenses"""
        # TODO
        pass

    def getMonthlyOverview(self,timeStamp):
        """returns List of ..."""
        # TODO
        return []

    def getCategoryOverview(self,category):
        """returns List of ..."""
        # TODO
        return[]