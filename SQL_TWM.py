import pyodbc 
import pandas as pd
from sqlalchemy import create_engine
#import display

#conectando ao server SQL
server = '177.70.121.163' 
database = 'twm_localiza' 
username = 'u_victor_magalhaes' 
password = 'Vi@haha270596' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)


#retornando banco na busca  *obs: tipo: pyodbc.Cursor 
cursor = cnxn.cursor()
print(cursor, type(cursor))


sql = 'SELECT * FROM dbo.t_fatura_base fatura'

# Query into dataframe
df= pd.io.sql.read_sql(sql, cnxn)

#display(df.head())
print(df.head())

'-------------------------------------------------------------------------------------------------------------------------'
# from sqlalchemy import create_engine
# import pandas

# # Postgres username, password, and database name
# POSTGRES_ADDRESS = '177.70.121.163' ## INSERT YOUR DB ADDRESS IF IT'S NOT ON PANOPLY
# POSTGRES_PORT = '5439'
# POSTGRES_USERNAME = 'u_victor_magalhaes' ## CHANGE THIS TO YOUR PANOPLY/POSTGRES USERNAME
# POSTGRES_PASSWORD = 'Vi@haha270596' ## CHANGE THIS TO YOUR PANOPLY/POSTGRES PASSWORD
# POSTGRES_DBNAME = 'twm_localiza' ## CHANGE THIS TO YOUR DATABASE NAME
# # A long string that contains the necessary Postgres login information
# postgres_str = ('postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'
# .format(username=POSTGRES_USERNAME,
# password=POSTGRES_PASSWORD,
# ipaddress=POSTGRES_ADDRESS,
# port=POSTGRES_PORT,
# dbname=POSTGRES_DBNAME))
# # Create the connection
# cnx = create_engine(postgres_str)




# df = pandas.read_sql_query('SELECT * FROM dbo.t_fatura_base fatura', con=cnx)


