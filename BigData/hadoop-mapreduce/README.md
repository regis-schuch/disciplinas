# WordCount com Hadoop Streaming – Obras de Machado de Assis

## Ambiente e instalação

Este experimento foi desenvolvido e testado em **Ubuntu 24.04 LTS**, com o **Apache Hadoop 3.x** instalado seguindo exatamente o passo a passo do tutorial oficial da Cherry Servers:

> https://www.cherryservers.com/blog/install-hadoop-ubuntu-2404

Recomenda-se utilizar o mesmo procedimento para garantir compatibilidade com os comandos e configurações descritos neste projeto.

---

## Objetivo

Este projeto tem como objetivo demonstrar, de forma **didática e prática**, o uso do modelo **MapReduce** com **Hadoop Streaming** para realizar a **contagem de palavras (WordCount)** em obras literárias de domínio público do escritor **Machado de Assis**.

Os textos utilizados são arquivos `.txt` obtidos a partir do **Projeto Gutenberg**:

> https://www.gutenberg.org/

Com o experimento buscamos entender:

- como funciona o processamento distribuído com Hadoop;
- o papel das fases **Map** e **Reduce**;
- como preparar dados textuais para análise;
- como calcular métricas sobre grandes volumes de texto.

---

## Estrutura do projeto

### Sistema de arquivos local (Linux)

```

~/BIG-DATA/machado_assis/
mapper.py
reducer.py
livro1.txt
livro2.txt
livro3.txt
livroN.txt

```

### HDFS (Hadoop)

```

/user/input            → arquivos de entrada (.txt)
/user/output/results   → saída do WordCount

````

---

## Pré-requisitos

- Ubuntu 24.04 LTS
- Apache Hadoop 3.x instalado conforme tutorial Cherry Servers
- HDFS e YARN em execução
- Usuário `hadoop`
- Python 3 instalado

---

## Passo a passo completo

### 1) Acessar o diretório dos livros

```bash
cd ~/BIG-DATA/machado_assis
ls
````

---

### 2) Criar o `mapper.py`

```bash
nano mapper.py
```

```python
#!/usr/bin/env python3
# mapper.py
#
# Objetivo: ler texto do STDIN (entrada padrão) e emitir pares:
#   palavra \t 1
# Esses pares serão agrupados e somados no reducer.py.

import sys

# Lê cada linha que chega pela entrada padrão (STDIN)
for linha in sys.stdin:
    # Remove espaços e quebra de linha do início e do fim
    linha = linha.strip()

    # Divide a linha em "palavras" separadas por espaços
    palavras = linha.split()

    # Para cada palavra, emite (palavra, 1)
    for palavra in palavras:
        # O Hadoop Streaming espera que a saída seja texto.
        # Usamos TAB (\t) para separar chave e valor.
        print(f"{palavra}\t1")
```

---

### 3) Criar o `reducer.py`

```bash
nano reducer.py
```

```python
#!/usr/bin/env python3
# reducer.py
#
# Objetivo: receber do STDIN pares no formato:
#   palavra \t contagem
# Como o Hadoop ordena as chaves, palavras iguais chegam juntas.
# O reducer soma as contagens e emite:
#   palavra \t total

import sys

palavra_atual = None
contagem_atual = 0

# Lê cada linha (já vinda da saída do mapper e ordenada pelo Hadoop)
for linha in sys.stdin:
    linha = linha.strip()

    # Separa "palavra" e "contagem" (separadas por TAB)
    try:
        palavra, contagem_str = linha.split('\t', 1)
        contagem = int(contagem_str)
    except ValueError:
        # Linha malformada: ignora
        continue

    # Se a palavra é a mesma que a anterior, acumula
    if palavra_atual == palavra:
        contagem_atual += contagem
    else:
        # Se mudou a palavra, emite o resultado da palavra anterior
        if palavra_atual is not None:
            print(f"{palavra_atual}\t{contagem_atual}")

        # Atualiza "estado" para a nova palavra
        palavra_atual = palavra
        contagem_atual = contagem

# Não esquecer de emitir a última palavra processada
if palavra_atual is not None:
    print(f"{palavra_atual}\t{contagem_atual}")
```

---

### 4) Tornar os scripts executáveis

```bash
chmod +x mapper.py reducer.py
ls -l mapper.py reducer.py
```

---

### 5) Teste local

```bash
cat dom_casmurro.txt | ./mapper.py | sort | ./reducer.py > /tmp/saida_wc.txt
head /tmp/saida_wc.txt
```

---

### 6) Verificar se Hadoop está rodando

```bash
jps
```

Se necessário:

```bash
start-dfs.sh
start-yarn.sh
```

---

### 7) Preparar o HDFS

```bash
hdfs dfs -mkdir -p /user/input
hdfs dfs -rm -r -f /user/input/*
hdfs dfs -put -f *.txt /user/input/
hdfs dfs -ls /user/input
```

---

### 8) Remover saída anterior

```bash
hdfs dfs -rm -r -f /user/output/results
hdfs dfs -mkdir -p /user/output
```

---

### 9) Executar o WordCount com Hadoop Streaming

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input /user/input/*.txt \
  -output /user/output/results \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py
```

---

### 10) Visualizar resultados

```bash
hadoop fs -cat /user/output/results/part-*
```

Top 30 palavras:

```bash
hadoop fs -cat /user/output/results/part-* | sort -nr -k2 | head -30
```

---

### 11) Métricas de exemplo

```bash
hadoop fs -cat /user/output/results/part-* | awk -F'\t' '{s+=$2} END {print s}'
hadoop fs -cat /user/output/results/part-* | wc -l
```

---

### 12) Salvar resultado localmente

```bash
hadoop fs -cat /user/output/results/part-* > wordcount_machado.txt
```

---

### 13) Reexecutar rapidamente

```bash
hdfs dfs -rm -r -f /user/output/results

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input /user/input/*.txt \
  -output /user/output/results \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py
```

---

## Licença dos textos

As obras utilizadas são de **domínio público**, obtidas do Projeto Gutenberg:

[https://www.gutenberg.org/](https://www.gutenberg.org/)

---

