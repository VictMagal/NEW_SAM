from NOSQL_RavenDB import QueryNOSQL
from SQL_TWM import QuerySQL


class Execute_search ():
    def __init__(self):
        print('---------------- DADOS ----------------')
        self.cliente = 'twm_localiza'
        self.mes_emissao = '202201'
        print(self.cliente)
        print(self.mes_emissao)
        
        self.query_dbo_t_fatura_base = '''
                                        SELECT  nu_fatura_base, id_ged
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
                                       SELECT   id_raven 
                                       FROM     t_arquivo_ged 
                                       
                                       WHERE    id_ged = 'valor_id_ged'
                                   '''

    def query_sql_start (self):
        print('----------------- SQL -----------------')
        QuerySQL_start = QuerySQL()
        QuerySQL_start.setUp(self.cliente)
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
        
        tabela_id_raven = QuerySQL_start.query(self.query_t_arquivo_ged.replace('valor_id_ged', self.id_ged))      
        
        self.id_raven = tabela_id_raven.id_raven[i]
       
        print('----------------- INFO ----------------')
        print('id_ged_no_twm:', self.id_ged)
        print('id_ged_no_raven:', self.id_raven)
        print('nu_fatura_base:', self.nu_fatura_base)

        Execute_search_start.query_nosql_start(self.nu_fatura_base)

    
        # try:
        #     self.sql_dict = { 
        #                     'file_name'     :   tabela_twm.nu_fatura_base[i]+'.pdf',
        #                     'dt_emissao'    :   tabela_twm.dt_emissao[i],
        #                     'dt_vencimento' :   tabela_twm.dt_vencimento[i],
        #                     'vl_total'      :   tabela_twm.tt_total_fatura[i]
                                
        #                     }
        #     print('----------------- TWM ---------------')
        #     print(self.sql_dict)
        #     #self.id_fatura = tabela_twm.nu_fatura_base[0]+'.pdf'
        #     #Execute_search_start.query_nosql_start()
            
        # except:
        #     print('Fatura não encontrada SQL.')
        
    def query_nosql_start (self, nu_fatura_base):
        print('---------------- NOSQL ----------------')
        print('file_name:', nu_fatura_base+'.pdf')
        # Executando query para cada fatura pendente que veio do TWM e preenchendo dict com os valores parseados
        QueryNOSQL_start = QueryNOSQL()
        QueryNOSQL_start.setUp()
        query_results = QueryNOSQL_start.query(nu_fatura_base)
        try:
            query_jason = query_results[0]
            print(query_jason)
        except:
            print('Fatura não encontrada no RavenDB.')
            print(query_results)
            
        

Execute_search_start = Execute_search()
Execute_search_start.query_sql_start()

# Nome dos campos principais no twm: nu_fatura_base, dt_emissao, dt_vencimento, tt_total_fatura
'''
            SQL                     RAVEN
        nu_fatura_base          file_name + .pdf
        dt_emissao              dt_emissao
        dt_vencimento           dt_vencimento
        tt_total_fatura         vl_total

'''

