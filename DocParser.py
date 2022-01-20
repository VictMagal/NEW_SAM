import pydocparser
import time

#Login parser usando API 
parser = pydocparser.Parser()
parser.login('7a5a9bde8daf2b40e2282e7002a5bc2b689770eb')
result = parser.ping()

print(result)
parsers = parser.list_parsers()

list_energia = []
for i in range(len(parsers)):
    teste = parsers[i]
    teste_label = teste['label'].upper()
    
    if 'ENERGIA' in teste_label:
        list_energia.append(teste_label)
        
print(list_energia)        
print(len(list_energia))


fornecedor = 'Energia_Cemig'

# layouts = parsers.list_parser_model_layouts(fornecedor)
# print(layouts)
# print(len(layouts))

#-----------------------------------------------Envia PDF para ser parseado -------------------------------------------------------------
# path = 'teste_cemig_3010594770_20220222.pdf'
# id = parser.upload_file_by_path(path, fornecedor) #args: file to upload, the name of the parser
# print(id)

# time.sleep(240)

id = '0e3273ea873714e71feac69babed8728'

#Note that "fileone.pdf" was in the current working directory
data = parser.get_one_result(fornecedor, id) # The id is the doc id that was returned by `parser.upload()`
print(data)