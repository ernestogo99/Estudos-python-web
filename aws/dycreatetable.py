import boto3

# Cria o resource do DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1') # Especifique sua região

table_name = 'Usuarios'

print(f"Criando a tabela '{table_name}'...")

try:
    table = dynamodb.create_table(
        TableName=table_name,
        # Define os atributos que farão parte da chave
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'  # 'S' para String, 'N' para Number, 'B' para Binary
            }
        ],
        # Define qual atributo é qual parte da chave
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'  # HASH = Partition Key
            }
        ],
        # Define a capacidade de leitura/escrita (mínimo para o free tier)
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )

    # Espera até que a tabela seja criada e esteja ATIVA
    table.wait_until_exists()
    print(f"Tabela '{table_name}' criada com sucesso!")

except Exception as e:
    # Trata o caso em que a tabela já existe
    if 'ResourceInUseException' in str(e):
        print(f"A tabela '{table_name}' já existe.")
    else:
        print(f"Ocorreu um erro: {e}")