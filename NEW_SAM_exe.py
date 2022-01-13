from NOSQL_RavenDB import QueryNOSQL
from SQL_TWM import QuerySQL
from GED_File import QueryGED

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

    def query_sql_start (self):
        print('----------------- SQL -----------------')
        QuerySQL_start = QuerySQL()
        QuerySQL_start.setUpsql(self.cliente)
        tabela_twm = QuerySQL_start.query(self.query_dbo_t_fatura_base.replace('valor_data', self.mes_emissao))
        
        if len(tabela_twm.index) == 0:
            print('Aviso: Nenhuma Fatura encontrada no TWM.')    
        else:
            #print(tabela_twm)    
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
        
        soma_valores_auditoria =float(0)
        
        for i in range(len(valores_faturados_auditoria)):
           
            if valores_faturados_auditoria[i]['valor'] == '':
                valores_faturados_auditoria[i]['valor'] = float(0)
                valor_auditoria = float(0)
           
            if type(valores_faturados_auditoria[i]['valor']) == str:
                
                string2 = '!.#%'
                char_rep = {k: '' for k in string2}
                
                valor_auditoria = valores_faturados_auditoria[i]['valor'].translate(str.maketrans(char_rep))
                valor_auditoria = float(valor_auditoria.replace (',','.'))
                
                
            
            else:
                valores_faturados_auditoria[i]['valor'] = float(valores_faturados_auditoria[i]['valor'])
           
            soma_valores_auditoria +=float(valor_auditoria)
   
    
        if valor_total_fatura == '':
           valor_total_fatura2 = float(0)
      
        if type(valor_total_fatura) == str:
           
           string2 = '!.#%'
           char_rep = {k: '' for k in string2}
           
           valor_total_fatura2 = valor_total_fatura.translate(str.maketrans(char_rep))
           valor_total_fatura2 = float(valor_total_fatura2.replace (',','.'))
       
        else:
           valor_total_fatura2 = float(valores_faturados_auditoria[i]['valor'])
    
    
        Vl_total = "{:.2f}".format(valor_total_fatura2)
        Vl_auditoria = "{:.2f}".format(soma_valores_auditoria)
        
        print('Vl_total: ',Vl_total)
        print('Vl_total: ',Vl_auditoria)
        
        if Vl_total == Vl_auditoria:
            print('VALOR CORRETO!!')
    
        
    def query_GED_start (self):
        print('---------------- GED ----------------')   
        fatura_ged = self.id_raven
            
        Query_activeGED = QueryGED()
        Query_activeGED.setUpged()
        
        query_results_where = Query_activeGED.query_where(fatura_ged)
        
        query_results_attachmentoperation = Query_activeGED.get_attachmentoperation("GED", str(fatura_ged))
        
        
Execute_search_start = Execute_search()
Execute_search_start.query_sql_start()
Execute_search_start.query_GED_start()
Execute_search_start.query_nosql_start()



