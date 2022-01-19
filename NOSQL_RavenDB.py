from pyravendb.store import document_store
from pyravendb.data.query import IndexQuery, QueryOperator

class QueryNOSQL():
    def setUpnosql (self):
        # Configurações de acesso ao RavenDB da guiabdo: "usando PFX file para certificação"
        print('XXXXXXX... NOSQL...XXXXXXXXX')
        urls = "https://a.rdbguiando.ravendb.community"
        cert = {"pfx": "C:/Users/Victor Magal/Downloads/Raven/victormagalhaes.client.certificate/victormagalhaes.client.certificate.pfx", "password": "#YpzIf&t3dby"}
        self.store =  document_store.DocumentStore(urls=urls, database="automacao-faturas", certificate=cert)
        self.store.initialize()
          
    def query (self, twm_conta_aglutinada, twm_dt_vencimento):
        # Query procurando pelo índice do banco Ex: where(informar no nome da coluna no banco, informar o valor procurado).
        with self.store.open_session() as session:

            twm_dt_vencimento = '23/09/2021'
            twm_conta_aglutinada = '3011263210'

            query_data_vencimento = list(session.query().where(dt_vencimento = twm_dt_vencimento))
            query_dt_e_conta =  list(session.query().where_equals('dt_vencimento', twm_dt_vencimento).and_also().where_equals('dc_identificador_conta', twm_conta_aglutinada))
 
            print(len(query_data_vencimento))
            print(len(query_dt_e_conta))

            return query_dt_e_conta        
        


