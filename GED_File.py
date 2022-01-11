from pyravendb.store import document_store
from pyravendb.raven_operations.operations import GetAttachmentOperation
from pyravendb.data.operation import AttachmentType

print('XXXXXXX... GED_File...XXXXXXXXXXXXX')
class Query():
    def setUp (self):
        urls = "https://a.rdbguiando.ravendb.community"
        cert = {"pfx": "C:/Users/Victor Magal/Downloads/Raven/victormagalhaes.client.certificate/victormagalhaes.client.certificate.pfx", "password": "#YpzIf&t3dby"}
        self.store =  document_store.DocumentStore(urls=urls, database="GED", certificate=cert)
        self.store.initialize()
          
    def query_where (self, Name_fatura):
        with self.store.open_session() as session:
            query_results = list(session.query().where(Name = Name_fatura))
            return query_results        
        
        
    def get_attachmentoperation(self, entity_or_document_id, name):
        operation = GetAttachmentOperation(entity_or_document_id, name, AttachmentType.document, None)
        
        print(operation, type(operation))
        print('-------')
       # print(operation.Name)
        return self.store.operations.send(operation)
            
    
    
    
Query_active = Query()
Query_active.setUp()
query_results = Query_active.query_where('0152965091_201805.pdf')



Query_active.get_attachmentoperation("GED", '0152965091_201805.pdf')


# print(query_results[0])
# print(len(query_results))