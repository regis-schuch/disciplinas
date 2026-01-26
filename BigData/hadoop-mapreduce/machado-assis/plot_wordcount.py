import pandas as pd
import matplotlib.pyplot as plt

ARQUIVO_ENTRADA = "wordcount_machado.txt"
TOP_N = 20

def main():
    # Carrega dados
    df = pd.read_csv(
        ARQUIVO_ENTRADA,
        sep="\t",
        names=["palavra", "contagem"],
        encoding="utf-8"
    )

    # Ordena por frequência
    df_top = df.sort_values(by="contagem", ascending=False).head(TOP_N)

    # Cria gráfico
    plt.figure(figsize=(12, 6))
    plt.bar(df_top["palavra"], df_top["contagem"])

    plt.title("Top palavras mais frequentes – Obras de Machado de Assis")
    plt.xlabel("Palavra")
    plt.ylabel("Frequência")

    plt.xticks(rotation=60, ha="right")
    plt.tight_layout()

    # Salva e mostra
    plt.savefig("top_palavras_machado.png", dpi=150)
    plt.show()

    print("Gráfico salvo em: top_palavras_machado.png")

if __name__ == "__main__":
    main()
