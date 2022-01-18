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
        
    def get_attachmentoperation(self, entity_or_document_id, Name_fatura):
        print(Name_fatura)
        operation = GetAttachmentOperation(entity_or_document_id, Name_fatura, AttachmentType.document, None)
        #print('operation PDF:', operation)
        return operation
    
