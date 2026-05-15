import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Pedidos')

print("Buscando todos os pedidos do cliente 'cliente123'...")

try:
    # A operação query USA a chave de partição para a busca
    response = table.query(
        # KeyConditionExpression define o critério de busca na chave primária
        KeyConditionExpression=Key('id_cliente').eq('cliente12345')
    )
    
    items = response.get('Items', [])
    
    if not items:
        print("Nenhum pedido encontrado para o cliente 'cliente123'.")
    else:
        print("Pedidos encontrados:")
        for item in items:
            print(f"- Pedido: {item['id_pedido']}, Status: {item['status']}, Valor: {item['valor_total']}")
            
except Exception as e:
    print(f"Ocorreu um erro ao fazer a query: {e}")