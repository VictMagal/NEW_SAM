
# Coluna extraída do DocParser que é usada para sanear e subir para o Dash *Mas faltam as colunas azuis do consolidado
list_campos_parser =        ['dc_identificador_conta',
                             'dt_vencimento',
                             'vl_total',
                             'dc_razao_social',
                             'dc_identificador_pessoa_juridica',
                             'dc_razao_social_cliente',
                             'dc_identificador_pessoa_juridica_cliente',
                             'dc_endereco_cliente',
                             'dt_leitura_anterior',
                             'dt_leitura_atual',
                             'unidade_medida',
                             'dt_mes_referencia',
                             'vl_base_calculo_icms',
                             'vl_valor_icms',
                             'vl_aliquota_icms',
                             'vl_base_calculo_pis_pasep',
                             'vl_valor_pis_pasep',
                             'vl_aliquota_pis_pasep',
                             'vl_base_calculo_cofins',
                             'vl_aliquota_cofins',
                             'vl_valor_cofins',
                             'dc_classe',
                             'dc_subclasse',
                             'valores_faturados_auditoria Descricao',
                             'valores_faturados_auditoria Quantidade',
                             'valores_faturados_auditoria Tarifa Preco',
                             'valores_faturados_auditoria Valor',
                             'valores_faturados_auditoria Faturado',
                             'dc_modalidade_tarifaria',
                             'dc_grupo_tensao',
                             'dc_subgrupo_tensao',
                             'vl_tensao_nominal',
                             'vl_tensao_contratada',
                             'dc_limites_tensao',
                             'fator_carga Hora Ponta',
                             'fator_carga Hora Fora Ponta',
                             'energia_reativa Hfp/único',
                             'energia_reativa Hora Ponta',
                             'energia_reativa Reservado']

# Criando dicioário com valores vazios para todos os campos do parser
list_valor_parser = []
for i in range(len(list_campos_parser)):
    list_valor_parser.append(0)

dict_indice_e_valor = dict(zip(list_campos_parser, list_valor_parser))