import boto3

bucket_name = "boto3-a1187173-c639-47c9-9c40-b4875c7eb77f"
object_key = "documentos/meu_arquivo_na_nuvem.txt"

s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)

# 1. Deletar o objeto
print(f"Deletando o objeto '{object_key}'...")
try:
    s3.Object(bucket_name, object_key).delete()
    print("Objeto deletado com sucesso.")
except Exception as e:
    print(f"Erro ao deletar objeto: {e}")


# 2. Deletar o bucket (agora que está vazio)
print(f"Deletando o bucket '{bucket_name}'...")
try:
    bucket.delete()
    print("Bucket deletado com sucesso.")
except Exception as e:
    print(f"Erro ao deletar o bucket: {e}")