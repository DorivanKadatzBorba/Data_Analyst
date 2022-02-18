import acessando_blob_storage as dl

container='presentation'

# UPLOAD
arquivo_upload_origem='C:\\Users\\Dorivan\\Desktop\\stacklabs\\olist_customers_dataset.csv'
arquivo_upload_destino='olist_customers_dataset.csv'

#DOWNLOAD
#arquivo_download_origem='C:\\diretorio\\nome-do-arquivo'
#arquivo_download_destino='C:\\diretorio\\nome-do-arquivo'

dl.upload_blob(container, arquivo_upload_origem,arquivo_upload_destino)
#dl.download_blob(container, 'arquivo_download_origem', arquivo_download_destino)