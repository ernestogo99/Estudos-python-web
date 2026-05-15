import boto3

bucket_name = "boto3-aulanuvemufc"

s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)

print(f"Listando objetos no bucket '{bucket_name}':")

try:
    for obj in bucket.objects.all():
        print(f"- Chave: {obj.key}, Tamanho: {obj.size} bytes, Última Modificação: {obj.last_modified}")
except Exception as e:
    print(f"Ocorreu um erro ao listar objetos: {e}")