import boto3

bucket_name = "boto3-aulanuvemufc"
folder_prefix = "musicas/"

s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)

print(f"Listando objetos no bucket '{bucket_name}':")

try:
    found_objects = False
    for obj in bucket.objects.filter(Prefix=folder_prefix):
        print(f"- Chave: {obj.key}, Tamanho: {obj.size} bytes, Última Modificação: {obj.last_modified}")
        found_objects = True

    if not found_objects:
        print(f"Nenhum objeto encontrado na pasta '{folder_prefix}'.")

except Exception as e:
    print(f"Ocorreu um erro ao listar objetos: {e}")