from pyravendb.store import document_store
from pyravendb.raven_operations.operations import GetAttachmentOperation
from pyravendb.data.operation import AttachmentType

class Banco_nosql_raven_ged():
    def __init__(self):
        urls = "https://a.rdbguiando.ravendb.community"
        cert = {"pfx": "C:/Users/Victor Magal/Downloads/Raven/victormagalhaes.client.certificate/victormagalhaes.client.certificate.pfx", "password": "#YpzIf&t3dby"}
        store =  document_store.DocumentStore(urls=urls, database="GED", certificate=cert)
        store.initialize()
        
            
    def get_attachmentoperation(self, id_ged):
        operation = GetAttachmentOperation("GED", id_ged, AttachmentType.document, None)
        
        return operation

active_Banco_nosql_raven_ged = Banco_nosql_raven_ged()
documento = active_Banco_nosql_raven_ged.get_attachmentoperation("GEDFileDocuments/6170851-A")

print(documento)


