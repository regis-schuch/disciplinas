from confluent_kafka import Consumer
from pymongo import MongoClient, errors
import json

# Configurações do Kafka
consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'sales-consumer-group',
    'auto.offset.reset': 'earliest'  # Começa do início se o offset não estiver armazenado
}

consumer = Consumer(consumer_config)
consumer.subscribe(['sales-topic'])

# Configuração do MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["sales_db"]
sales_collection = db["raw_sales_data"]  # Coleção para armazenar os dados brutos

# Criação de índice no MongoDB (otimização)
sales_collection.create_index("Produto", unique=False)

# Consumo contínuo
try:
    print("Consumindo mensagens do Kafka...")
    while True:
        msg = consumer.poll(1.0)  # Tempo de espera para novas mensagens

        if msg is None:
            continue
        if msg.error():
            print(f"Erro: {msg.error()}")
            continue

        # Parse da mensagem recebida
        try:
            record = json.loads(msg.value().decode('utf-8'))
            print(f"Mensagem recebida: {record}")

            # Validação dos campos
            required_fields = {"Produto", "Categoria", "Quantidade Vendida", "Preço Unitário (R$)", "Total de Vendas (R$)"}
            if not required_fields.issubset(record.keys()):
                print(f"Mensagem inválida: {record}")
                continue

            # Inserir no MongoDB
            try:
                sales_collection.insert_one(record)
                print(f"Registro inserido no MongoDB: {record}")
            except errors.PyMongoError as e:
                print(f"Erro ao inserir no MongoDB: {e}")

        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")

except KeyboardInterrupt:
    print("Encerrando consumidor...")
finally:
    consumer.close()

