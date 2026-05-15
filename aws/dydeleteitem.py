import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Usuarios')

print("Deletando o item com id = 'user001'...")

try:
    table.delete_item(
        Key={
            'id': 'user001'
        }
    )
    print("Item deletado com sucesso!")
except Exception as e:
    print(f"Ocorreu um erro ao deletar o item: {e}")