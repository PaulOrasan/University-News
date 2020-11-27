import sqlite3
class Database:
    def __init__(self, dbName):
        '''
        Creates a database object by linking to the database referenced by dbName
        dbName - string that represents a sqlite database file
        '''
        self._connection = sqlite3.connect('links.sqlite')
        self._cursor = self._connection.cursor()

    def createTable(self):
        '''
        Creates table in database if table is not existent
        '''
        createCommand = 'CREATE TABLE IF NOT EXISTS links(' \
                        'address TEXT NOT NULL UNIQUE);'
        self._cursor.execute(createCommand)

    def insertTable(self,data):
        '''
        Executes insert SQL command
        '''
        insertCommand = ''.join(['INSERT OR IGNORE INTO links(address) VALUES ( \"', data, '\");'])
        self._cursor.execute(insertCommand)
        self._connection.commit()

    def checkIfExists(self, data):
        '''
        Checks if data exists anywhere in table links
        Returns True if data already exists
        '''
        selectCommand = ''.join(['SELECT address from links WHERE address = \"',data,'\"'])
        self._cursor.execute(selectCommand)
        return self._cursor.fetchone() != None

    def close(self):
        self._cursor.close()