Apache Kafka 4.2.0 (KRaft) no Windows (1 Controller + 3 Brokers)
0) Pré-requisitos
0.1 Java 17+
Instale Java 17+ e confirme:
java -version
Se der 'java' não é reconhecido, configure o Java no PATH ou defina JAVA_HOME.
1) Estrutura esperada
Kafka extraído em:
C:\kafka\kafka_2.13-4.2.0
Diretórios de dados (vamos criar):
C:\kafka\data\controller
C:\kafka\data\broker1
C:\kafka\data\broker2
C:\kafka\data\broker3
Portas:
Controller: 9093
Broker1: 9092
Broker2: 9094
Broker3: 9095
2) Corrigir erro do wmic (OBRIGATÓRIO no Windows)
Se você tentar iniciar Kafka e aparecer:
'wmic' não é reconhecido...
é porque o script do Kafka chama wmic e o Windows não tem mais isso.
2.1 Editar o arquivo do Kafka
Abra este arquivo:
C:\kafka\kafka_2.13-4.2.0\bin\windows\kafka-server-start.bat
Procure a linha:
wmic os get osarchitecture | find /i "32-bit" >nul 2>&1
E comente assim:
rem wmic os get osarchitecture | find /i "32-bit" >nul 2>&1
Salve o arquivo.
Pronto: agora o kafka-server-start.bat vai funcionar no Windows.
Se também for usar “stop”, depois fazemos o mesmo no kafka-server-stop.bat, mas para iniciar basta o start.
3) Criar diretórios de dados
No PowerShell:
mkdir C:\kafka\data -Force
mkdir C:\kafka\data\controller -Force
mkdir C:\kafka\data\broker1 -Force
mkdir C:\kafka\data\broker2 -Force
mkdir C:\kafka\data\broker3 -Force
Confirme:
dir C:\kafka\data
4) Criar os arquivos de configuração (Controller + 3 brokers)
Todos ficam em:
C:\kafka\kafka_2.13-4.2.0\config
4.1 Controller — controller.properties
Crie/edite:
C:\kafka\kafka_2.13-4.2.0\config\controller.properties
Cole EXATAMENTE:
process.roles=controller
node.id=1

# Modo dinâmico (Kafka 4.2): NÃO use controller.quorum.voters aqui
controller.quorum.bootstrap.servers=localhost:9093

listeners=CONTROLLER://localhost:9093
advertised.listeners=CONTROLLER://localhost:9093

controller.listener.names=CONTROLLER
listener.security.protocol.map=CONTROLLER:PLAINTEXT

log.dirs=C:/kafka/data/controller
4.2 Broker 1 — broker1.properties (SE NÃO TIVER, ENTÃO DEVE SER CRIADO)
Crie:
C:\kafka\kafka_2.13-4.2.0\config\broker1.properties
Cole:
process.roles=broker
node.id=2

controller.quorum.bootstrap.servers=localhost:9093
controller.listener.names=CONTROLLER

listeners=PLAINTEXT://localhost:9092
inter.broker.listener.name=PLAINTEXT

listener.security.protocol.map=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT

log.dirs=C:/kafka/data/broker1

4.3 Broker 2 — broker2.properties
Crie:
C:\kafka\kafka_2.13-4.2.0\config\broker2.properties
Cole:
process.roles=broker
node.id=3

controller.quorum.bootstrap.servers=localhost:9093
controller.listener.names=CONTROLLER

listeners=PLAINTEXT://localhost:9094
inter.broker.listener.name=PLAINTEXT

listener.security.protocol.map=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT

log.dirs=C:/kafka/data/broker2

4.4 Broker 3 — broker3.properties
Crie:
C:\kafka\kafka_2.13-4.2.0\config\broker3.properties
Cole:
process.roles=broker
node.id=4

controller.quorum.bootstrap.servers=localhost:9093
controller.listener.names=CONTROLLER

listeners=PLAINTEXT://localhost:9095
inter.broker.listener.name=PLAINTEXT

listener.security.protocol.map=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT

log.dirs=C:/kafka/data/broker3

4.5 Verificar se os arquivos existem
dir C:\kafka\kafka_2.13-4.2.0\config\controller.properties
dir C:\kafka\kafka_2.13-4.2.0\config\broker1.properties
dir C:\kafka\kafka_2.13-4.2.0\config\broker2.properties
dir C:\kafka\kafka_2.13-4.2.0\config\broker3.properties

5) Zerar o ambiente (recomendado se já tentou antes)
Se já tentou formatar antes, apague tudo dentro de C:\kafka\data:
Remove-Item -Recurse -Force C:\kafka\data\controller\*
Remove-Item -Recurse -Force C:\kafka\data\broker1\*
Remove-Item -Recurse -Force C:\kafka\data\broker2\*
Remove-Item -Recurse -Force C:\kafka\data\broker3\*
6) Inicializar (formatar) o cluster
Entre na pasta do Kafka:
cd C:\kafka\kafka_2.13-4.2.0
6.1 Gerar um Cluster ID
.\bin\windows\kafka-storage.bat random-uuid
Copie o ID retornado (exemplo fictício):
z1JSGYgQRu2vwHQBCimL8g
Vamos chamar de <CLUSTER_ID>.

6.2 Formatar o Controller (standalone)
.\bin\windows\kafka-storage.bat format -t <CLUSTER_ID> -c .\config\controller.properties --standalone
Confirme:
dir C:\kafka\data\controller
Deve existir:
meta.properties
bootstrap.checkpoint
__cluster_metadata-0
6.3 Formatar os 3 brokers (mesmo Cluster ID)
.\bin\windows\kafka-storage.bat format -t <CLUSTER_ID> -c .\config\broker1.properties
.\bin\windows\kafka-storage.bat format -t <CLUSTER_ID> -c .\config\broker2.properties
.\bin\windows\kafka-storage.bat format -t <CLUSTER_ID> -c .\config\broker3.properties
Confirme meta.properties:
dir C:\kafka\data\broker1\meta.properties
dir C:\kafka\data\broker2\meta.properties
dir C:\kafka\data\broker3\meta.properties
7) Subir o cluster (ordem correta)
Abra 4 janelas do PowerShell.
7.1 Controller
cd C:\kafka\kafka_2.13-4.2.0
.\bin\windows\kafka-server-start.bat .\config\controller.properties
7.2 Broker 1
cd C:\kafka\kafka_2.13-4.2.0
.\bin\windows\kafka-server-start.bat .\config\broker1.properties
7.3 Broker 2
cd C:\kafka\kafka_2.13-4.2.0
.\bin\windows\kafka-server-start.bat .\config\broker2.properties
7.4 Broker 3
cd C:\kafka\kafka_2.13-4.2.0
.\bin\windows\kafka-server-start.bat .\config\broker3.properties
8) Testes (validação do cluster)
Abra um terminal novo para testes.
8.1 Verificar broker respondendo
cd C:\kafka\kafka_2.13-4.2.0
.\bin\windows\kafka-broker-api-versions.bat --bootstrap-server localhost:9092
Se listar versões → OK.
8.2 Criar tópico tempo
.\bin\windows\kafka-topics.bat --create --topic tempo --bootstrap-server localhost:9092 --replication-factor 3 --partitions 3
Listar tópicos:
.\bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092
Descrever tópico:
.\bin\windows\kafka-topics.bat --describe --topic tempo --bootstrap-server localhost:9092
8.3 Producer
Abra um terminal novo:
.\bin\windows\kafka-console-producer.bat --topic tempo --bootstrap-server localhost:9092
Digite:
Ola Kafka
Teste Kafka
8.4 Consumer
Abra um terminal novo:
.\bin\windows\kafka-console-consumer.bat --topic tempo --bootstrap-server localhost:9092 --from-beginning
Você deve ver as mensagens.

9) Funcionamento interno (didático)
9.1 Log distribuído
Kafka armazena mensagens em um log ordenado por offset.
9.2 Estrutura lógica
Topic "tempo"
 ├── Partition 0
 ├── Partition 1
 ├── Partition 2
Producer envia mensagens para o tópico.
Kafka decide a partition (por chave, round-robin, etc.).
Consumer lê as partitions.
9.3 Estrutura física (no disco)
Exemplo:
C:\kafka\data\broker1\tempo-0
Arquivos típicos:
00000000000000000000.log → dados (mensagens)
00000000000000000000.index → índice por offset
00000000000000000000.timeindex → índice por tempo
9.4 Segments
Cada partition é dividida em segmentos (.log) para:
facilitar retenção e limpeza
melhorar performance
evitar arquivos gigantes
Quando o .log cresce, o Kafka cria um novo segmento.
9.5 Replicação
Com replication-factor=3:
cada partition tem 3 cópias (1 leader + 2 followers)
leader atende leituras/escritas
followers replicam e assumem se necessário



Caso de Uso -  Kafka 4.2.0 + Open-Meteo + Kafka Connect + MongoDB (Compass)
Estrutura usada (igual a sua)
C:\Kafka\
├── kafka_2.13-4.2.0\
├── data\
├── connectors\
└── batch\
1) Pré-requisitos
1.1 Java
Verifique:
java -version
1.2 MongoDB
MongoDB instalado e acessível no Compass em mongodb://localhost:27017
Observação: o banco/coleção só aparece no Compass depois que o primeiro documento for gravado.

2) Kafka 4.2.0 (assumindo que já está funcionando)
Validar o broker com:
cd C:\Kafka\kafka_2.13-4.2.0
.\bin\windows\kafka-broker-api-versions.bat --bootstrap-server localhost:9092
3) Criar tópico exclusivo para JSON 
Isso evita que mensagens “texto puro” quebrem o MongoDB Sink.
Crie o tópico:
cd C:\Kafka\kafka_2.13-4.2.0

.\bin\windows\kafka-topics.bat --create --topic tempo_json --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
4) Baixar e instalar o MongoDB Sink Connector (2.0.3)
4.1 Baixar (Confluent Hub)
Página oficial:
https://www.confluent.io/hub/mongodb/kafka-connect-mongodb
Baixe:
mongodb-kafka-connect-mongodb-2.0.3.zip
4.2 Extrair para a pasta de plugins (igual a sua)
Extrair para:
C:\Kafka\connectors\
Resultado esperado:
C:\Kafka\connectors\mongodb-kafka-connect-mongodb-2.0.3\lib\mongo-kafka-connect-2.0.3-confluent.jar
5) Ajustar o connect-standalone.properties 
Arquivo:
C:\Kafka\kafka_2.13-4.2.0\config\connect-standalone.properties
5.1 O que precisa ficar obrigatoriamente correto
Garanta que existam estas linhas e com esses valores:
bootstrap.servers=localhost:9092
listeners=http://localhost:8083
plugin.path=C:/Kafka/connectors

key.converter=org.apache.kafka.connect.storage.StringConverter
value.converter=org.apache.kafka.connect.json.JsonConverter
value.converter.schemas.enable=false
6) Iniciar Kafka Connect (standalone)
Abrir um PowerShell novo e execute:
cd C:\Kafka\kafka_2.13-4.2.0

.\bin\windows\connect-standalone.bat .\config\connect-standalone.properties
6.1 Testar se o Connect subiu
Em outro PowerShell:
curl -UseBasicParsing http://localhost:8083/
Deve retornar JSON com versão e cluster id.
6.2 Confirmar que o plugin foi carregado
Invoke-RestMethod http://localhost:8083/connector-plugins | ConvertTo-Json -Depth 5
Deve aparecer algo como:
com.mongodb.kafka.connect.MongoSinkConnector

7) Criar o arquivo do conector MongoDB (JSON)
Salvar em:
C:\Kafka\batch\mongodb-tempo-sink.json
Conteúdo:
{
  "name": "mongodb-tempo-sink",
  "config": {
    "connector.class": "com.mongodb.kafka.connect.MongoSinkConnector",
    "tasks.max": "1",
    "topics": "tempo_json",
    "connection.uri": "mongodb://localhost:27017",
    "database": "clima_db",
    "collection": "tempo_now",
    "key.converter": "org.apache.kafka.connect.storage.StringConverter",
    "value.converter": "org.apache.kafka.connect.json.JsonConverter",
    "value.converter.schemas.enable": "false",
    "errors.tolerance": "all"
  }
}
8) Registrar o conector no Kafka Connect
No PowerShell:
$body = Get-Content "C:\Kafka\batch\mongodb-tempo-sink.json" -Raw

Invoke-RestMethod `
-Method Post `
-Uri "http://localhost:8083/connectors" `
-ContentType "application/json" `
-Body $body
8.1 Verificar status
Invoke-RestMethod "http://localhost:8083/connectors/mongodb-tempo-sink/status" | ConvertTo-Json -Depth 20
Esperado:
connector: RUNNING
task: RUNNING
9) Producer Open-Meteo → Kafka
Arquivo:
C:\Kafka\batch\open-meteo-to-kafka.py
Código:
import time
import json
import requests
from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': 'localhost:9092'})
TOPICO = 'tempo_json'

def enviar_dados():
    while True:
        r = requests.get("https://api.open-meteo.com/v1/forecast?latitude=-29.171&longitude=-53.5&current_weather=true")
        if r.status_code == 200:
            tempo = r.json().get("current_weather", {})
            tempo["timestamp"] = time.strftime('%Y-%m-%dT%H:%M:%S')
            producer.produce(TOPICO, value=json.dumps(tempo))
            producer.flush()
            print("Enviado:", tempo)
        time.sleep(10)

if __name__ == "__main__":
    enviar_dados()
Executar:
python C:\Kafka\batch\open-meteo-to-kafka.py

10) Validar que o Kafka está recebendo
Em outro terminal:
cd C:\Kafka\kafka_2.13-4.2.0

.\bin\windows\kafka-console-consumer.bat --topic tempo_json --bootstrap-server localhost:9092 --from-beginning
Você deve ver mensagens JSON.
11) Ver no MongoDB Compass
Conecte no Compass:
mongodb://localhost:27017
Agora deve aparecer:
database: clima_db
collection: tempo_now
Se não aparecer, clique Refresh.
Lembre: o banco só “existe” no MongoDB quando o primeiro documento é gravado.
O que está acontecendo em cada etapa (resumo)
Producer Python lê Open-Meteo e publica JSON no tópico tempo_json.
Kafka grava esses eventos em disco (partições/segmentos).
Kafka Connect lê o tópico e converte o JSON usando JsonConverter com schemas.enable=false.
MongoDB Sink Connector insere cada mensagem como documento em clima_db.tempo_now.
Compass mostra o banco quando já existe dado persistido.
