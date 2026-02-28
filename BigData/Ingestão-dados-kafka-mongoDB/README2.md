# Apache Kafka 4.2.0 (KRaft) no Windows & Integração com MongoDB

Este repositório contém o guia passo a passo para configurar um cluster Apache Kafka 4.2.0 no Windows, contendo 1 Controller e 3 Brokers. A segunda parte detalha um caso de uso prático integrando dados climáticos (Open-Meteo) com Kafka Connect e MongoDB.

---

## Parte 1: Apache Kafka 4.2.0 (KRaft) no Windows (1 Controller + 3 Brokers)

### 0) Pré-requisitos

#### 0.1 Java 17+
Instale o Java 17 ou superior e confirme no terminal:
```cmd
java -version

```

> Se o retorno for `'java' não é reconhecido`, configure o Java no `PATH` das variáveis de ambiente ou defina o `JAVA_HOME`.

### 1) Estrutura Esperada

* **Kafka extraído em:** `C:\kafka\kafka_2.13-4.2.0`
* **Diretórios de dados (vamos criar):**
* `C:\kafka\data\controller`
* `C:\kafka\data\broker1`
* `C:\kafka\data\broker2`
* `C:\kafka\data\broker3`


* **Portas:**
* **Controller:** 9093
* **Broker 1:** 9092
* **Broker 2:** 9094
* **Broker 3:** 9095



### 2) Corrigir erro do wmic (OBRIGATÓRIO no Windows)

Se você tentar iniciar o Kafka e aparecer `'wmic' não é reconhecido...`, é porque o script nativo do Kafka chama o `wmic` e as versões mais recentes do Windows não trazem mais esse recurso por padrão.

**2.1 Editar o arquivo do Kafka**
Abra o arquivo abaixo em um editor de texto:
`C:\kafka\kafka_2.13-4.2.0\bin\windows\kafka-server-start.bat`

Procure a linha:

```bat
wmic os get osarchitecture | find /i "32-bit" >nul 2>&1

```

E comente adicionando `rem` no início:

```bat
rem wmic os get osarchitecture | find /i "32-bit" >nul 2>&1

```

Salve o arquivo. Pronto: agora o `kafka-server-start.bat` vai funcionar no Windows. *(Se for usar o comando “stop”, faça o mesmo no `kafka-server-stop.bat`, mas para iniciar basta isso).*

### 3) Criar diretórios de dados

Abra o **PowerShell** e execute:

```powershell
mkdir C:\kafka\data -Force
mkdir C:\kafka\data\controller -Force
mkdir C:\kafka\data\broker1 -Force
mkdir C:\kafka\data\broker2 -Force
mkdir C:\kafka\data\broker3 -Force

```

Confirme se foram criados:

```powershell
dir C:\kafka\data

```

### 4) Criar os arquivos de configuração (Controller + 3 brokers)

Todos os arquivos devem ser criados/editados dentro da pasta: `C:\kafka\kafka_2.13-4.2.0\config`

#### 4.1 Controller — `controller.properties`

Crie ou edite o arquivo `C:\kafka\kafka_2.13-4.2.0\config\controller.properties` e cole EXATAMENTE o conteúdo abaixo:

```properties
process.roles=controller
node.id=1

# Modo dinâmico (Kafka 4.2): NÃO use controller.quorum.voters aqui
controller.quorum.bootstrap.servers=localhost:9093

listeners=CONTROLLER://localhost:9093
advertised.listeners=CONTROLLER://localhost:9093

controller.listener.names=CONTROLLER
listener.security.protocol.map=CONTROLLER:PLAINTEXT

log.dirs=C:/kafka/data/controller

```

#### 4.2 Broker 1 — `broker1.properties`

Crie o arquivo `C:\kafka\kafka_2.13-4.2.0\config\broker1.properties` e cole:

```properties
process.roles=broker
node.id=2

controller.quorum.bootstrap.servers=localhost:9093
controller.listener.names=CONTROLLER

listeners=PLAINTEXT://localhost:9092
inter.broker.listener.name=PLAINTEXT

listener.security.protocol.map=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT

log.dirs=C:/kafka/data/broker1

```

#### 4.3 Broker 2 — `broker2.properties`

Crie o arquivo `C:\kafka\kafka_2.13-4.2.0\config\broker2.properties` e cole:

```properties
process.roles=broker
node.id=3

controller.quorum.bootstrap.servers=localhost:9093
controller.listener.names=CONTROLLER

listeners=PLAINTEXT://localhost:9094
inter.broker.listener.name=PLAINTEXT

listener.security.protocol.map=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT

log.dirs=C:/kafka/data/broker2

```

#### 4.4 Broker 3 — `broker3.properties`

Crie o arquivo `C:\kafka\kafka_2.13-4.2.0\config\broker3.properties` e cole:

```properties
process.roles=broker
node.id=4

controller.quorum.bootstrap.servers=localhost:9093
controller.listener.names=CONTROLLER

listeners=PLAINTEXT://localhost:9095
inter.broker.listener.name=PLAINTEXT

listener.security.protocol.map=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT

log.dirs=C:/kafka/data/broker3

```

#### 4.5 Verificar se os arquivos existem

Execute no PowerShell para confirmar:

```powershell
dir C:\kafka\kafka_2.13-4.2.0\config\controller.properties
dir C:\kafka\kafka_2.13-4.2.0\config\broker1.properties
dir C:\kafka\kafka_2.13-4.2.0\config\broker2.properties
dir C:\kafka\kafka_2.13-4.2.0\config\broker3.properties

```

### 5) Zerar o ambiente (recomendado se já tentou antes)

Se você já tentou formatar antes e deu erro, apague tudo dentro de `C:\kafka\data` executando no PowerShell:

```powershell
Remove-Item -Recurse -Force C:\kafka\data\controller\*
Remove-Item -Recurse -Force C:\kafka\data\broker1\*
Remove-Item -Recurse -Force C:\kafka\data\broker2\*
Remove-Item -Recurse -Force C:\kafka\data\broker3\*

```

### 6) Inicializar (formatar) o cluster

Entre na pasta raiz do Kafka:

```powershell
cd C:\kafka\kafka_2.13-4.2.0

```

#### 6.1 Gerar um Cluster ID

```powershell
.\bin\windows\kafka-storage.bat random-uuid

```

Copie o ID retornado (exemplo fictício: `z1JSGYgQRu2vwHQBCimL8g`). Vamos chamá-lo de `<CLUSTER_ID>`.

#### 6.2 Formatar o Controller (standalone)

Substitua `<CLUSTER_ID>` pelo ID gerado:

```powershell
.\bin\windows\kafka-storage.bat format -t <CLUSTER_ID> -c .\config\controller.properties --standalone

```

Confirme se formatou corretamente:

```powershell
dir C:\kafka\data\controller

```

Devem existir os arquivos: `meta.properties`, `bootstrap.checkpoint` e a pasta `__cluster_metadata-0`.

#### 6.3 Formatar os 3 brokers (com o mesmo Cluster ID)

```powershell
.\bin\windows\kafka-storage.bat format -t <CLUSTER_ID> -c .\config\broker1.properties
.\bin\windows\kafka-storage.bat format -t <CLUSTER_ID> -c .\config\broker2.properties
.\bin\windows\kafka-storage.bat format -t <CLUSTER_ID> -c .\config\broker3.properties

```

Confirme a criação do `meta.properties` em cada um:

```powershell
dir C:\kafka\data\broker1\meta.properties
dir C:\kafka\data\broker2\meta.properties
dir C:\kafka\data\broker3\meta.properties

```

### 7) Subir o cluster (ordem correta)

Abra **4 janelas distintas do PowerShell** (uma para cada processo).

**7.1 Controller**

```powershell
cd C:\kafka\kafka_2.13-4.2.0
.\bin\windows\kafka-server-start.bat .\config\controller.properties

```

**7.2 Broker 1**

```powershell
cd C:\kafka\kafka_2.13-4.2.0
.\bin\windows\kafka-server-start.bat .\config\broker1.properties

```

**7.3 Broker 2**

```powershell
cd C:\kafka\kafka_2.13-4.2.0
.\bin\windows\kafka-server-start.bat .\config\broker2.properties

```

**7.4 Broker 3**

```powershell
cd C:\kafka\kafka_2.13-4.2.0
.\bin\windows\kafka-server-start.bat .\config\broker3.properties

```

### 8) Testes (validação do cluster)

Abra um terminal novo para realizar os testes.

#### 8.1 Verificar broker respondendo

```powershell
cd C:\kafka\kafka_2.13-4.2.0
.\bin\windows\kafka-broker-api-versions.bat --bootstrap-server localhost:9092

```

Se listar as versões sem erros, está OK.

#### 8.2 Criar tópico "tempo"

```powershell
.\bin\windows\kafka-topics.bat --create --topic tempo --bootstrap-server localhost:9092 --replication-factor 3 --partitions 3

```

Listar os tópicos:

```powershell
.\bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092

```

Descrever o tópico detalhadamente:

```powershell
.\bin\windows\kafka-topics.bat --describe --topic tempo --bootstrap-server localhost:9092

```

#### 8.3 Producer

Abra um terminal novo para enviar mensagens:

```powershell
.\bin\windows\kafka-console-producer.bat --topic tempo --bootstrap-server localhost:9092

```

Digite mensagens de teste e pressione Enter:

```text
Ola Kafka
Teste Kafka

```

#### 8.4 Consumer

Abra um terminal novo para consumir as mensagens:

```powershell
.\bin\windows\kafka-console-consumer.bat --topic tempo --bootstrap-server localhost:9092 --from-beginning

```

Você deve ver as mensagens digitadas no Producer.

---

### 9) Funcionamento Interno (Didático)

#### 9.1 Log Distribuído

O Kafka armazena as mensagens em um log que é ordenado por *offset* (deslocamento).

#### 9.2 Estrutura Lógica

```text
Topic "tempo"
 ├── Partition 0
 ├── Partition 1
 └── Partition 2

```

* O **Producer** envia mensagens para o tópico.
* O Kafka decide para qual **partition** a mensagem vai (por chave, *round-robin*, etc.).
* O **Consumer** lê as mensagens das partitions.

#### 9.3 Estrutura Física (no disco)

Exemplo de caminho: `C:\kafka\data\broker1\tempo-0`
Arquivos típicos que você encontrará lá dentro:

* `00000000000000000000.log` → dados brutos (as mensagens em si)
* `00000000000000000000.index` → índice por offset
* `00000000000000000000.timeindex` → índice por tempo

#### 9.4 Segments

Cada partition é dividida em segmentos (arquivos `.log`) com o objetivo de:

* Facilitar a retenção e a limpeza de dados antigos.
* Melhorar a performance geral.
* Evitar a criação de arquivos gigantescos no disco.

> Quando um arquivo `.log` cresce até o limite configurado, o Kafka fecha esse arquivo e cria um novo segmento.

#### 9.5 Replicação

Com o comando `replication-factor=3` executado anteriormente:

* Cada partition possui 3 cópias no cluster (1 *Leader* + 2 *Followers*).
* O **Leader** é quem atende as requisições de leitura e escrita.
* Os **Followers** apenas replicam os dados do Leader e assumem a liderança automaticamente caso o Leader caia.

---

---

## Parte 2: Caso de Uso - Kafka 4.2.0 + Open-Meteo + Kafka Connect + MongoDB (Compass)

Neste laboratório, vamos capturar dados de uma API climática, jogar no Kafka e enviar automaticamente para o MongoDB via Kafka Connect.

### Estrutura Usada

```text
C:\Kafka\
├── kafka_2.13-4.2.0\
├── data\
├── connectors\
└── batch\

```

### 1) Pré-requisitos

#### 1.1 Java

Verifique a versão:

```cmd
java -version

```

#### 1.2 MongoDB

Certifique-se de que o MongoDB está instalado e acessível via MongoDB Compass no endereço:
`mongodb://localhost:27017`

> **Observação:** O banco de dados e a coleção só aparecerão no Compass *depois* que o primeiro documento for gravado.

### 2) Kafka 4.2.0 (Validação)

Assumindo que o cluster do passo anterior já está rodando, valide o broker:

```powershell
cd C:\Kafka\kafka_2.13-4.2.0
.\bin\windows\kafka-broker-api-versions.bat --bootstrap-server localhost:9092

```

### 3) Criar tópico exclusivo para JSON

Isto evita que mensagens em “texto puro” caiam no tópico e quebrem o MongoDB Sink Connector.
Crie o tópico:

```powershell
cd C:\Kafka\kafka_2.13-4.2.0
.\bin\windows\kafka-topics.bat --create --topic tempo_json --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1

```

### 4) Baixar e instalar o MongoDB Sink Connector (2.0.3)

#### 4.1 Baixar (Confluent Hub)

Acesse a página oficial: [MongoDB Kafka Connector no Confluent Hub](https://www.confluent.io/hub/mongodb/kafka-connect-mongodb)
Baixe o arquivo: `mongodb-kafka-connect-mongodb-2.0.3.zip`

#### 4.2 Extrair para a pasta de plugins

Extraia o conteúdo para: `C:\Kafka\connectors\`
O resultado esperado é ter o `.jar` acessível neste caminho:
`C:\Kafka\connectors\mongodb-kafka-connect-mongodb-2.0.3\lib\mongo-kafka-connect-2.0.3-confluent.jar`

### 5) Ajustar o connect-standalone.properties

Edite o arquivo: `C:\Kafka\kafka_2.13-4.2.0\config\connect-standalone.properties`

#### 5.1 Configurações Obrigatórias

Garanta que existam estas linhas com estes exatos valores no final do arquivo:

```properties
bootstrap.servers=localhost:9092
listeners=http://localhost:8083
plugin.path=C:/Kafka/connectors

key.converter=org.apache.kafka.connect.storage.StringConverter
value.converter=org.apache.kafka.connect.json.JsonConverter
value.converter.schemas.enable=false

```

### 6) Iniciar Kafka Connect (standalone)

Abra um **PowerShell novo** e execute:

```powershell
cd C:\Kafka\kafka_2.13-4.2.0
.\bin\windows\connect-standalone.bat .\config\connect-standalone.properties

```

#### 6.1 Testar se o Connect subiu

Em outro terminal PowerShell, dispare:

```powershell
curl -UseBasicParsing http://localhost:8083/

```

Deve retornar um JSON com a versão e o cluster id do Kafka Connect.

#### 6.2 Confirmar que o plugin do MongoDB foi carregado

```powershell
Invoke-RestMethod http://localhost:8083/connector-plugins | ConvertTo-Json -Depth 5

```

Você deve ver na saída a classe: `com.mongodb.kafka.connect.MongoSinkConnector`.

### 7) Criar o arquivo do conector MongoDB (JSON)

Crie o arquivo em `C:\Kafka\batch\mongodb-tempo-sink.json` e insira o conteúdo:

```json
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

```

### 8) Registrar o conector no Kafka Connect

No PowerShell, faça o POST da configuração via REST API:

```powershell
$body = Get-Content "C:\Kafka\batch\mongodb-tempo-sink.json" -Raw

Invoke-RestMethod `
-Method Post `
-Uri "http://localhost:8083/connectors" `
-ContentType "application/json" `
-Body $body

```

#### 8.1 Verificar status do Conector

```powershell
Invoke-RestMethod "http://localhost:8083/connectors/mongodb-tempo-sink/status" | ConvertTo-Json -Depth 20

```

O retorno esperado é ter tanto o *connector* quanto a *task* como `RUNNING`.

### 9) Producer Open-Meteo → Kafka

Crie o script em Python no arquivo `C:\Kafka\batch\open-meteo-to-kafka.py`:

```python
import time
import json
import requests
from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': 'localhost:9092'})
TOPICO = 'tempo_json'

def enviar_dados():
    while True:
        r = requests.get("[https://api.open-meteo.com/v1/forecast?latitude=-29.171&longitude=-53.5&current_weather=true](https://api.open-meteo.com/v1/forecast?latitude=-29.171&longitude=-53.5&current_weather=true)")
        if r.status_code == 200:
            tempo = r.json().get("current_weather", {})
            tempo["timestamp"] = time.strftime('%Y-%m-%dT%H:%M:%S')
            producer.produce(TOPICO, value=json.dumps(tempo))
            producer.flush()
            print("Enviado:", tempo)
        time.sleep(10)

if __name__ == "__main__":
    enviar_dados()

```

Execute o script:

```cmd
python C:\Kafka\batch\open-meteo-to-kafka.py

```

### 10) Validar que o Kafka está recebendo os dados

Em um terminal novo:

```powershell
cd C:\Kafka\kafka_2.13-4.2.0
.\bin\windows\kafka-console-consumer.bat --topic tempo_json --bootstrap-server localhost:9092 --from-beginning

```

Você deverá ver mensagens no formato JSON aparecendo na tela.

### 11) Ver os dados no MongoDB Compass

1. Conecte-se no MongoDB Compass na URI: `mongodb://localhost:27017`
2. Agora devem aparecer na barra lateral:
* **database:** `clima_db`
* **collection:** `tempo_now`


3. Se não aparecer imediatamente, clique no botão **Refresh**.

> *Lembrete: O banco só “existe” fisicamente no MongoDB quando o primeiro documento é gravado com sucesso.*

---

### Resumo do Fluxo (O que está acontecendo)

1. **Producer Python:** Lê a API pública do Open-Meteo e publica um payload JSON no tópico `tempo_json` do Kafka.
2. **Kafka Brokers:** Gravam esses eventos (JSON) em disco, distribuindo-os em partições/segmentos.
3. **Kafka Connect:** Lê continuamente as mensagens do tópico `tempo_json` e converte o JSON lido em formato interno utilizando o `JsonConverter` (com `schemas.enable=false`).
4. **MongoDB Sink Connector:** Pega esses dados do Connect e realiza o *insert* de cada mensagem como um documento na coleção `tempo_now` do banco `clima_db`.
5. **Compass:** Interface gráfica que exibe o banco assim que os dados são persistidos no MongoDB.

```
