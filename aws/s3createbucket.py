import boto3
import uuid # Para gerar um nome único

# O nome do bucket deve ser único globalmente
# Usamos uuid para ajudar a criar um nome único
bucket_name = "boto3-aulanuvemufc"
region = 'us-east-1' # Ou a sua região de preferência

s3 = boto3.resource('s3')

print(f"Criando o bucket '{bucket_name}' na região '{region}'...")

try:
    if region == 'us-east-1':
        s3.create_bucket(Bucket=bucket_name)
    else:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': region}
        )
    print("Bucket criado com sucesso!")
except Exception as e:
    print(f"Não foi possível criar o bucket: {e}")