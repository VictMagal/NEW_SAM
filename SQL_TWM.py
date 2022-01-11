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





query = 'SELECT * FROM dbo.t_fatura_base fatura,' \
                     'INNER JOIN dbo.t_conta_aglutinada_base conta ON conta.id_conta_aglutinada_base = fatura.id_conta_aglutinada_base' \
                     'INNER JOIN dbo.t_tipo_conta tipo_conta ON tipo_conta.id_tipo_conta = conta.id_tipo_conta' \ 
                     'INNER JOIN dbo.t_vertical vertical ON vertical.id_vertical = tipo_conta.id_vertical' \
                    'LEFT JOIN dbo.t_valor_fatura valor_fatura ON valor_fatura.id_fatura = fatura.id_fatura_base AND valor_fatura.id_campo_fatura = 4,' \
                    'WHERE   ( valor_fatura.dc_valor_fatura = Não' \
                    'OR valor_fatura.dc_valor_fatura IS NULL)' \
                    'AND tipo_conta.id_vertical = 2' \
                    'AND conta.ic_aprovada=1 AND SUBSTRING(CONVERT(CHAR(8),dt_emissao,112),1,6) = 202201'



QuerySQL_start = QuerySQL()
QuerySQL_start.setUp('twm_localiza')
QuerySQL_start.query(query)







'-------------------------------------------------------------------------------------------------------------------------'


