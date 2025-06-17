
# 📑 Documentação da Sintaxe da DSL — iDevS

## 📜 Visão Geral da DSL

A DSL (**Domain-Specific Language**) iDevS foi projetada para descrever:

- 🏗️ A infraestrutura de execução (compartimentos, launcher, root of trust, hardware).
- 🔑 A gestão de chaves e segurança.
- 🔁 O fluxo de processos de integração entre serviços digitais.
- 🔗 As interações com APIs, bancos de dados, serviços de mensageria ou sistemas externos.

Ela permite transformar modelos textuais diretamente em código C executável e seguro.

## 🔤 Regras Gerais da Sintaxe

- ✅ **Case-sensitive.**
- ✅ As strings são delimitadas por aspas (`"`).
- ✅ Atribuições usam `=`.
- ✅ Blocos são definidos entre `{ ... }`.
- ✅ Listas usam colchetes `[ ... ]`.
- ✅ Cada declaração dentro de um bloco é separada por quebras de linha.

## 🏗️ Estrutura Global da DSL

```plaintext
IntegrationSolution "NOME_DO_MODELO" {
    Infrastructure { ... }
    Services { ... }
    KeysExchange { ... }
    Process "NOME_DO_PROCESSO" { ... }
}
```

... (continuação conforme conteúdo completo enviado)
