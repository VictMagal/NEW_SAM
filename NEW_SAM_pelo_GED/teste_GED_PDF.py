from pyravendb.store import document_store
from pyravendb.raven_operations.operations import GetAttachmentOperation
from pyravendb.data.operation import AttachmentType
import pickle
import io
from PIL import Image
import img2pdf
import base64
import zipfile
from io import BytesIO
from pdf2image import convert_from_path
import os

# Inicialização do Raven usando certificação PFX (arquivo .pfx disponibilizado pela infra da guiando)
urls = "https://a.rdbguiando.ravendb.community"
cert = {"pfx": "C:/Users/Victor Magal/Downloads/Raven/victormagalhaes.client.certificate/victormagalhaes.client.certificate.pfx", "password": "#YpzIf&t3dby"}
store =  document_store.DocumentStore(urls=urls, database="GED", certificate=cert)
store.initialize()

# Retornando arquivo do GED: @GED é o nome do banco; 
banco = 'GED'
fatura = 'GEDFileDocuments/6110935-A'

operation = GetAttachmentOperation(banco, fatura, AttachmentType.document, None)
print(operation)



print(operation, '-' , type(operation))

# Transformando em arquivo de bytes
arq_bytes = pickle.dumps(operation)
print(arq_bytes)
print(type(arq_bytes))
print()


bytesio_o = io.BytesIO(arq_bytes)
print(bytesio_o)

# os.startfile(bytesio_o)

#Salva o arquivo em algum formato .bin .pdf .jpeg
with open("testando.pdf", "wb") as f:
    f.write(bytesio_o.getbuffer())
# Cria um zip
zip_buffer = io.BytesIO()
with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
    for file_name, data in [('1.pdf', io.BytesIO(arq_bytes))]:
        zip_file.writestr(file_name, data.getvalue())
#salva o arquivo em zip    
with open('1.zip', 'wb') as f:
    f.write(zip_buffer.getvalue())






# images = convert_from_path('testando.pdf')
 
# for i in range(len(images)):
   
#       # Save pages as images in the pdf
#     images[i].save('page'+ str(i) +'.jpg', 'JPEG')








# Imagem tif em bytes
name_img = 'EXEMPLO_TIF.tif'

varbinary = io.open(name_img, 'rb').read()
#print(varbinary)
print(type(varbinary))
print()
# Convertendo para BytesIO para a leitura de seus metadados
image_data = Image.open(io.BytesIO(varbinary))
print(type(image_data))
num_pages = image_data.n_frames


# Imprimindo o número  de páginas
print('NUMERO DE PAGINAS: ', num_pages)

# Convertendo o arquivo tif em PDF
convert_pdf = img2pdf.convert(varbinary)


zip_buffer = io.BytesIO()
with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
    for file_name, data in [('1.pdf', io.BytesIO(convert_pdf))]:
        zip_file.writestr(file_name, data.getvalue())
        
        
# Imprime o zip em bytes
#print(zip_buffer.getvalue())

#Para salvar o arquivo localmente
# with open('1.zip', 'wb') as f:
#     f.write(zip_buffer.getvalue())

zip_base64 = base64.encodebytes(zip_buffer.getvalue())
#print(zip_base64)