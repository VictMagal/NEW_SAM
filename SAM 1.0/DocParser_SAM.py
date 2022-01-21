import pydocparser
import time

class Parseamento_docparser():
    def __init__(arquivo_pdf, tabela_twm):
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

        # Nome do fornecedor vem como razão social, é preciso padronizar pelo input do parser
        fornecedor = 'Coletar da tabela TWM'
        identificador_twm = 'Coletar da tabela TWM'
        
        fornecedor = 'Energia_Cemig'
        #-----------------------------------------------Envia PDF para ser parseado -------------------------------------------------------------
        
        # path = 'teste_cemig_3010594770_20220222.pdf'
        # id = parser.upload_file_by_path(path, fornecedor) #args: file to upload, the name of the parser
        # print(id)
        
        # time.sleep(240)
        
        id = '0e3273ea873714e71feac69babed8728'
        
        #Note that "fileone.pdf" was in the current working directory
        data = parser.get_one_result(fornecedor, id) # The id is the doc id that was returned by `parser.upload()`
        print(data)