from NOSQL_RavenDB import QueryNOSQL
from SQL_TWM import QuerySQL


class Execute_search ():
    def __init__(self):
        print('---------------- DADOS ----------------')
        self.cliente = 'twm_fleury'
        self.mes_emissao = '202201'
        self.query = '''
                    SELECT  *
                    FROM    dbo.t_fatura_base fatura
                            INNER JOIN dbo.t_conta_aglutinada_base conta ON conta.id_conta_aglutinada_base = fatura.id_conta_aglutinada_base
                            INNER JOIN dbo.t_tipo_conta tipo_conta ON tipo_conta.id_tipo_conta = conta.id_tipo_conta
                            INNER JOIN dbo.t_vertical vertical ON vertical.id_vertical = tipo_conta.id_vertical
                            LEFT JOIN dbo.t_valor_fatura valor_fatura ON valor_fatura.id_fatura = fatura.id_fatura_base
                                                                         AND valor_fatura.id_campo_fatura = 4
                    
                    WHERE   ( valor_fatura.dc_valor_fatura = 'Não'
                              OR valor_fatura.dc_valor_fatura IS NULL
                            )
                            AND tipo_conta.id_vertical = 2
                            AND conta.ic_aprovada=1 AND SUBSTRING(CONVERT(CHAR(8),dt_emissao,112),1,6)=
                '''

    def query_sql_start (self):
        print('----------------- SQL -----------------')
        QuerySQL_start = QuerySQL()
        QuerySQL_start.setUp(self.cliente)
        tabela_twm = QuerySQL_start.query(self.query + self.mes_emissao)
        # Nome dos campos principais no twm: nu_fatura_base, dt_emissao, dt_vencimento, tt_total_fatura
        '''
                    SQL                     RAVEN
                nu_fatura_base          file_name + .pdf
                dt_emissao              dt_emissao
                dt_vencimento           dt_vencimento
                tt_total_fatura         vl_total

        '''
        print(tabela_twm)
        for i in range(len(tabela_twm)):
            try:
                self.sql_dict = { 
                                'file_name'     :   tabela_twm.nu_fatura_base[i]+'.pdf',
                                'dt_emissao'    :   tabela_twm.dt_emissao[i],
                                'dt_vencimento' :   tabela_twm.dt_vencimento[i],
                                'vl_total'      :   tabela_twm.tt_total_fatura[i]
                                    
                                }
                
                print(self.sql_dict)
                self.id_fatura = tabela_twm.nu_fatura_base[0]+'.pdf'
                Execute_search_start.query_nosql_start()
            except:
                print('Fatura não encontrada SQL.')
        
    def query_nosql_start (self):
        print('---------------- NOSQL ----------------')
        # Executando query para cada fatura pendente que veio do TWM e preenchendo dict com os valores parseados
        QueryNOSQL_start = QueryNOSQL()
        QueryNOSQL_start.setUp()
        query_results = QueryNOSQL_start.query(self.id_fatura)
        try:
            query_jason = query_results[0]
            print(query_jason)
        except:
            print('Fatura não encontrada no RavenDB.')
            print(query_results)
            
        

Execute_search_start = Execute_search()
Execute_search_start.query_sql_start()


