# Documentação da Sintaxe da DSL — iDevS

## Visão Geral da DSL

A DSL (**Domain-Specific Language**) iDevS foi projetada para descrever:

- A infraestrutura de execução (compartimentos, launcher, root of trust, hardware).
- A gestão de chaves.
- O fluxo de processos de integração entre serviços digitais.
- As interações com APIs de serviços digitais externos.

Ela permite transformar modelos textuais diretamente em código C.

## Regras Gerais da Sintaxe

- **Case-sensitive.**
- As strings são delimitadas por aspas (`"`).
- Atribuições usam `=`.
- Blocos são definidos entre `{ ... }`.
- Listas usam colchetes `[ ... ]`.
- Cada declaração dentro de um bloco é separada por quebras de linha.

## Estrutura Global da DSL

```plaintext
IntegrationSolution "NOME_DO_MODELO" {
    Infrastructure { ... }
    Services { ... }
    KeysExchange { ... }
    Process "NOME_DO_PROCESSO" { ... }
}
```
---

## **Bloco Infrastructure**

Define a infraestrutura segura que executará o processo.

```plaintext
Infrastructure {
    Launcher "NOME_DO_LAUNCHER"
    SecureHardware "NOME_DO_HARDWARE"
    Compartment "NOME_DO_COMPARTIMENTO"
    RootOfTrust "NOME_DA_CA"
    SourceCode "NOME_DO_CODIGO.c"
}
```

| Elemento         | Descrição                                |
| ---------------- | ---------------------------------------- |
| `Launcher`       | Entidade que orquestra execução e chaves |
| `SecureHardware` | Hardware seguro (ex.: MorelloBoard)      |
| `Compartment`    | Compartimento de execução isolado        |
| `RootOfTrust`    | Autoridade certificadora                 |
| `SourceCode`     | Arquivo fonte C vinculado ao processo    |

---

## **Bloco Services**

Define os serviços digitais utilizados no processo.

```plaintext
Services {
    API "Store" { url = "https://store.api.com" }
    API "Taxi" { url = "https://taxi.api.com" }
    API "Messaging" { url = "https://msg.api.com" }
}
```

| Tipo de Serviço | Descrição                                 |
| --------------- | ----------------------------------------- |
| `API`           | Serviços REST, SOAP, Web API              |
| `Database`      | Bancos de dados                           |
| `Queue`         | Filas, brokers de mensagens               |
| `File`          | Arquivos locais ou remotos                |
| `Custom`        | Serviço específico, definido pelo usuário |

Cada serviço pode ter atributos em pares chave-valor (`attr = valor`).

---

## **Bloco KeysExchange**

Define a troca de chaves públicas entre programa (processo de integração) e serviços.

```plaintext
KeysExchange {
    ProgramPublicKey "NOME_DO_PROCESSO"
    ServicePublicKey "Store"
    ServicePublicKey "Taxi"
    ServicePublicKey "Messaging"
}
```

Isso garante que os participantes possuem chaves válidas para assinatura, criptografia e autenticação.

---

## **Bloco Process**

Define o processo de integração, os serviços usados e as etapas.

```plaintext
Process "PurchaseFlow" {
    uses ["Store", "Taxi", "Messaging"]

    Step "RetrievePurchase" {
        Read from Store
    }

    Step "CheckAndBook" {
        If "purchase >= 150" {
            Write to Taxi
            Write to Messaging
        }
    }

    Step "Archive" {
        Write to Messaging
    }
}
```

| Elemento | Descrição                                        |
| -------- | ------------------------------------------------ |
| `uses`   | Lista de serviços envolvidos no processo         |
| `Step`   | Etapa do processo (pode ter várias por processo) |
| `Action` | Ação dentro da etapa (ver abaixo)                |

---

## **Ações Suportadas (`Actions`)**

### **Read**

```plaintext
Read from <Service>
```

Lê dados de um serviço.

---

### **Write**

```plaintext
Write to <Service>
```

Escreve dados em um serviço.

---

### **If (condicional)**

```plaintext
If "condição" {
    <ações>
}
```

Executa as ações internas **se a condição for verdadeira.**

---

### **For (loop)**

```plaintext
For <variável> in <Service> {
    <ações>
}
```

Executa ações para cada item retornado do serviço.

---

### **Transform (transformação de dados)**

```plaintext
Transform input=VAR operation="OP" output=VAR
```

Aplica uma transformação.

---

### **StoreLocalData / RetrieveLocalData**

```plaintext
StoreLocalData input=VAR
RetrieveLocalData output=VAR
```

Armazena ou recupera dados localmente durante a execução do processo.

---

## **Validação da Sintaxe**

A sintaxe é validada automaticamente pelo parser ANTLR com a gramática definida no arquivo:

```plaintext
grammar/iDevS.g4
```
