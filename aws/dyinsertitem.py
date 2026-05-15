import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Usuarios')

print("Inserindo um novo item na tabela 'Usuarios'...")

try:
    response = table.put_item(
       Item={
            'id': 'user002',
            'nome': 'João Silva',
            'idade': 35,
            'cidade': 'São Paulo',
            'email': 'joao.silva@example.com'
        }
    )
    print("Item inserido com sucesso!")
    # print(response) # Descomente para ver a resposta completa da AWS
except Exception as e:
    print(f"Ocorreu um erro ao inserir o item: {e}")