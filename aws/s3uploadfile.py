import boto3

# Substitua pelo nome do seu bucket
bucket_name = "boto3-aulanuvemufc" 
# Caminho do arquivo local
file_path = "teste.txt" 
# Nome que o objeto terá no S3
object_key = "musicas/mus2.mp3" 

s3 = boto3.resource('s3')

print(f"Fazendo upload de '{file_path}' para '{bucket_name}/{object_key}'...")

try:
    s3.Bucket(bucket_name).upload_file(file_path, object_key)
    print("Upload concluído com sucesso!")
except Exception as e:
    print(f"Ocorreu um erro no upload: {e}")