from pyravendb.store import document_store

print('XXXXXXX... NEW_SAM_1...XXXXXXXXXXXXX')
class Query():
    def setUp (self):
        # Configurações de acesso ao RavenDB da guiabdo: "usando PFX file para certificação"
        urls = "https://a.rdbguiando.ravendb.community"
        cert = {"pfx": "C:/Users/Victor Magal/Downloads/Raven/victormagalhaes.client.certificate/victormagalhaes.client.certificate.pfx", "password": "#YpzIf&t3dby"}
        self.store =  document_store.DocumentStore(urls=urls, database="automacao-faturas", certificate=cert)
        self.store.initialize()
          
    def query_where (self, id_fatura):
        # Query procurando pelo índice do banco Ex: where(informar no nome da coluna no banco, informar o valor procurado).
        with self.store.open_session() as session:
            query_results = list(session.query().where(id = id_fatura))
            return query_results        
            
    def query_where_equals (self, field_name, value):
        # Query procurando um ou outro where basta apagar ".adn_also()". Com isso funciona como "and".
        with self.store.open_session() as session:
            query_results = list(session.query().where_equals(field_name, value).and_also().where_equals("vl_total", "314,22"))
            print(query_results[0].vl_total)
            print(query_results[0].dt_vencimento)
            print(len(query_results))
            print('------------------------------')
            
    def query_on_date_time_range(self):
        # Query procurando por range da datas.
        with self.store.open_session() as session:
           query_results = list(session.query(collection_name="Parseamentos").where_between("at", '01/09/2021', '31/09/2021'))
           print(query_results)
           print(len(query_results))
           print('------------------------------')
