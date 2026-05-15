import boto3

dynamodb = boto3.resource('dynamodb') # Especifique sua região
table_name = 'Pedidos'

print(f"Criando a tabela '{table_name}' com chave composta...")

try:
    table = dynamodb.create_table(
        TableName=table_name,
        # 1. Definimos AMBOS os atributos da chave
        AttributeDefinitions=[
            {
                'AttributeName': 'id_cliente', # Chave de Partição
                'AttributeType': 'S'           # 'S' para String
            },
            {
                'AttributeName': 'id_pedido',  # Chave de Classificação
                'AttributeType': 'S'
            }
        ],
        # 2. Especificamos o papel de cada atributo
        KeySchema=[
            {
                'AttributeName': 'id_cliente',
                'KeyType': 'HASH'  # HASH = Partition Key
            },
            {
                'AttributeName': 'id_pedido',
                'KeyType': 'RANGE' # RANGE = Sort Key
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )

    table.wait_until_exists()
    print(f"Tabela '{table_name}' criada com sucesso!")

except Exception as e:
    if 'ResourceInUseException' in str(e):
        print(f"A tabela '{table_name}' já existe.")
    else:
        print(f"Ocorreu um erro: {e}")