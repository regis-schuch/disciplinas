
# Documentação Formal da Gramática — iDevS DSL

## Definição Geral

A gramática da DSL **iDevS** foi projetada para descrever **processos de integração de serviços digitais** com ênfase em segurança, isolamento e execução confiável, compatível com **Trusted Execution Environments (TEEs)** como **CHERI/Morello**.

Esta gramática foi implementada usando **ANTLR 4**, baseada em uma **Context-Free Grammar (CFG)**, e permite definir:

Ela permite descrever:

- Infraestrutura de execução segura.
- Serviços externos (APIs, bancos, mensageria).
- Troca de chaves.
- Processos de integração, steps e ações.

---

## Gramática Completa

```antlr
grammar iDevS;

integrationSolution
    : 'IntegrationSolution' STRING '{'
        infrastructure
        services
        keysExchange?
        process+
      '}'
    ;

infrastructure
    : 'Infrastructure' '{'
        launcher
        secureHardware
        compartment
        rootOfTrust
        sourceCode
      '}'
    ;

launcher        : 'Launcher' STRING;
secureHardware  : 'SecureHardware' STRING;
compartment     : 'Compartment' STRING;
rootOfTrust     : 'RootOfTrust' STRING;
sourceCode      : 'SourceCode' STRING;

services
    : 'Services' '{' service+ '}'
    ;

service
    : ('API' | 'Database' | 'Queue' | 'File' | 'Custom') STRING '{' attrPair* '}'
    ;

attrPair : ID '=' value ;

value
    : STRING
    | [0-9]+ ('.' [0-9]+)?
    | 'true'
    | 'false'
    ;

keysExchange
    : 'KeysExchange' '{' (programKey | serviceKey)+ '}'
    ;

programKey
    : 'ProgramPublicKey' STRING
    ;

serviceKey
    : 'ServicePublicKey' STRING
    ;

process
    : 'Process' STRING '{'
        'uses' '[' serviceRef (',' serviceRef)* ']'
        step+
      '}'
    ;

serviceRef
    : STRING | ID
    ;

step
    : 'Step' STRING '{' action+ '}'
    ;

action
    : read
    | write
    | ifblock
    | forblock
    | transform
    | storeLocal
    | retrieveLocal
    ;

read        : 'Read' 'from' serviceRef ;
write       : 'Write' 'to' serviceRef ;
ifblock     : 'If' STRING '{' action+ '}' ;
forblock    : 'For' ID 'in' serviceRef '{' action+ '}' ;
transform   : 'Transform' 'input=' ID 'operation=' STRING 'output=' ID ;
storeLocal  : 'StoreLocalData' 'input=' ID ;
retrieveLocal: 'RetrieveLocalData' 'output=' ID ;

ID      : [a-zA-Z_][a-zA-Z_0-9]* ;
STRING  : '"' (~["\
])* '"' ;
WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;
```

---

## Estrutura Resumida

| Bloco               | Descrição                                        |
|---------------------|--------------------------------------------------|
| `IntegrationSolution`| Raiz, define toda a solução de integração       |
| `Infrastructure`     | Launcher, hardware, compartimento, rootOfTrust |
| `Services`           | Define serviços externos (API)        |
| `KeysExchange`       | Define chaves públicas                         |
| `Process`            | Pipeline com steps                             |
| `Step`               | Etapas do pipeline                             |
| `Action`             | Ações (Read, Write, If, For, etc)              |


---

## **Explicação Detalhada dos Blocos da Gramática**

---

### **Bloco: `IntegrationSolution` (Raiz)**

```antlr
integrationSolution
    : 'IntegrationSolution' STRING '{'
        infrastructure
        services
        keysExchange?
        process+
      '}'
    ;
```

Representa a **solução completa de integração**.
Atributo:

`STRING`: Nome da solução (`"PurchasePipeline"`, `"InventorySync"`, etc.).
Contém obrigatoriamente:

- `infrastructure`: Infraestrutura segura.
- `services`: Definição dos serviços externos.
- Um ou mais `process`: Definição dos pipelines de integração.
- Opcional:
  
      - `keysExchange`: Configuração da troca de chaves.

---

### **Bloco: `Infrastructure`**

```antlr
infrastructure
    : 'Infrastructure' '{'
        launcher
        secureHardware
        compartment
        rootOfTrust
        sourceCode
      '}'
    ;
```

Descreve o ambiente seguro.
Subcomponentes:

  * `Launcher`: Entidade responsável pela orquestração e attestation.
  * `SecureHardware`: Define o hardware seguro (ex.: `"MorelloBoard"`).
  * `Compartment`: Nome do compartimento seguro.
  * `RootOfTrust`: Entidade certificadora.
  * `SourceCode`: Arquivo de código fonte associado.

---

### **Bloco: `Services`**

```antlr
services
    : 'Services' '{' service+ '}'
    ;
```

Lista os serviços externos utilizados no processo.
Cada serviço é definido com:

```antlr
service
    : ('API' | 'Database' | 'Queue' | 'File' | 'Custom') STRING '{' attrPair* '}'
    ;
```

Tipos de serviços:

- `API`, `Database`, `Queue`, `File` ou `Custom`.

Atributos:

- `STRING`: Nome do serviço (`"Store"`, `"Taxi"`, `"Messaging"`).

Permite adicionar atributos livres via `attrPair`:

```antlr
attrPair : ID '=' value ;
```

Exemplo:

```plaintext
API "Store" { url = "https://store.api.com" }
```

---

### **Bloco: `KeysExchange`**

```antlr
keysExchange
    : 'KeysExchange' '{' (programKey | serviceKey)+ '}'
    ;
```

Descreve a configuração de chaves e certificados.
Suporte a:

- `ProgramPublicKey`: Chave pública do programa seguro.
- `ServicePublicKey`: Chaves públicas dos serviços.

Exemplo:

```plaintext
KeysExchange {
    ProgramPublicKey "PurchaseFlow"
    ServicePublicKey "Store"
    ServicePublicKey "Taxi"
    ServicePublicKey "Messaging"
}
```

---

### **Bloco: `Process` (Pipeline de Integração)**

```antlr
process
    : 'Process' STRING '{'
        'uses' '[' serviceRef (',' serviceRef)* ']'
        step+
      '}'
    ;
```

- Define um pipeline de integração.
- `STRING`: Nome do processo (`"PurchaseFlow"`).
- Atributo `uses`: Lista os serviços que o processo irá consumir.
- Contém uma sequência de `step`.

---

### **Bloco: `Step` (Etapas do Processo)**

```antlr
step
    : 'Step' STRING '{' action+ '}'
    ;
```

- Define uma etapa do pipeline.
- A etapa contém uma ou mais `action`.

---

### **Bloco: `Action` (Ações dentro de Steps)**

```antlr
action
    : read
    | write
    | ifblock
    | forblock
    | transform
    | storeLocal
    | retrieveLocal
    ;
```

**Ações Suportadas:**

| Ação            | Descrição                                                                            |
| --------------- | ------------------------------------------------------------------------------------ |
| `Read`          | Leitura de dados de um serviço (`Read from Store`)                                   |
| `Write`         | Escrita em um serviço (`Write to Taxi`)                                              |
| `If`            | Bloco condicional (`If "purchase >= 150" { ... }`)                                   |
| `For`           | Loop sobre elementos de um serviço (`For item in Store { ... }`)                     |
| `Transform`     | Operação de transformação (`Transform input=price operation="* 2" output=new_price`) |
| `StoreLocal`    | Armazena dados localmente (`StoreLocalData input=order_id`)                          |
| `RetrieveLocal` | Recupera dados locais (`RetrieveLocalData output=order_id`)                          |

---

### **Tokens Léxicos**

```antlr
ID      : [a-zA-Z_][a-zA-Z_0-9]* ;
STRING  : '"' (~["\\\r\n])* '"' ;
WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;
```

- **ID:** Identificadores de variáveis e serviços.
- **STRING:** Sequências entre aspas (`"example"`).
- **VALUE:** Pode ser `STRING`, número (`123` ou `45.67`), ou booleano (`true`/`false`).
- Suporte a comentários de linha (`// comentário`).
