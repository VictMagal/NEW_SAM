from pyravendb.store import document_store
from pyravendb.raven_operations.operations import GetAttachmentOperation
from pyravendb.data.operation import AttachmentType

class Banco_nosql_raven_ged():
    def __init__(tabela_twm):
        '''
            @tabela_twm: Tabela gerada pela busca no banco SQL do TWM, contendo as principais campos usados. Ex: Identificador, Chave_ged...    
            @urls: Link do domínio da guiando no RavenDB
            @cert: Arquivo .Pfx de acesso ao link (cert e password geradas pela Infra da guiando)
        '''
        urls = "https://a.rdbguiando.ravendb.community"
        cert = {"pfx": "C:/Users/Victor Magal/Downloads/Raven/victormagalhaes.client.certificate/victormagalhaes.client.certificate.pfx", "password": "#YpzIf&t3dby"}
        store =  document_store.DocumentStore(urls=urls, database="GED", certificate=cert)
        store.initialize()
        
        for new_id_ged_raven in tabela_twm['new_id_ged_raven']:
            new_id_ged_raven = str(new_id_ged_raven)
            operation = Banco_nosql_raven_ged.get_attachmentoperation(new_id_ged_raven)
        
        return operation
            
    def get_attachmentoperation(id_ged):
        operation = GetAttachmentOperation("GED", id_ged, AttachmentType.document, None)
        
        return operation
    