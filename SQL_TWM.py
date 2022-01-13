import pyodbc 
import pandas as pd

class QuerySQL():
    def setUpsql (self, database):
        # Configurações de acesso ao SQL twm da guiabdo
        print('XXXXXXX... SQL...XXXXXXXXX')
        server = '177.70.121.163' 
        username = 'u_victor_magalhaes' 
        password = 'Vi@haha270596' 
        self.cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        self.cursor = self.cnxn.cursor()
          
    def query (self, sql):
        #Query no banco e retorna arquivo pd
        tabela_twm = pd.io.sql.read_sql(sql, self.cnxn)
        return tabela_twm











'-------------------------------------------------------------------------------------------------------------------------'


