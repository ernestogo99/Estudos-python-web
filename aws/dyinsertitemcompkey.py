import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Pedidos')

# Pedido 1 para o cliente123
print("Inserindo o primeiro pedido para o cliente 'cliente123'...")
table.put_item(
   Item={
        'id_cliente': 'cliente1235',
        'id_pedido': 'pedido002',
        'data_pedido': '2025-10-02T14:30:00Z',
        'valor_total': 150,
        'status': 'ENVIADO'
    }
)

# Pedido 2 para o mesmo cliente123
print("Inserindo o segundo pedido para o cliente 'cliente123'...")
table.put_item(
   Item={
        'id_cliente': 'cliente1234',
        'id_pedido': 'pedido001',
        'data_pedido': '2025-10-28T18:00:00Z',
        'valor_total': 50,
        'status': 'PAGAMENTO_APROVADO'
    }
)

print("Itens inseridos com sucesso!")