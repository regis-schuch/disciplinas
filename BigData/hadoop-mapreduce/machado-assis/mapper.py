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
