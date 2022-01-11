import pyodbc 
import pandas as pd

print('XXXXXXX... SQL_TWM...XXXXXXXXXXXXX')
class QuerySQL():
    def setUp (self, database):
        # Configurações de acesso ao SQL twm da guiabdo
        server = '177.70.121.163' 
        username = 'u_victor_magalhaes' 
        password = 'Vi@haha270596' 
        self.cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        self.cursor = self.cnxn.cursor()
          
    def query (self, sql):
        #Query no banco e retorna arquivo pd
        df = pd.io.sql.read_sql(sql, self.cnxn)
        print(df.head())









QuerySQL_start = QuerySQL()
QuerySQL_start.setUp('twm_localiza')
QuerySQL_start.query(r"SELECT * FROM dbo.t_fatura_base fatura WHERE valor_fatura.dc_valor_fatura = 'Não'")


'-------------------------------------------------------------------------------------------------------------------------'


