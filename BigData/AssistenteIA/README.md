# Assistente de IA para Triagem Clínica

Este projeto implementa um assistente de IA com interface web para triagem clínica automatizada, utilizando embeddings semânticos, banco vetorial (ChromaDB) e modelo local (Mistral via Ollama).

---

## Visão Geral

O assistente recebe sintomas clínicos como entrada, encontra casos semelhantes num banco vetorial e classifica o paciente segundo o **Protocolo de Manchester**, fornecendo também condutas iniciais.

---

## Pré-requisitos

- **Sistema operacional:** Windows 10 ou superior
- **Memória RAM recomendada:** 8GB ou mais
- **Espaço em disco:** 10GB+

---

## Etapas de Instalação

### 1. Instalar o Ollama

- Acesse: [https://ollama.com/download](https://ollama.com/download)
- Após a instalação, execute no terminal para testar:
  ```bash
  ollama list
  ```

---

### 2. Baixar o modelo `mistral`

```bash
ollama pull mistral
```

---

### 3. Instalar Python 3.10.x

- Baixe: [Python 3.10.11](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe)
- Marque a opção **Add Python to PATH** durante a instalação.
- Teste:
  ```bash
  python --version
  ```

---

### 4. Criar o ambiente virtual

```powershell
No Windows PowerShell:
python -m venv venv310
.\venv310\Scripts\Activate.ps1
```

---

### 5. Instalar dependências

```bash
pip install --upgrade pip
pip install streamlit
pip install llama-index
pip install chromadb
pip install sentence-transformers
pip install nest_asyncio
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

---

### 6. Criar os arquivos

- `app.py` ou `app-bd.py`: código principal da aplicação.
- `casos.txt`: casos simulados de triagem clínica.

---

## Executar o Aplicativo

```bash
No Windows PowerShell:
streamlit run app.py
```

Acesse em [http://localhost:8501](http://localhost:8501)

---

## Interface esperada

- Campo para digitar os sintomas
- Botão "Classificar e gerar conduta"
- Resultado com **classificação de risco**, **justificativa clínica** e **condutas iniciais**

---

## Visualizar dados com DB Browser

1. Baixe e instale: [https://sqlitebrowser.org](https://sqlitebrowser.org)
2. Abra o arquivo do banco no diretório `./chroma_db/`
3. Execute as consultas:

```sql
SELECT * FROM collections;
SELECT * FROM embeddings;
SELECT * FROM embeddings_queue;
```

---

## Exemplos de Casos Armazenados

```text
case_0: "Paciente do sexo masculino, 58 anos, com dor torácica intensa..."
case_7: "Paciente com falta de ar aos mínimos esforços, tosse produtiva..."
case_15: "Paciente com dispneia súbita, cianose e confusão..."
case_19: "Paciente com perda súbita de força no braço esquerdo..."
```

---

## Links úteis

- [LlamaIndex](https://docs.llamaindex.ai/en/stable/)
- [ChromaDB](https://docs.trychroma.com/)
- [Ollama](https://ollama.com/)
- [Streamlit](https://streamlit.io/)

---

