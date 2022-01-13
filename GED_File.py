from pyravendb.store import document_store
from pyravendb.raven_operations.operations import GetAttachmentOperation
from pyravendb.data.operation import AttachmentType

class QueryGED():
    def setUpged (self):
        print('XXXXXXX... GED_File...XXXXXXXXXXXXX')
        urls = "https://a.rdbguiando.ravendb.community"
        cert = {"pfx": "C:/Users/Victor Magal/Downloads/Raven/victormagalhaes.client.certificate/victormagalhaes.client.certificate.pfx", "password": "#YpzIf&t3dby"}
        self.store =  document_store.DocumentStore(urls=urls, database="GED", certificate=cert)
        self.store.initialize()
        
    def query_where (self, Name_fatura):
        with self.store.open_session() as session:
            print(Name_fatura)
            query_results = list(session.query().where(Id = "GEDFileDocuments/5783192-A"))
            
            
            print('query_results', query_results)
            return query_results        
            
    def get_attachmentoperation(self, entity_or_document_id, Name_fatura):
        print(Name_fatura)
        operation = GetAttachmentOperation(entity_or_document_id, Name_fatura, AttachmentType.document, None)
        print('operation', operation)
        return self.store.operations.send(operation)
    
