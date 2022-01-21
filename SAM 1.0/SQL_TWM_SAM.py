import pyodbc
import pandas as pd

class Banco_sql_twm():
    def __init__(twm_cliente, tipo_data, ano_mes, vertical_fatura):
        '''
                        # Configurações de acesso ao banco SQL TWM da guiando/
            @twm_cliente: nome do banco no SQL. Ex: twm_localiza, twm_puc, twm_fleury, twm_riachuelo...
            @tipo_data: tipo de data usada em cada cliente. Ex: data_emissao, data_vencimento...
            @ano_mes: data a ser análisada. Ex: 202201, 202202...
            @vertical_fatura: tipo de fatura. Ex: água, 2 = energia, condomínio...
            @server: servidor da guiando (disponibilizado pela equipe de G.A.)
            @username: login do usuário 
            @password: senha do usuário
            @tabela_twm: Nova tabela criada para usar somente as informações necessárias.
        '''
        server = '177.70.121.163'
        username = 'u_victor_magalhaes'
        password = 'Vi@haha270596'
        database = twm_cliente
        
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        
        query_tabela_fatura = Banco_sql_twm.query_tabela_fatura_base(tipo_data, ano_mes, vertical_fatura)
        twm_tabela = Banco_sql_twm.realizar_busca_twm(query_tabela_fatura, cnxn)
        
        tabela_twm = twm_tabela[['nu_fatura_base', 'id_ged','dc_razao_social_fornecedor', 'nu_cliente_base', 'dt_vencimento']]
        
        for id_ged in twm_tabela['id_ged']:
            query_id_ged = Banco_sql_twm.query_tabela_arquivo_ged(id_ged)
            query_ged = Banco_sql_twm.realizar_busca_twm(query_id_ged, cnxn)
            
            id_ged_raven = query_ged['id_raven'][0]         #OBS: fixado no primeiro pra teste, fazer pegar todos
            tabela_twm['new_id_ged_raven'] = id_ged_raven
            
        return tabela_twm
        
    
    def query_tabela_fatura_base (tipo_data, ano_mes, vertical_fatura):
        query_dbo_t_fatura_base = '''
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
                                                AND conta.ic_aprovada=1 AND SUBSTRING(CONVERT(CHAR(8),tipo_data,112),1,6)='ano_mes'
                                        '''
        query_dbo_t_fatura_base = query_dbo_t_fatura_base.replace('tipo_data', tipo_data)
        retunr_dbo_t_fatura_base = query_dbo_t_fatura_base.replace('ano_mes', ano_mes)
        
        return retunr_dbo_t_fatura_base
    
    
    def query_tabela_arquivo_ged (valor_id_ged):
        query_t_arquivo_ged = '''
                                       SELECT   *
                                       FROM     t_arquivo_ged 
                                       
                                       WHERE    id_ged = 'valor_id_ged'
                                   '''
        return_t_arquivo_ged = query_t_arquivo_ged.replace('valor_id_ged', valor_id_ged)
        
        return return_t_arquivo_ged


    def realizar_busca_twm (sql, cnxn):
        tabela_output = pd.io.sql.read_sql(sql, cnxn)
        
        return tabela_output
















