from SQL_TWM_SAM import Banco_sql_twm
from NOSQL_RAVEN_GED_SAM import Banco_nosql_raven_ged
from DocParser_SAM import Parseamento_docparser

#                            Input sistema
list_clientes = ['twm_localiza', 'twm_riachuelo', 'twm_fleury', 'twm_pucminas']
list_vertical = []

for cliente in list_clientes:
#for vertical in list_vertical:
    twm_cliente = cliente 
    tipo_data = 'dt_vencimento'
    ano_mes = '202201'
    vertical_fatura = 4
    
    # Busca dos arquivos não saneados 
    try:
        tabela_twm = Banco_sql_twm.__init__(twm_cliente, tipo_data, ano_mes, vertical_fatura)
        print(cliente)
        print(tabela_twm)
    except:
        print('xxxxxxxxxxxxxxxxxxxx')
        print('Erro na busca TWM.')
        print('xxxxxxxxxxxxxxxxxxxx')
    
    
    # Busca dos PDFs no GED do Raven
    try:
        arquivo_pdf = Banco_nosql_raven_ged.__init__(tabela_twm) #ainda não chega o arquivo PDF aqui, tem que colocar em Bytes e dps converter
    except:
        print('xxxxxxxxxxxxxxxxxxxx')
        print('Erro na busca do GED.')
        print('xxxxxxxxxxxxxxxxxxxx')
        
        
    # Envia o arquivo PDF ao DocParser e retornar Json da fatura parseada
    try:
        json_parseado = Parseamento_docparser.__init__(arquivo_pdf, tabela_twm)
    except:
        print('xxxxxxxxxxxxxxxxxxxx')
        print('Erro de Parseamento do PDF.')
        print('xxxxxxxxxxxxxxxxxxxx')