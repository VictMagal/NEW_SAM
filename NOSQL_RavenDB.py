from pyravendb.store import document_store

print('XXXXXXX... NEW_SAM_1...XXXXXXXXXXXXX')
class QueryNOSQL():
    def setUp (self):
        # Configurações de acesso ao RavenDB da guiabdo: "usando PFX file para certificação"
        urls = "https://a.rdbguiando.ravendb.community"
        cert = {"pfx": "C:/Users/Victor Magal/Downloads/Raven/victormagalhaes.client.certificate/victormagalhaes.client.certificate.pfx", "password": "#YpzIf&t3dby"}
        self.store =  document_store.DocumentStore(urls=urls, database="automacao-faturas", certificate=cert)
        self.store.initialize()
          
    def query (self, id_fatura):
        # Query procurando pelo índice do banco Ex: where(informar no nome da coluna no banco, informar o valor procurado).
        with self.store.open_session() as session:
            query_results = list(session.query().where(id = id_fatura))
            return query_results        
            