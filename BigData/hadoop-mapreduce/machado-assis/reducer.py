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
