import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Usuarios')

print("Atualizando o item 'user001': adicionando email e mudando a idade...")

try:
    response = table.update_item(
        Key={
            'id': 'user001'
        },
        # Expressão que define o que será atualizado
        UpdateExpression="set idade = :i, email = :e",
        # Dicionário com os valores a serem usados na expressão
        ExpressionAttributeValues={
            ':i': 31,
            ':e': "joao.silva@example.com"
        },
        # Retorna o item como ele ficou APÓS a atualização
        ReturnValues="UPDATED_NEW"
    )
    print("Item atualizado com sucesso:", response['Attributes'])
except Exception as e:
    print(f"Ocorreu um erro ao atualizar o item: {e}")