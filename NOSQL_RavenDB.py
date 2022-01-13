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
            #query_identificador = list(session.query().where(file_name = twm_identificador+'.pdf'))
            
            query_data_vencimento = list(session.query().where(dt_vencimento = twm_dt_vencimento))
            query_conta_aglutinada = list(session.query().where(dc_identificador_conta = twm_conta_aglutinada))
            print(len(query_data_vencimento))
            print(len(query_conta_aglutinada))
            
            
            
            return query_conta_aglutinada        