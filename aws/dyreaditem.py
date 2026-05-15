import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Usuarios')

print("Buscando o item com id = 'user001'...")

try:
    response = table.get_item(
        Key={
            'id': 'user002'
        }
    )
    
    if 'Item' in response:
        item = response['Item']
        print("Item encontrado:", item)
    else:
        print("Item com id 'user001' não encontrado.")
        
except Exception as e:
    print(f"Ocorreu um erro ao buscar o item: {e}")