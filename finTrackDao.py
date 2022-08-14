import os
import sqlite3

class FinTrackDAO:
    """Data-Access-Object to handle usage of Database"""
    
    def __init__(self,type="local") -> None:
        # TODO
        if(not os.path.exists(os.path.join(os.path.dirname(__file__),"userdata"))):
            os.mkdir(os.path.join(os.path.dirname(__file__),"userdata"))

        self.__loadDatabase()

    def __loadDatabase(self):
        self.filename = os.path.join(os.path.dirname(__file__),"userdata/findata.db")
        self.CreateDatabase()

    def CreateDatabase(self):
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        try:
            c.execute('''CREATE TABLE IF NOT EXISTS finData
                                (id INTEGER primary key, description TEXT, amount FLOAT, timestamp DATE, recurring BOOLEAN, isMonthly BOOLEAN, category TEXT)''')

            c.execute('''CREATE TABLE IF NOT EXISTS finCategorys
                                (categoryName text primary key)''')
        except sqlite3.OperationalError:
            print("Database Creation not successfull!")
        conn.commit()
        conn.close()

    def getCategorys(self):
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()

        retCategorys = []

        for row in c.execute('''SELECT * FROM finCategorys ORDER BY categoryName ASC'''):
            retCategorys.append(row[0])

        conn.commit()
        conn.close()
        return retCategorys

    def addExpense(self,description,amount,timeStamp,recurring=False,isMonthly=True,category=None):
        """Add new Expense to Database
        Parameters:
            -description: Description of Expense
            -amount: Amount of expense
            -timeStamp: Time of Expense
            -recurring: single expense or recurring expenses
            -isMonthly: monthly or yearly
            -category: Category of expense"""
        # TODO test
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()

        try:
            c.execute("INSERT INTO finData (description,amount,timestamp,recurring,isMonthly,category) VALUES(?,?,?,?,?,?)",
            (description,-amount,timeStamp,recurring,isMonthly,category))
        except sqlite3.OperationalError:
            return (False,"Database Error!")
        except sqlite3.IntegrityError:
            return (False,"Expense already exists!")
        except:
            print("other error!")

        conn.commit()
        conn.close()
        return (True,)

    def addIncome(self,description,amount,timeStamp,recurring=False,isMonthly=True):
        """Add new Income
        Parameters:
            -description: Description of income
            -amount: Amount of income
            -timeStamp: Time of Income
            -recurring: single income or recurring income
            -isMonthly: monthly or yearly"""
        # TODO test
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()

        try:
            c.execute("INSERT INTO finData (description,amount,timestamp,recurring,isMonthly) VALUES(?,?,?,?,?)",
            (description,amount,timeStamp,recurring,isMonthly))
        except sqlite3.OperationalError:
            return (False,"Database Error!")
        except sqlite3.IntegrityError:
            return (False,"Income already exists!")

        conn.commit()
        conn.close()
        return (True,)

    def addCategory(self,categoryName):
        """Add new Category for Expenses
            -categoryName: Name of Category"""
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()

        try:
            c.execute("INSERT INTO finCategorys VALUES(?)",(categoryName,))
        except sqlite3.OperationalError:
            return (False,"Database Error!")
        except sqlite3.IntegrityError:
            return (False,"Category already exists!")

        conn.commit()
        conn.close()
        return (True,)

    def getMonthlyOverview(self,month,year):
        """returns List of ..."""
        # TODO
        return []

    def getCategoryOverview(self,category):
        """returns List of ..."""
        # TODO
        return[]