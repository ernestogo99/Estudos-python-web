import boto3

sqs_client = boto3.client('sqs', region_name='us-east-1')
response = sqs_client.create_queue(QueueName='fila-processamento-videos')
queue_url = response['QueueUrl']
print(f"Fila criada: {queue_url}")
#https://sqs.us-east-1.amazonaws.com/303787634525/fila-processamento-videos