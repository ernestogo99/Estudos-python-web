import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Usuarios')

print("Deletando a tabela 'Usuarios'...")

try:
    table.delete()
    table.wait_until_not_exists() # Espera a tabela ser de fato deletada
    print("Tabela deletada com sucesso!")
except Exception as e:
    print(f"Ocorreu um erro ao deletar a tabela: {e}")