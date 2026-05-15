import boto3
import json
import uuid

# Cole a URL da fila criada no setup
QUEUE_URL = "https://sqs.us-east-1.amazonaws.com/303787634525/fila-processamento-videos"

sqs_client = boto3.client('sqs', region_name='us-east-1')

def enviar_tarefas(num_tarefas=5):
    print(f"Enviando {num_tarefas} tarefas para a fila...")
    for i in range(num_tarefas):
        tarefa = {
            'tarefa_id': str(uuid.uuid4()),
            'arquivo_video': f'video_{i+1}.mp4'
        }
        sqs_client.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(tarefa)
        )
        print(f"  -> Tarefa {tarefa['tarefa_id']} enviada.")

if __name__ == '__main__':
    enviar_tarefas()