import boto3

bucket_name = "boto3-aulanuvemufc"
object_key = "arquivos/teste.txt"
# Nome do arquivo a ser salvo localmente
download_path = "arquivo_baixado.txt"

s3 = boto3.resource('s3')

print(f"Baixando '{object_key}' de '{bucket_name}' para '{download_path}'...")

try:
    s3.Bucket(bucket_name).download_file(object_key, download_path)
    print("Download concluído com sucesso!")
except Exception as e:
    print(f"Ocorreu um erro no download: {e}")