import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



with st.sidebar.header("🔍 Filtros"):
    resp_genero = requests.get('http://localhost:5000/api/categories')
    genres = resp_genero.json()

    year_max = st.sidebar.slider("Ano Máximo", 2000, 2024, 2024)
    genre = st.sidebar.multiselect("Selecione os Generos:",genres)
    min_rating = st.sidebar.slider("Nota mínima", 0.0, 10.0, 0.0)
    max_rating = st.sidebar.slider("Nota máxima", 0.0, 10.0, 10.0)

params = {}


if year_max <= 2024:
    params['year_max'] = year_max
if genre:
    params['genre'] = genre
if min_rating > 0.0:
    params['min_rating'] = min_rating
if max_rating < 10.0:
    params['max_rating'] = max_rating

resp = requests.get("http://localhost:5000/api/statistics")
url = 'http://127.0.0.1:5000/api/data'
response = requests.get(url, params=params)

data_json = response.json()

df = pd.DataFrame(data_json)

order = ['Rank', 'Release Group', 'Year', '$Worldwide', 'Rating', 'Rating_Num', 'Vote_Count']

st.title(f"Análise de Bilheteria de Filmes 2000–{year_max}")


print(df.head(5))

st.header("Tabela de dados:")
st.dataframe(df[order], use_container_width=True, hide_index=True)

st.header("📊 Estatísticas Globais")

st.subheader("Bilheteria Mundial por Ano")
fig1, ax1 = plt.subplots()
sns.barplot(data=df, x="Year", y="$Worldwide", errorbar=None, palette="coolwarm", ax=ax1)
ax1.set_title("Bilheteria Mundial por Ano")
ax1.set_xlabel("Ano")
ax1.set_ylabel("Bilheteria (US$)")
plt.xticks(rotation=45)
st.pyplot(fig1)

st.subheader("Distribuição de Bilheteria por Localidade")
fig3, ax3 = plt.subplots()
plt.bar(df['Year'],df['$Foreign'], label='Estrangeira')
plt.bar(df['Year'], df['$Domestic'], label='Nacional')
plt.ylabel('Valor')
plt.title('Distribuição de Bilheteria por Localidade')
plt.legend()
st.pyplot(fig3)

# Histograma de Ratings
st.subheader("Distribuição dos Ratings")
fig2, ax2 = plt.subplots()
sns.histplot(df["Rating_Num"], bins=20, kde=True, ax=ax2)
ax2.set_title("Distribuição das Avaliações")
ax2.set_xlabel("Nota")
ax2.set_ylabel("Frequência")
ax2.set_xlim(0, 10)
st.pyplot(fig2)


# Consulta por ID
st.header("🔍 Buscar Filme por Rank")
rank = st.number_input("Digite o Rank do Filme", min_value=1, max_value=500, step=1)
if st.button("Buscar"):
    resp = requests.get(f"http://localhost:5000/api/record/{rank}")
    if resp.status_code == 200:
        filme = resp.json()
        if "erro" in filme:
            st.warning("Filme não encontrado.")
        else:
            st.write(f"### {filme['Release Group']} ({filme['Year']})")
            st.write(f"**Rating:** {filme['Rating']} | **Votos:** {filme['Vote_Count']} | **Bilheteria:** ${filme['$Worldwide']}")
    else:
        st.error("Erro ao buscar filme.")