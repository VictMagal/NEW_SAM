from SQL_TWM_pelo_GED import QuerySQL
from GED_File_pelo_GED import QueryGED
import csv
import json
from json import dumps
import pandas as pd
import pickle
import openpyxl
from io import BytesIO

class Execute_search ():
    def __init__(self):
        print('---------------- DADOS ----------------')
        '''
            @twm_cliente: Escolher o cliente twm_localiza, , twm_riachuelo, twm_fleury, twm_puc
            @mes_emissao: Escolher o mÊs pra verificar os não-saneados
        '''
        self.twm_cliente = 'twm_localiza'
        self.mes_emissao = '202006'
        
        
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
        
        if self.twm_cliente == 'twm_localiza':
            self.cliente = 'LOCALIZA'
        elif self.twm_cliente == 'twm_riachuelo':
            self.cliente = 'RIACHUELO'
        elif self.twm_cliente == 'twm_fleury':
            self.cliente = 'FLEURY'
        elif self.twm_cliente == 'twm_puc':
            self.cliente = 'PUC'
        else:
            print('cliente não identificado: Dados iniciais')
        
        print(self.cliente)
        print(self.mes_emissao)
   
    
    def string_to_float(self, valor):
        '''
            @valor: Usado para corrigir quando o valor vem formatado 1,110.00 alterando para o padrão do python
        '''
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
        QuerySQL_start = QuerySQL()
        QuerySQL_start.setUpsql(self.twm_cliente)
        tabela_twm = QuerySQL_start.query(self.query_dbo_t_fatura_base.replace('valor_data', self.mes_emissao))
       
        self.tabela_twm = tabela_twm
        print(self.tabela_twm.columns)
        
        if len(tabela_twm.index) == 0:
            print('Aviso: Nenhuma Fatura encontrada no TWM.')    
        else:
            True
#------------------------------FAZ UMA FATURA POR VEZ, PARA FAZER VÁRIAS ADAPTAR (andamento da adaptação)

        for index, row in tabela_twm.iterrows():
            self.nu_fatura_base = row['nu_fatura_base']
            self.id_ged = row['id_ged']
            self.conta_aglutinada = row['nu_cliente_base']
            self.dt_vencimento = str(row['dt_vencimento']).replace('-', '')
            self.dc_razao_social_fornecedor = row['dc_razao_social_fornecedor']
            
            tabela_id_raven = QuerySQL_start.query(self.query_t_arquivo_ged.replace('valor_id_ged', self.id_ged)) 
            self.id_raven = tabela_id_raven.id_raven[0]
            
            print('----------------- INFO ----------------')
            print('id_ged_no_twm:', self.id_ged)
            print('id_ged_no_raven:', self.id_raven)
            print('nu_fatura_base:', self.nu_fatura_base)
            print('conta_aglutinada:', self.conta_aglutinada)
            print('dt_vencimento:', self.dt_vencimento)
            print('dc_razao_social_fornecedor:', self.dc_razao_social_fornecedor)
            print()
            
            self.contador_de_faturas_total = len(tabela_twm.index)
            print('Total = ', self.contador_de_faturas_total)
            print('Executando:', self.nu_fatura_base)
            
            Execute_search_start.query_GED_start()
            #Execute_search_start.col_parser_to_col_consolidado()
            #Execute_search_start.json_parser_to_csv()
        
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
        
        # bytesio_o = BytesIO(bytes)

        # with open("testando.bin", "wb") as f:
        #     f.write(bytesio_o.getbuffer())
        
    def linkado_excel (self): 
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
       
        
        
    def col_parser_to_col_consolidado(self):
        print('--------------parser_to_linkado ----------------')
        # Informações do linkado (Consultoria)
        list_localiza_parser = ['Dc_identificador_conta', 'Dt_vencimento', 'Vl_total', 'Dc_razao_social', 'Dc_identificador_pessoa_juridica', 'Dc_razao_social_cliente', 'Dc_identificador_pessoa_juridica_cliente', 'Dc_endereco_cliente', 'Dt_leitura_anterior', 'Dt_leitura_atual', 'Unidade_medida', 'Dt_mes_referencia', 'Vl_base_calculo_icms', 'Vl_valor_icms', 'Vl_aliquota_icms', 'Vl_base_calculo_pis_pasep', 'Vl_valor_pis_pasep', 'Vl_aliquota_pis_pasep', 'Vl_base_calculo_cofins', 'Vl_aliquota_cofins', 'Vl_valor_cofins', 'Dc_classe', 'Dc_subclasse', 'Valores_faturados_auditoria Descricao', 'Valores_faturados_auditoria Quantidade', 'Valores_faturados_auditoria Tarifa Preco', 'Valores_faturados_auditoria Valor', 'Valores_faturados_auditoria Faturado', 'Dc_modalidade_tarifaria', 'Dc_grupo_tensao', 'Dc_subgrupo_tensao', 'Vl_tensao_nominal', 'Vl_tensao_contratada', 'Dc_limites_tensao', 'Fator_carga Hora Ponta', 'Fator_carga Hora Fora Ponta', 'Energia_reativa Hfp/único', 'Energia_reativa Hora Ponta', 'Energia_reativa Reservado', 'twm_Fornecedor', 'twm_Identificador', 'twm_Categoria', 'twm_Subcategoria', 'twm_Data de emissão', 'twm_Status', 'twm_Nota fiscal', 'twm_Localidade', 'twm_Sigla', 'twm_Regional']
        list_localiza_dash = ['Nº da Conta', 'Vencimento', 'Valor total', 'Razão social fornecedor', 'CNPJ Fornecedor', 'Razão social Cliente', 'CNPJ cliente', 'Endereço cliente', 'Data leitura anterior', 'Data leitura atual', 'Unidade medida', 'Mês referência', 'Base de cálculo ICMS', 'Valor ICMS', 'Alíquota ICMS', 'Base de cálculo PIS/PASEP', 'Valor PIS/PASEP', 'Alíquota PIS/PASEP', 'Base de cálculo COFINS', 'Alíquota COFINS', 'Valor COFINS', 'Classe', 'Subclasse', 'Descrição Serviço', 'Consumo', 'Tarifa com imposto', 'Valor do Serviço', 'Faturado', 'Modalidade tarifária', 'Grupo tensão', 'Subgrupo tensão', 'Tensão nominal', 'Tensão contratada', 'Limites tensão', 'Carga Hora Ponta', 'Carga Hora Fora Ponta', 'Energia Reativa Hfp/unico', 'Energia Reativa Hora Ponta', 'Energia Reativa Reservado', 'Fornecedor', 'Identificador', 'Categoria', 'Subcategoria', 'Data de emissão', 'Status', 'Nota fiscal', 'Localidade', 'Sigla', 'Regional']
        
        list_riachuelo_parser = ['Dc_identificador_conta', 'Dt_vencimento', 'Vl_total', 'Dc_razao_social', 'Dc_identificador_pessoa_juridica', 'Dc_razao_social_cliente', 'Dc_identificador_pessoa_juridica_cliente', 'Dc_endereco_cliente', 'Vl_base_calculo_icms', 'Dt_leitura_anterior', 'Unidade_medida', 'Dt_mes_referencia', 'Vl_aliquota_icms', 'Dt_leitura_atual', 'Vl_valor_icms', 'Vl_base_calculo_pis_pasep', 'Vl_aliquota_pis_pasep', 'Vl_valor_pis_pasep', 'Vl_base_calculo_cofins', 'Vl_aliquota_cofins', 'Vl_valor_cofins', 'Dc_classe', 'Dc_subclasse', 'Valores_faturados_auditoria Descricao', 'Valores_faturados_auditoria Quantidade', 'Valores_faturados_auditoria Tarifa Preco', 'Valores_faturados_auditoria Valor', 'Valores_faturados_auditoria Faturado', 'Dc_modalidade_tarifaria', 'Dc_grupo_tensao', 'Dc_subgrupo_tensao', 'Vl_tensao_nominal', 'Vl_tensao_contratada', 'Dc_limites_tensao', 'Energia_reativa Hfp/único', 'Energia_reativa Hora Ponta', 'Energia_reativa Reservado', 'Fator_carga Hora Ponta', 'Fator_carga Hora Fora Ponta', 'twm_Concessionária', 'twm_Identificador', 'twm_Categoria', 'twm_Subcategoria', 'twm_Data de emissão', 'twm_Localidade', 'twm_Status', 'twm_Cód. Filial', 'twm_AVB', 'twm_Nota fiscal'] 
        list_riachuelo_dash = ['Nº da Conta', 'Vencimento', 'Valor total', 'Razão social fornecedor', 'CNPJ Fornecedor', 'Razão social Cliente', 'CNPJ cliente', 'Endereço cliente', 'Base de cálculo ICMS', 'Data leitura anterior', 'Unidade medida', 'Mês referência', 'Alíquota ICMS', 'Data leitura atual', 'Valor ICMS', 'Base de cálculo PIS/PASEP', 'Alíquota PIS/PASEP', 'Valor PIS/PASEP', 'Base de cálculo COFINS', 'Alíquota COFINS', 'Valor COFINS', 'Classe', 'Subclasse', 'Descrição Serviço', 'Quantidade', 'Tarifa com imposto', 'Valor do Serviço', 'Faturado', 'Modalidade tarifária', 'Grupo tensão', 'Subgrupo tensão', 'Tensão nominal', 'Tensão contratada', 'Limites tensão', 'Carga Hora Ponta', 'Carga Hora Fora Ponta', 'Energia Reativa Hfp/unico', 'Energia Reativa Hora Ponta', 'Energia Reativa Reservado', 'Concessionária', 'Identificador', 'Categoria', 'Subcategoria', 'Data de emissão', 'Localidade', 'Status', 'Cód. Filial', 'AVB', 'Nota fiscal']
        
        list_fleury_parser = ['Nome_fornecedor', 'Dc_identificador_conta', 'Dt_vencimento', 'Vl_total', 'Dc_razao_social', 'Dc_identificador_pessoa_juridica', 'Dc_razao_social_cliente', 'Dc_identificador_pessoa_juridica_cliente', 'Dc_endereco_cliente', 'Vl_base_calculo_icms', 'Dt_leitura_anterior', 'Unidade_medida', 'Dt_mes_referencia', 'Vl_aliquota_icms', 'Dt_leitura_atual', 'Vl_valor_icms', 'Vl_base_calculo_pis_pasep', 'Vl_aliquota_pis_pasep', 'Vl_valor_pis_pasep', 'Vl_base_calculo_cofins', 'Vl_aliquota_cofins', 'Vl_valor_cofins', 'Dc_classe', 'Dc_subclasse', 'Valores_faturados_auditoria Descricao', 'Valores_faturados_auditoria Quantidade', 'Valores_faturados_auditoria Valor', 'Valores_faturados_auditoria Tarifa Preco', 'Dc_modalidade_tarifaria', 'Dc_grupo_tensao', 'Dc_subgrupo_tensao', 'Vl_tensao_nominal', 'Vl_tensao_contratada', 'Dc_limites_tensao', 'None', 'None', 'None', 'None', 'None', 'None', 'twm_Identificador', 'twm_Categoria', 'twm_Data de emissão', 'twm_Localidade', 'twm_Status', 'twm_Cód. Filial', 'twm_Mês', 'twm_Subcategoria', None]
        list_fleury_dash = ['Concessionária', 'Nº da Conta', 'Vencimento', 'Valor total', 'Razão social fornecedor', 'CNPJ Fornecedor', 'Razão social Cliente', 'CNPJ cliente', 'Endereço cliente', 'Base de cálculo ICMS', 'Data leitura anterior', 'Unidade medida', 'Mês referência', 'Alíquota ICMS', 'Data leitura atual', 'Valor ICMS', 'Base de cálculo PASEP', 'Alíquota PASEP', 'Valor PASEP', 'Base de cálculo COFINS', 'Alíquota COFINS', 'Valor COFINS', 'Classe', 'Subclasse', 'Descrição Serviço', 'Consumo Faturado', 'Valor do Serviço', 'Tarifa com imposto', 'Modalidade tarifária', 'Grupo tensão', 'Subgrupo tensão', 'Tensão Nominal', 'Tensão contratada', 'Limites tensão', 'Demanda Contratada ponta', 'Demanda registrada ponta', 'Demanda Contratada fora ponta', 'Demanda registrada fora ponta', 'Consumo ponta', 'Consumo fora ponta', 'Identificador', 'Categoria', 'Data de emissão', 'Localidade', 'Status', 'Cód. Filial', 'Mês', 'Subcategoria', None]
        
        list_puc_parser = ['Dc_identificador_conta', 'Dt_vencimento', 'Vl_total', 'Dc_razao_social', 'Dc_identificador_pessoa_juridica', 'Dc_razao_social_cliente', 'Dc_identificador_pessoa_juridica_cliente', 'Dc_endereco_cliente', 'Vl_base_calculo_icms', 'Dt_leitura_anterior', 'Unidade_medida', 'Dt_mes_referencia', 'Vl_aliquota_icms', 'Dt_leitura_atual', 'Vl_valor_icms', 'Vl_base_calculo_pis_pasep', 'Vl_aliquota_pis_pasep', 'Vl_valor_pis_pasep', 'Vl_base_calculo_cofins', 'Vl_aliquota_cofins', 'Vl_valor_cofins', 'Dc_classe', 'Dc_subclasse', 'Valores_faturados_auditoria Descricao', 'Valores_faturados_auditoria Quantidade', 'Valores_faturados_auditoria Valor', 'Valores_faturados_auditoria Faturado', 'Valores_faturados_auditoria Tarifa Preco', 'Dc_modalidade_tarifaria', 'Dc_grupo_tensao', 'Dc_subgrupo_tensao', 'Vl_tensao_nominal', 'Vl_tensao_contratada', 'Dc_limites_tensao', 'Energia_reativa Reservado', 'Fator_carga Hora Ponta', 'Fator_carga Hora Fora Ponta', 'Energia_reativa Hfp/único', 'Energia_reativa Hora Ponta', 'twm_Fornecedor', 'twm_Identificador', 'twm_Categoria', 'twm_Subcategoria', 'twm_Localidade', 'twm_Metro Quadrado', 'twm_Alunos', 'twm_Data de emissão', 'twm_GRUPO', None]
        list_puc_dash = ['Nº da Conta', 'Vencimento', 'Valor total', 'Razão social fornecedor', 'CNPJ Fornecedor', 'Razão social Cliente', 'CNPJ cliente', 'Endereço cliente', 'Base de cálculo ICMS', 'Data leitura anterior', 'Unidade medida', 'Mês referência', 'Alíquota ICMS', 'Data leitura atual', 'Valor ICMS', 'Base de cálculo PIS/PASEP', 'Alíquota PIS/PASEP', 'Valor PIS/PASEP', 'Base de cálculo COFINS', 'Alíquota COFINS', 'Valor COFINS', 'Classe', 'Subclasse', 'Descrição Serviço', 'Quantidade', 'Tarifa com imposto', 'Valor do Serviço', 'Faturado', 'Modalidade tarifária', 'Grupo tensão', 'Subgrupo tensão', 'Tensão nominal', 'Tensão contratada', 'Limites tensão', 'Energia Reativa Hfp/unico', 'Energia Reativa Hora Ponta', 'Energia Reativa Reservado', 'Carga Hora Ponta', 'Carga Hora Fora Ponta', 'Fornecedor', 'Identificador', 'Categoria', 'Subcategoria', 'Localidade', 'Metro Quadrado', 'Alunos', 'Data de emissão', 'GRUPO', None]
        
        #CRIAR DICT DAS LISTAS LINKADO
        self.linkado_localiza = json.loads(dumps(dict(zip(list_localiza_parser, list_localiza_dash)), ensure_ascii=False))
        self.linkado_riachuelo = json.loads(dumps(dict(zip(list_riachuelo_parser, list_riachuelo_dash)), ensure_ascii=False))
        self.linkado_fleury = json.loads(dumps(dict(zip(list_fleury_parser, list_fleury_dash)), ensure_ascii=False))
        self.linkado_puc = json.loads(dumps(dict(zip(list_puc_parser, list_puc_dash)), ensure_ascii=False))
        
        
        #Escolher o arquivo utilizado de acordo com o cliente
        #print(self.cliente)
        if self.cliente == 'LOCALIZA':
            self.json_linkado = self.linkado_localiza
        elif self.cliente == 'RIACHUELO':
            self.json_linkado = self.linkado_riachuelo
        elif self.cliente == 'FLEURY':
            self.json_linkado = self.linkado_fleury
        elif self.cliente == 'PUC':
            self.json_linkado = self.linkado_puc
        else:
            print('Erro ao identificar cliente linkado.')
            
        #Comparar linkado com parserado e gerar o consolidado final do Json do Dash;            
        list_indice_consolidado = []
        list_valor_consolidado = []

        for indice_linkado in self.json_linkado: 
            valor_linkado = self.json_linkado[indice_linkado]
            list_indice_consolidado.append(valor_linkado)
            
            valor_linkado = self.json_parseado.get(indice_linkado.lower(), 'N/D')
         
        #Procurar os valores N/D no banco do TWM(self.tabela_twm);  
            if valor_linkado == 'N/D':
                dict_consolidado_and_twm = {
                                            'twm_identificador':'nu_fatura_base',
                                            'twm_data de emissão':'dt_emissao',
                                            'twm_nota fiscal':'nu_nota_fiscal',
                                            'twm_fornecedor':'nu_fatura_fornecedor',
                                            'twm_status':'ic_status',
                                            'twm_localidade':'id_localidade'
                                            }
                
                if indice_linkado.lower() in dict_consolidado_and_twm.keys():
                    busca_coluna_twm = dict_consolidado_and_twm[indice_linkado.lower()]
                    
                    if busca_coluna_twm == 'nu_fatura_base':
                        try:     valor_linkado = self.tabela_twm.nu_fatura_base[0]
                        except:  print(busca_coluna_twm, ': Não encontrado no twm')
                    
                    if busca_coluna_twm == 'nu_nota_fiscal':
                        try:     valor_linkado = self.tabela_twm.nu_nota_fiscal[0]
                        except:  print(busca_coluna_twm, ': Não encontrado no twm')

            list_valor_consolidado.append(valor_linkado)
            
        #Consolidado final (dashboard)
        self.json_consolidado = json.loads(dumps(dict(zip(list_indice_consolidado, list_valor_consolidado)), ensure_ascii=False))
        
        
    def json_parser_to_csv(self):
        print('--------------parser_to_csv ----------------')
        print(self.json_consolidado, len(self.json_consolidado))
        
        #Transforma Json consolidado em Arquivo DataFrame
        data_items = self.json_consolidado.items()
        data_list = list(data_items)
        df = pd.DataFrame(data_list)
        print(df)
    
        #Salva o arquivo em um Excel na pasta do código
        #df.to_excel("Consolidado_"+ self.cliente+".xlsx", sheet_name="Plan1")
        
Execute_search_start = Execute_search()
Execute_search_start.query_sql_start()
print('################## FIM #############################')



