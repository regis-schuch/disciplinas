
# 📜 Documentação Formal da Gramática — iDevS DSL

## 🔗 Definição Geral

A gramática da DSL iDevS foi implementada utilizando **ANTLR 4**, seguindo os princípios de uma **context-free grammar (CFG)**.

Ela permite descrever:

- 🏗️ Infraestrutura de execução segura.
- 🔗 Serviços externos (APIs, bancos, mensageria).
- 🔐 Troca de chaves.
- 🔁 Processos de integração, steps e ações.

---

## 🔤 Gramática Completa

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

## 🏗️ Estrutura Resumida

| Bloco               | Descrição                                        |
|---------------------|--------------------------------------------------|
| `IntegrationSolution`| Raiz, define toda a solução de integração       |
| `Infrastructure`     | Launcher, hardware, compartimento, rootOfTrust |
| `Services`           | Define serviços externos (API, DB, etc)        |
| `KeysExchange`       | Define chaves públicas                         |
| `Process`            | Pipeline com steps                             |
| `Step`               | Etapas do pipeline                             |
| `Action`             | Ações (Read, Write, If, For, etc)              |

---

## 🔥 Por que documentar?

- ✅ Validação formal da linguagem.
- ✅ Base para artigos, teses e documentação técnica.
- ✅ Facilita manutenção, extensão e evolução da DSL.
- ✅ Clareza e robustez para qualquer desenvolvedor ou pesquisador.

---

**Grupo de Computação Aplicada (GCA) — Unijuí**  
**Projeto CAMB — University of Cambridge**
