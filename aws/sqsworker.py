import boto3
import json
import time
import sys

# Cole a URL da fila criada no setup
QUEUE_URL = "https://sqs.us-east-1.amazonaws.com/303787634525/fila-processamento-videos"

sqs_client = boto3.client('sqs', region_name='us-east-1')

# Pegamos um ID para o worker a partir da linha de comando
worker_id = sys.argv[1] if len(sys.argv) > 1 else "worker_default"
print(f"--- Worker '{worker_id}' INICIADO ---")

while True:
    print(f"[{worker_id}] Procurando por tarefas...")
    response = sqs_client.receive_message(
        QueueUrl=QUEUE_URL,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=5
    )
    
    if 'Messages' in response:
        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']
        tarefa = json.loads(message['Body'])
        
        print(f"[{worker_id}] INICIOU o processamento da tarefa {tarefa['tarefa_id']} para o arquivo '{tarefa['arquivo_video']}'")
        time.sleep(5) # Simula o trabalho pesado de processar o vídeo
        print(f"[{worker_id}] COMPLETOU o processamento da tarefa {tarefa['tarefa_id']}.")
        
        # Deleta a mensagem para que outro worker não a processe
        sqs_client.delete_message(QueueUrl=QUEUE_URL, ReceiptHandle=receipt_handle)
    # else:
    #     print(f"[{worker_id}] Nenhuma tarefa encontrada.")