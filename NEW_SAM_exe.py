from NOSQL_RavenDB import Query
#import json

print('XXXXXXX... NEW_SAM_exe...XXXXXXXXXXXXX')


# Valores que vão sair do TWM e iniciar o processo de saneamento 
saneado = 'Não' #ou vazio
id_fatura = 'd17caf9ade5348a287295914b0d17dfd' #precisa ver qual vem do TWM e comparar com qual indice do Raven






# Executando query para cada fatura pendente que veio do TWM e preenchendo dict com os valores parseados
Query_start = Query()
Query_start.setUp()

query_results = Query_start.query_where(id_fatura)
query_jason = query_results[0]

print(query_jason)

print('--------------------------------------')






# Comparando os valores do 
vl_total = query_results[0].vl_total
valores_faturados = query_results[0].valores_faturados
valores_faturados_auditoria = query_results[0].valores_faturados_auditoria




# print(vl_total)
# #print(valores_faturados)
# print(valores_faturados_auditoria[0])

# valor = valores_faturados_auditoria[0].descricao
# print(valor)

#for i in valores_faturados_auditoria:
    