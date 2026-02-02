---
marp: true
theme: gaia
_class: lead
backgroundColor: #f0f4f8
backgroundImage: url('https://source.unsplash.com/1600x900/?technology,abstract')
color: #ffffff
---

# Como o Apache Spark Pensa?
## Uma introdução didática à arquitetura de Big Data

<br>

**Professor(a):** [Seu Nome Aqui]

---

# O Problema do "Jeito Antigo"
## (A Motivação)

![bg left:40%](https://source.unsplash.com/800x600/?old,computer,harddrive)

* **O Cenário:** Você tem 10 Terabytes de dados para processar.
* **A Solução Antiga (tipo MapReduce):**
    * Divide o trabalho, mas salva tudo no **Disco Rígido** a cada passo.
    * **Problema:** O disco é LENTO. É como ter que guardar os ingredientes na geladeira toda vez que você corta um legume.
* **A Revolução Spark:** E se mantivéssemos os ingredientes na bancada (Memória RAM) o tempo todo?

---

# A Grande Analogia: A Cozinha Profissional

Vamos imaginar que o Spark é um grande restaurante para entender como ele se organiza.

![bg right:45%](https://source.unsplash.com/800x600/?chef,commercial+kitchen,cooking)

1.  **O Chefe de Cozinha (Driver):**
    * Ele não corta cebola. Ele tem a receita na cabeça e comanda a equipe.
2.  **Os Cozinheiros (Executors):**
    * Eles põem a mão na massa nas suas estações. Eles têm sua própria bancada (Memória RAM).
3.  **O Gerente do Restaurante (Cluster Manager):**
    * Contrata os cozinheiros e garante que não faltem facas e fogões (Recursos de CPU/Memória).

---

# A Arquitetura Técnica (Traduzindo)

Os nomes reais dos componentes que vimos na analogia.

<br>

<div style="display: flex; justify-content: space-around; align-items: center;">
    <div style="text-align: center; border: 2px solid #007bff; padding: 20px; border-radius: 10px; background-color: #e6f2ff;">
        <h3>🧠 DRIVER<br>(O Cérebro)</h3>
        <p>Onde roda o `main()`.<br>Cria o plano de voo.</p>
    </div>
    <div style="font-size: 3rem;">➡</div>
    <div style="text-align: center; border: 2px solid #28a745; padding: 20px; border-radius: 10px; background-color: #e6ffe6;">
        <h3>💪 EXECUTORS<br>(Os Músculos)</h3>
        <p>Processos distribuídos.<br>Executam e guardam cache.</p>
    </div>
</div>

---

# O Segredo da Velocidade: A "Preguiça" Inteligente

**Lazy Evaluation (Avaliação Preguiçosa)**

O Spark não faz nada imediatamente. Ele cria um plano primeiro.

![bg left:35%](https://source.unsplash.com/800x600/?planning,blueprint,strategy)

* Se você pedir: *"Leia o arquivo, filtre os erros, conte as linhas".*
* **O que ele faz agora:** Nada. Ele apenas anota esses passos em uma lista de tarefas (chamada DAG).
* **Por que isso é bom?** Ele pode olhar a lista inteira depois e encontrar o caminho mais rápido antes de gastar energia.

---

# As Ordens que você dá ao Spark

Existem apenas dois tipos de comandos no código Spark:

<br>

| Tipo | O que é? (Analogia) | Exemplos |
| :--- | :--- | :--- |
| **Transformações** <br>(São Preguiçosas) | **As Receitas:** Dizem *como* os dados devem mudar, mas não executam agora. | `map`, `filter`, `groupByKey` |
| **Ações** <br>(O Gatilho) | **O Pedido do Cliente:** Obrigam o Spark a parar de planejar e entregar um resultado real. | `count`, `save`, `show`, `collect` |

---

# A Hierarquia do Trabalho

Quando você chama uma **Ação**, o Spark divide o trabalho assim:

![bg right:40%](https://source.unsplash.com/800x600/?hierarchy,structure,organization)

1.  **JOB (O Projeto):** O objetivo final (ex: o relatório completo).
    * ⬇ *divide em*
2.  **STAGES (Etapas):** Fases do trabalho. Uma etapa termina quando os dados precisam mudar de lugar.
    * ⬇ *divide em*
3.  **TASKS (Tarefas):** A menor unidade.
    * ⭐ **Regra de Ouro:** 1 Task cuida de 1 pedaço de dados (Partição). 100 partições = 100 tasks.

---

# O Momento Crítico: O Shuffle

Quando os "Cozinheiros" precisam trocar ingredientes entre si.

![bg left:40%](https://source.unsplash.com/800x600/?traffic,network,chaos,wires)

* A maioria das operações é rápida porque cada executor trabalha isolado com seus dados.
* Mas, operações como `groupBy` ou `join` exigem que dados viajem pela rede de um computador para outro.
* **Isso é o SHUFFLE.**
* É a parte mais lenta e custosa do Spark. Evite shuffles desnecessários!

---

# Recapitulação: O que aprendemos?

![bg right:30%](https://source.unsplash.com/800x600/?success,learning,graduation)

1.  Spark ama **Memória RAM** (por isso é rápido).
2.  O **Driver** planeja, os **Executors** trabalham.
3.  Ele usa **Lazy Evaluation** (preguiça) para otimizar o plano antes de executar.
4.  **Ações** disparam o trabalho real; Transformações são apenas planos.
5.  Cuidado com o **Shuffle** (tráfego de rede).

<br>

## Obrigado!
