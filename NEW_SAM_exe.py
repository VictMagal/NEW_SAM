from NOSQL_RavenDB import QueryNOSQL
from SQL_TWM import QuerySQL
from GED_File import QueryGED
import csv
import json
from json import dumps
import pandas as pd
import pickle
import openpyxl

class Execute_search ():
    def __init__(self):
        print('---------------- DADOS ----------------')
        self.cliente = 'twm_localiza'
        self.mes_emissao = '202201'
        print(self.cliente)
        print(self.mes_emissao)
        
        self.query_dbo_t_fatura_base = '''
                                        SELECT  *
                                        FROM    dbo.t_fatura_base fatura
                                                INNER JOIN dbo.t_conta_aglutinada_base conta ON conta.id_conta_aglutinada_base = fatura.id_conta_aglutinada_base
                                                INNER JOIN dbo.t_tipo_conta tipo_conta ON tipo_conta.id_tipo_conta = conta.id_tipo_conta
                                                INNER JOIN dbo.t_vertical vertical ON vertical.id_vertical = tipo_conta.id_vertical
                                                LEFT JOIN dbo.t_valor_fatura valor_fatura ON valor_fatura.id_fatura = fatura.id_fatura_base
                                                                                             AND valor_fatura.id_campo_fatura = 4
                                        
                                        WHERE   (valor_fatura.dc_valor_fatura = 'Não'
                                                  OR valor_fatura.dc_valor_fatura IS NULL
                                                )
                                                AND tipo_conta.id_vertical = 2
                                                AND conta.ic_aprovada=1 AND SUBSTRING(CONVERT(CHAR(8),dt_emissao,112),1,6)='valor_data'
                                        '''
        
        self.query_t_arquivo_ged = '''
                                       SELECT   *
                                       FROM     t_arquivo_ged 
                                       
                                       WHERE    id_ged = 'valor_id_ged'
                                   '''
    def string_to_float(self, valor):
        if valor == '':
            valor = float(0)
        
        if type(valor) == str:    
            string2 = '!.#%'
            char_rep = {k: '' for k in string2}
            valor =valor.translate(str.maketrans(char_rep))
            valor = float(valor.replace (',','.'))
            
        else:
            valor = float(valor)
            
        valor = "{:.2f}".format(valor)
        return float(valor)
    def query_sql_start (self):
        print('----------------- SQL -----------------')
        QuerySQL_start = QuerySQL()
        QuerySQL_start.setUpsql(self.cliente)
        tabela_twm = QuerySQL_start.query(self.query_dbo_t_fatura_base.replace('valor_data', self.mes_emissao))
        
        if len(tabela_twm.index) == 0:
            print('Aviso: Nenhuma Fatura encontrada no TWM.')    
        else:
            True
#------------------------------FAZ UMA FATURA POR VEZ, PARA FAZER VÁRIAS ADAPTAR
        i = 0
        self.nu_fatura_base = tabela_twm.nu_fatura_base[i]
        self.id_ged = tabela_twm.id_ged[i]
        self.conta_aglutinada = tabela_twm.nu_cliente_base[i]
        self.dt_vencimento = str(tabela_twm.dt_vencimento[i]).replace('-', '')
        
        tabela_id_raven = QuerySQL_start.query(self.query_t_arquivo_ged.replace('valor_id_ged', self.id_ged))      
        self.id_raven = tabela_id_raven.id_raven[i]
       
        print('----------------- INFO ----------------')
        print('id_ged_no_twm:', self.id_ged)
        print('id_ged_no_raven:', self.id_raven)
        print('nu_fatura_base:', self.nu_fatura_base)
        print('conta_aglutinada:', self.conta_aglutinada)
        print('dt_vencimento:', self.dt_vencimento)
        
    def query_nosql_start (self):
        print('---------------- NOSQL ----------------')
        # Executando query para cada fatura pendente que veio do TWM e preenchendo dict com os valores parseados
        QueryNOSQL_start = QueryNOSQL()
        QueryNOSQL_start.setUpnosql()
        
        dia = self.dt_vencimento[6:]
        mes = self.dt_vencimento[4:6]
        ano = self.dt_vencimento[:4]
        self.dt_vencimento_Raven = (dia+'/'+mes+'/'+ano)
        
        print('identificador_twm: ', self.nu_fatura_base)
        print('conta_aglutinada: ', self.conta_aglutinada)
        print('dt_vencimento_Ravn: ', self.dt_vencimento)

        query_results = QueryNOSQL_start.query(str(self.conta_aglutinada), str(self.dt_vencimento_Raven))
        
        valor_total_fatura = query_results[0].vl_total
        valores_faturados_auditoria = query_results[0].valores_faturados_auditoria
        
        valor_total_fatura = Execute_search().string_to_float(valor_total_fatura)
        
        soma_valores_auditoria =float(0)
        for i in range(len(valores_faturados_auditoria)):
            valores_faturados_auditoria[i]['valor'] = Execute_search().string_to_float(valores_faturados_auditoria[i]['valor'])
            soma_valores_auditoria += valores_faturados_auditoria[i]['valor']
        
        soma_valores_auditoria  = Execute_search().string_to_float(soma_valores_auditoria)  
        
        if valor_total_fatura == soma_valores_auditoria:
            print('VALOR CORRETO!!')
            print('valor_total_fatura = ',valor_total_fatura)
            print('soma_valores_auditoria = ', soma_valores_auditoria)
        else:
            print('VALOR ERRADO!!')
            print('valor_total_fatura = ',valor_total_fatura)
            print('soma_valores_auditoria = ', soma_valores_auditoria)
        
        self.json_parseado = query_results[0]
        
    def query_GED_start (self):
        print('---------------- GED ----------------')   
        fatura_ged = self.id_raven
        Query_activeGED = QueryGED()
        Query_activeGED.setUpged()
        self.teste = Query_activeGED.get_attachmentoperation("GED", str(fatura_ged))
        
        
        teste = self.teste
        print(teste, '-' , type(teste))
        bytes = pickle.dumps(teste)
        print(bytes)
        
    def json_parser_to_csv(self):
        self.json_parseado = json.dumps(self.json_parseado.__dict__)
        self.json_parseado = json.loads(self.json_parseado)
        
        consolidado_json = []
        consolidado_pandas = []
        consolidado_csv = []
        
        print(pd.DataFrame.from_dict(self.json_parseado, orient='index'))
        
    def col_parser_to_col_consolidado(self, cliente, json_parseado):
        
        json_localiza = []
        json_riachuelo = []
        json_fleury = []
        json_puc = []
       
        
        wb = openpyxl.load_workbook('arquivo_linkado.xlsx')
        ws = wb['Worksheet']
        
        list_localiza1 = []
        list_localiza2 = []
        list_riachuelo1 = []
        list_riachuelo2 = []
        list_fleury1 = []
        list_fleury2 = []
        list_puc1 = []
        list_puc2 = []
        
        
        is_data = True
        count_row_twm = 1
        while is_data:
            count_row_twm += 1
            data =  ws.cell (row = count_row_twm, column = 1).value
            list_localiza1.append(data)
            data =  ws.cell (row = count_row_twm, column = 2).value
            list_localiza2.append(data)
            data =  ws.cell (row = count_row_twm, column = 3).value
            list_fleury1.append(data)
            data =  ws.cell (row = count_row_twm, column = 4).value
            list_fleury2.append(data)
            data =  ws.cell (row = count_row_twm, column = 5).value
            list_riachuelo1.append(data)
            data =  ws.cell (row = count_row_twm, column = 6).value
            list_riachuelo2.append(data)
            data =  ws.cell (row = count_row_twm, column = 7).value
            list_puc1.append(data)
            data =  ws.cell (row = count_row_twm, column = 8).value
            list_puc2.append(data)
            
            if data == None:
                is_data = False
                
        count_row_twm -=1
        count_row_twm = count_row_twm     
        
        
        print(count_row_twm)
        
        print(list_localiza1)
        print(list_localiza2)
        print(list_puc2)
        
        #CRIAR DICT DAS LISTAS E FÉ
        





       
    
    
    
Execute_search_start = Execute_search()
Execute_search_start.query_sql_start()
Execute_search_start.query_GED_start()
Execute_search_start.query_nosql_start()
Execute_search_start.json_parser_to_csv()
Execute_search_start.col_parser_to_col_consolidado(None,None)



