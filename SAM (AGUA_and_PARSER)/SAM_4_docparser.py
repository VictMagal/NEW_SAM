import pydocparser
import time

class Parseamento_docparser():
    def __init__(self, fornecedor, list_arquivo_pdf):
        '''
            @arquivo_pdf: arquivo gerado pela saída do GED no RavenDB
            @tabela_twm: contém @fornecedor e @identificador_twm
            @fornecedor: Razão social do fornecedor que vem do SQL do twm
            @identificador_twm: identificador da fatura para acompanhar seu trajeto
            @parser_login: Usa-se a chave API da guiando para enviar arquivos ao Parser
            @result: ping.pong (pong: significa que tudo ocorreu corretamente)
        '''
        parser = pydocparser.Parser()
        parser.login('7a5a9bde8daf2b40e2282e7002a5bc2b689770eb')
        result = parser.ping()
        print(result)   
        self.parser = parser
        self.fornecedor = fornecedor
        self.list_arquivo_pdf = list_arquivo_pdf
        
        #-----------------------------------------------Envia PDF para ser parseado -------------------------------------------------------------
    def importar_pdf(self):
        list_data = []
        list_id = []
        fornecedor = self.fornecedor #'Energia_Cemig'
        list_path = self.list_arquivo_pdf # '123131413123.pdf'
        #path = 'teste_cemig_3010594770_20220222.pdf'
        
        for path in list_path:
            id = self.parser.upload_file_by_path(path, fornecedor) #args: file to upload, the name of the parser
            list_id.append(id)
        
        len_list_id = len(list_id)
        len_list_path = len(list_path)

        print()
        print('Aguarda processamento no Parser...')
        
        for i in range (300, 0, -1):
            print(f"{i}", end="\r", flush= True)
            time.sleep(1)
            print()

        for id in list_id:
            #Note that "fileone.pdf" was in the current working directory
            data = self.parser.get_one_result(fornecedor, id) # The id is the doc id that was returned by `parser.upload()`    
            list_data.append(data)
     
                
        return list_data