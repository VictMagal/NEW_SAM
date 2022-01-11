import pydocparser

parser = pydocparser.Parser()

parser.login('7a5a9bde8daf2b40e2282e7002a5bc2b689770eb')

result = parser.ping()

print(result)
parsers = parser.list_parsers()

# print(type(parsers))
# print(len(parsers))

list_energia = []
for i in range(len(parsers)):
    teste = parsers[i]
    teste_label = teste['label'].upper()
    
    if 'ENERGIA' in teste_label:
        list_energia.append(teste_label)
        
print(list_energia)        
print(len(list_energia))

fornecedor = 'Energia_Cemig'

layouts = parsers.list_parser_model_layouts(fornecedor)

print(layouts)
print(len(layouts))



#path = 'TESTE_TESTE_TESTE_3011020234_20220122.pdf'
#id = parser.upload_file_by_path(path, fornecedor) #args: file to upload, the name of the parser
# Note that "fileone.pdf" was in the current working directory

#data = parser.get_one_result(fornecedor, id) # The id is the doc id that was returned by `parser.upload()`