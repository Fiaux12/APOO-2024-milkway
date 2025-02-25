import pandas as pd
import json
import os

SETTINGS_DATA_FILE = "../assets/settings/settings.json"
USER_DATA_FILE = "../assets/settings/usuarios.json"

# Função para carregar os dados de um arquivo JSON em um DataFrame
def ler_configuracoes():
    if os.path.exists(SETTINGS_DATA_FILE):
        with open(SETTINGS_DATA_FILE, "r") as arquivo:
            configuracoes = json.load(arquivo)
        return pd.DataFrame(configuracoes)
    

# Função para carregar os dados de um arquivo JSON em um DataFrame
def carregar_usuarios():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as arquivo:
            dados = json.load(arquivo)
        return pd.DataFrame(dados["Usuarios"])
    return pd.DataFrame(columns=["nome", "pontos", "save_point"])

# Função para salvar os dados do DataFrame no arquivo JSON
def salvar_usuarios(df):
    usuarios_json = {"Usuarios": df.to_dict(orient="records")}
    with open(USER_DATA_FILE, "w") as arquivo:
        json.dump(usuarios_json, arquivo, indent=4)

# Função para adicionar um novo usuário ao DataFrame
def adicionar_usuario(nome, pontos, save_point):
    df = carregar_usuarios()
    novo_usuario = pd.DataFrame([
        {"nome": nome,
        "pontos": pontos,
        "save_point": save_point
        }
    ])

    df = pd.concat([df, novo_usuario], ignore_index=True)
    salvar_usuarios(df)

# Função para atualizar os pontos 
def atualizar_pontos(nome_usuario, novos_pontos):
    df = carregar_usuarios()
    if nome_usuario.nome in df["nome"].values:
        df.loc[df["nome"] == nome_usuario.nome , "pontos"] = novos_pontos

    salvar_usuarios(df)

