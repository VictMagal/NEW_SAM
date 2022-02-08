import sys
from PyQt5 import uic, QtWidgets
from SAM_2 import verificação
from SAM_4_docparser import Parseamento_docparser
import openpyxl
import os


class load_arquivos:
        def __init__(self):
            self.arquivo_fornecedor = []
            self.palavra_chave = []
            self.list_fornecedor = []
            self.nome_fornecedor = []
            

        def ler_arquivo_fornecedor(self):
            fornecedor = QtWidgets.QFileDialog.getOpenFileNames()[0]
            
            print(fornecedor)
            print('Arquivos importados:', len(fornecedor))
            
            # with open (fornecedor, 'r') as a:
            #     self.arquivo_fornecedor = a.name
            for arquivo in fornecedor:
                self.list_fornecedor.append(arquivo)

            print('Load file fornecedor complete!')
            print('list_fornecedor:', self.list_fornecedor)
            

        def Identificar_Cliente(self):
            if self.palavra_chave[:3] == 'PUC':
                 self.Cliente = 'PUC'
                 print('Cliente = ',self.Cliente)
                
            elif self.palavra_chave[:3] == 'LOC':
                self.Cliente = 'LOCALIZA'
                print('Cliente = ',self.Cliente)
            
            elif self.palavra_chave[:3] == 'RIA':
                self.Cliente = 'RIACHUELO'
                print('Cliente = ',self.Cliente)
            
            elif self.palavra_chave[:3] == 'FLE':
                self.Cliente = 'FLEURY'
                print('Cliente = ',self.Cliente)
                
            elif self.palavra_chave[:3] == 'DAK':
                 self.Cliente = 'DAKI'
                 print('Cliente = ',self.Cliente)
            
            elif self.palavra_chave[:3] == 'PAG':
                 self.Cliente = 'PAGUE_MENOS'
                 print('Cliente = ',self.Cliente)
            
            elif self.palavra_chave[:3] == 'MRV':
                 self.Cliente = 'MRV'
                 print('Cliente = ',self.Cliente)
        
            else: 
                print('Cliente não identificado!!')

                
      
        def executar_SAM4(self):
            self.nova_list_fornecedor = []
            for nome_arquivo in self.list_fornecedor:
                file_oldname = os.path.join(nome_arquivo)
                
                novo_nome = nome_arquivo[:-4] + self.palavra_chave + '.pdf'
                self.nova_list_fornecedor.append(novo_nome)
                
                file_newname_newfile = os.path.join(novo_nome)
                os.rename(file_oldname, file_newname_newfile)
                
                
            self.list_fornecedor = self.nova_list_fornecedor
            
            
            nome_fornecedor = self.nome_fornecedor
            arquivo_pdf = self.list_fornecedor
            
            chama_SAM4 = Parseamento_docparser(nome_fornecedor, arquivo_pdf)
            self.list_json_parseado = chama_SAM4.importar_pdf()
         
            load_active.json_for_excel()
            
            
        def json_for_excel(self):
            print(self.nome_fornecedor.upper())
            
            if 'AGUA' in self.nome_fornecedor.upper():
                vertical = 'AGUA'
            elif 'ENERGIA' in self.nome_fornecedor.upper():
                vertical = 'ENERGIA'
            
            if vertical == 'AGUA':  
                self.wb_vertical = openpyxl.load_workbook('vertical_agua.xlsx')
                self.ws_vertical = self.wb_vertical['Worksheet']
            
            elif vertical == 'ENERGIA': 
                self.wb_vertical = openpyxl.load_workbook('vertical_energia.xlsx')
                self.ws_vertical = self.wb_vertical['Worksheet']
            
            is_data = True
            count_col_vertical = 0
            while is_data:
                count_col_vertical += 1
                data =  self.ws_vertical.cell (row = 1, column = count_col_vertical).value
                if data == None:
                    is_data = False
            row_vertical = 2
           
            print(self.list_json_parseado)
            
            for json_parseado in self.list_json_parseado:
                json_parseado = json_parseado[0]
                print(json_parseado)
                print(type(json_parseado))
                print()
                
                for num_descricao in range(len(json_parseado['valores_faturados'])):
                    json_valores_faturados = json_parseado['valores_faturados']
                    json_valores_faturados = json_valores_faturados[num_descricao]
                    
                    for j in range(count_col_vertical-1):
                        j+=1
                        column_vertical = self.ws_vertical.cell (row = 1, column = j).value
                        print()
                        print(column_vertical.lower())
                        print()
                        print(type(column_vertical.lower()))
                        
                        if column_vertical.lower() == 'valores_faturados valor':
                           column_vertical = 'valor'
                        
                        if column_vertical.lower() == 'descrição serviço':
                           column_vertical = 'descricao'
                            
                        if column_vertical.lower() in json_parseado.keys():
                            valor_parseado = json_parseado[column_vertical.lower()]
                            self.ws_vertical.cell (row = row_vertical, column = j).value = valor_parseado
                            print(valor_parseado)
        
                        elif column_vertical.lower() in json_valores_faturados.keys():
                            print('sim:', column_vertical.lower())
                            self.ws_vertical.cell (row = row_vertical, column = j).value = valor_parseado = json_valores_faturados[column_vertical.lower()]
                    
                    row_vertical += 1
                        
    
            self.wb_vertical.save('______vertical' + self.Cliente + '__' + self.nome_fornecedor+'.xlsx')
            print('Save file >>>>>', '______vertical' + self.Cliente + '__' + self.nome_fornecedor+'.xlsx')
            
            self.list_fornecedor = [('______vertical' + self.Cliente + '__' + self.nome_fornecedor+'.xlsx')]

        
        def executar_SAM2(self):
            print('Executando SAM_2...')
            palavra_chave = tela.lineEdit.text()
            self.palavra_chave = palavra_chave
            
            nome_fornecedor = tela.lineEdit_2.text()
            self.nome_fornecedor = nome_fornecedor
            
            load_active.Identificar_Cliente()
            load_active.executar_SAM4()
            
            fornecedor_x = 0 
            while fornecedor_x < len(self.list_fornecedor):
                print("Fazendo....>> ", self.list_fornecedor[fornecedor_x])
            
                chama_SAM2 = verificação(self.list_fornecedor[fornecedor_x], self.palavra_chave, self.Cliente)
                chama_SAM2.criar_new_sheet()
                chama_SAM2.count_ws()
                chama_SAM2.File_name()      
                chama_SAM2.count_new_ws()
                chama_SAM2.tabela_dinâmica_new_sheet()
                chama_SAM2.comparar_valores()
            
                fornecedor_x+=1
            

app = QtWidgets.QApplication([])
tela = uic.loadUi("Interface_SAM.ui")

tela.show()

load_active = load_arquivos()
tela.pushButton.clicked.connect(load_active.ler_arquivo_fornecedor)
tela.pushButton_4.clicked.connect(load_active.executar_SAM2)

sys.exit(app.exec_())