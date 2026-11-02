import os
import pandas as pd
import re

# função usada para ordenar os arquivos em ordem crescente (1,2,3...)
def extrair_numero(nome_arquivo):
  return int(nome_arquivo.split(".")[0])

# guardando dados do claude
# Ordena a lista usando a função acima como critério:
arquivos_claude = sorted(os.listdir("data/claude"), key=extrair_numero)
dados_claude = [] #os dados serão armazenados aqui para posteriormente irem p/ um dataframe

for nome in arquivos_claude:
    with open("data/claude/" + nome, "r", encoding="utf-8") as f:
        conteudo = f.read()
        ficha = {"arquivo": nome, "classe": "claude", "texto": conteudo}
        dados_claude.append(ficha)

df_claude = pd.DataFrame(dados_claude)

# guardando dados humanos
arquivos_human = sorted(os.listdir("data/human"), key=extrair_numero)
dados_human = [] #os dados serão armazenados aqui para posteriormente irem p/ um dataframe

for nome in arquivos_human:
    with open("data/human/" + nome, "r", encoding="utf-8") as f:
        conteudo = f.read()
        ficha = {"arquivo": nome, "classe": "human", "texto": conteudo}
        dados_human.append(ficha)

df_human = pd.DataFrame(dados_human)


#Pré processamento 
def tokenizar(texto):
  texto_min = texto.lower()
  return re.findall(r"\b[a-z]+\b", texto_min) #obs: descarta números

# (Isso vai criar uma coluna nova chamada 'tokens' na sua tabela)
df_claude["tokens"] = df_claude["texto"].apply(tokenizar)
df_human["tokens"] = df_human["texto"].apply(tokenizar)

print(df_claude.head(), "\n\n",df_human.head())
