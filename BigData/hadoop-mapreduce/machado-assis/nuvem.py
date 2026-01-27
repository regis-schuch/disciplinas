from wordcloud import WordCloud
import matplotlib.pyplot as plt

texto = ""

with open("wordcount_machado.txt", encoding="utf-8") as f:
    for linha in f:
        palavra, contagem = linha.strip().split("\t")
        texto += ((palavra + " ") * int(contagem))

wc = WordCloud(width=1000, height=500, background_color="white").generate(texto)

plt.figure(figsize=(12,6))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.title("Nuvem de palavras – Machado de Assis")
plt.show()
