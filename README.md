"""
# Análise de Bilheteria de Filmes (2000–2024)

Este projeto é uma aplicação integrada com **Flask** e **Streamlit** para análise de dados de filmes com base em um dataset real de bilheteria, avaliação e número de votos.

## Objetivos

- Aplicar **orientação a objetos** para organização do código.
- Utilizar **funções de alta ordem** e **expressões lambda** (em expansão).
- Construir uma **API RESTful** com Flask.
- Criar uma **interface interativa** com Streamlit que consome a API.
- Visualizar dados com **Seaborn**, **Matplotlib** e **Pandas**.
- Executar **concorrência** entre Flask e Streamlit.

---

## Estrutura do Projeto

```
box_office_analysis/
├── analysis.py         # Classes de carregamento e análise de dados
├── api.py              # API Flask com endpoints RESTful
├── app.py              # Interface interativa com Streamlit
├── data/
│   └── enhanced_box_office_data(2000-2024)u.csv
└── README.md           # Este arquivo
```

---

## 🚀 Como Executar o Projeto

### 1. Instale as dependências

> Use um ambiente virtual, se preferir:

```bash
pip install flask streamlit pandas matplotlib seaborn
```

### 2. Inicie a API Flask

```bash
python api.py
```

> A API estará disponível em `http://localhost:5000`

### 3. Em outro terminal, inicie o Streamlit

```bash
streamlit run app.py
```

> O app abrirá no navegador automaticamente.

---

## 🔍 Funcionalidades

### 📊 Estatísticas Globais
- Média, mediana e desvio padrão da bilheteria, nota e número de votos.

### 🔍 Consulta por Rank
- Permite buscar um filme pelo **Rank** e exibir:
  - Título
  - Ano
  - Nota (rating)
  - Votos
  - Bilheteria mundial

---

## 📊 Dataset Utilizado

- [Movies Box Office Dataset (2000–2024)](https://www.kaggle.com/datasets/harshitshankhdhar/enhanced-movie-box-office-2000-2023)
- Contém informações como:
  - Título, ano, classificação, número de votos e bilheteria mundial
  - Mais de 500 registros

---

## 👨‍💼 Autor

Diogo da Silva Moraes Pinto Junior  
Trabalho de Pós Graduação Ciência de Dados e Big Data Analytics da disciplina Linguagem Python do professor Linguagem Python na Universidade Estácio de Sá
"""
