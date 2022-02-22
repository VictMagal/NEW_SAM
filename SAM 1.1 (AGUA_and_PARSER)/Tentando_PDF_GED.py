from pyravendb.store import document_store
from pyravendb.raven_operations.operations import GetAttachmentOperation
from pyravendb.data.operation import AttachmentType

class Banco_nosql_raven_ged():
    def __init__(self):
        urls = "https://a.rdbguiando.ravendb.community"
        cert = {"pfx": "C:/Users/Victor Magal/Downloads/Raven/victormagalhaes.client.certificate/victormagalhaes.client.certificate.pfx", "password": "#YpzIf&t3dby"}
        self.store =  document_store.DocumentStore(urls=urls, database="GED", certificate=cert)
        self.store.initialize()
        
            
    def get_attachmentoperation(self, id_ged, identificador_pdf):
        
        # operation = self.store.operations.send(GetAttachmentOperation(id_ged, identificador_pdf, AttachmentType.document, None))
        # print(operation)
        # print()
        
        with self.store.open_session() as session:
            download = session.advanced.attachment.get(id_ged, identificador_pdf)
            documents = session.advanced.stream(id_ged)
        
        print(download)
        print()
        print(documents)
       
        return

active_Banco_nosql_raven_ged = Banco_nosql_raven_ged()
documento = active_Banco_nosql_raven_ged.get_attachmentoperation("GEDFileDocuments/162177-A", '98641473_180610.pdf')

f = open("C:/Users/Victor Magal/Desktop/SAM (AGUA_and_PARSER)/topology_files/acb60650eff1d498c2577d2480961ce1.raven-topology", "rb", buffering=0)
print(f)
print()
line1 = f.readline()
print(line1)



