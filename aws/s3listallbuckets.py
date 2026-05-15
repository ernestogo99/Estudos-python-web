import boto3

# Cria um objeto de resource do S3
s3 = boto3.resource('s3')

print("Listando todos os buckets S3:")

# Itera sobre todos os buckets e imprime o nome de cada um
try:
    for bucket in s3.buckets.all():
        print(f"- {bucket.name}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")