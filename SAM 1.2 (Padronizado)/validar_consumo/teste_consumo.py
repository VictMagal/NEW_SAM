import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib as plt
from sklearn.preprocessing import scale
import researchpy as rp
from scipy import stats


class ValidarConsumo:
    def __init__(self):
        #Carregar os bancos de dados dos clientes em excel
        self.cliente = 'Localiza'
        self.vertical = 'Energia'
        
        try:
            df = pd.read_excel(f"C:/Users/Victor Magal/Desktop/SAM 1.2 (Padronizado)/backup/{self.cliente}_{self.vertical}.xlsx")
            #print(df.head(n=10))
            print(df.columns)
            print(df.shape)
            self.df = df
        except:
            print(f"#Fail001:\nNão foi possível carregar o banco do cliente:{self.cliente}\nObs: Padrão do nome do arquivo é 'Cliente_Vertical'")

    def consumo_energia(self):
        #print(self.df['Categoria'].value_counts()) 
        #self.df['Categoria'].value_counts().plot(kind='bar')    
        
        #print(self.df['Subcategoria'].value_counts()) 
        #self.df['Subcategoria'].value_counts().plot(kind='bar')

        #print(self.df.loc[self.df['Subcategoria'] == 'Na ponta'].sum())
        
        self.df = self.df [['Nº da Conta', 'Vencimento','Identificador','Valor total','Categoria', 'Subcategoria','Quantidade']]
        print(self.df.head(n=5))
        #print(self.df['Categoria'].describe())
        #print()
        #print(self.df['Quantidade'].describe())
        print()
        print(self.df.groupby('Categoria')['Quantidade'].describe())
        
        
        
#-------------------------------------------------------------------------#
validar = ValidarConsumo()
validar.consumo_energia()
