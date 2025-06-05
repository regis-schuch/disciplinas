from confluent_kafka import Producer
import json
import random
from faker import Faker

# Inicializando o gerador de dados faker
fake = Faker()

# Configurações do Kafka
producer_config = {
    'bootstrap.servers': 'localhost:9092'  # Servidor Kafka
}

producer = Producer(producer_config)

# Função para callback
def delivery_report(err, msg):
    if err is not None:
        print(f'Erro ao enviar mensagem: {err}')
    else:
        print(f'Mensagem enviada: {msg.value().decode("utf-8")} para {msg.topic()}')

# Função para gerar dados dinâmicos
def gerar_dados():
    categorias = ["Eletrônicos", "Móveis", "Esportes", "Vestuário", "Livros"]
    produtos = [
        "Laptop", "Smartphone", "Tablet", "Monitor", "Teclado",
        "Mesa", "Cadeira", "Estante", "Sofá", "Cama",
        "Bicicleta", "Patins", "Capacete", "Bola", "Raquete",
        "Camisa", "Calça", "Jaqueta", "Tênis", "Mochila",
        "Livro de Ficção", "Livro de História", "Livro Técnico", "Revista", "Caderno"
    ]
    
    # Gera uma lista de registros dinâmicos
    registros = []
    for _ in range(10):  # Gerar 10 registros por execução
        produto = random.choice(produtos)
        categoria = random.choice(categorias)
        quantidade = random.randint(1, 10)  # Gerar quantidade aleatória
        preco = round(random.uniform(50, 5000), 2)  # Gerar preço aleatório
        total_vendas = round(quantidade * preco, 2)  # Calcular total de vendas

        registros.append({
            "Produto": produto,
            "Categoria": categoria,
            "Quantidade Vendida": quantidade,
            "Preço Unitário (R$)": preco,
            "Total de Vendas (R$)": total_vendas
        })
    return registros

# Gerar novos dados
data = gerar_dados()

# Controle para evitar duplicações: Criação de um conjunto com as chaves já enviadas
enviados = set()

for record in data:
    # Verifique se a chave já foi enviada
    if "Produto" in record:
        key = str(record["Produto"])
        if key not in enviados:
            try:
                producer.produce(
                    'sales-topic',  # Nome do tópico
                    key=key,
                    value=json.dumps(record),
                    callback=delivery_report
                )
                enviados.add(key)  # Marque a chave como enviada
            except Exception as e:
                print(f"Erro ao enviar mensagem para o Kafka: {e}")
        else:
            print(f"Mensagem duplicada detectada para o produto: {key}. Ignorando...")
    else:
        print("Registro inválido encontrado. Ignorando...")

# Aguarde o envio das mensagens
producer.flush()

