from fastapi import FastAPI
from pydantic import BaseModel
import pymysql

app = FastAPI()

# Rota Raiz
@app.get("/")
def raiz():
    return

# Cria Model
class Usuario(BaseModel):
    id: int
    nome: str
    pontuacao: int

class Pergunta(BaseModel):
    id: int
    pergunta: str
    resposta1: str
    resposta2: str
    resposta3: str

# Base de Dados

perguntas = pymysql.connect(db='perguntas', user='root', passwd='')

# Cria um cursor:
cursor = perguntas.cursor()

# Executa o comando:
cursor.execute("SELECT resposta1 FROM pergunta WHERE pergunta = 'teste'")

# Recupera o resultado:
resultado = cursor.fetchall()

# Mostra o resultado:
print('respostas: ')

for linha in resultado :
    print(linha)

# Finaliza a conexão
perguntas.close()


dados = [
    Usuario(id=1, email="teste@teste.com", nome="teste", pontuacao="3"),
    Usuario(id=2, email="teste1@teste.com", nome="teste1", pontuacao="4")

]

# Rota Get All
@app.get("/usuarios")
def get_todos_os_usuarios():
    return dados

@app.get("/perguntas")
def get_todas_as_perguntas():
    conexao = pymysql.connect(db='perguntas', user='root', passwd='')

    # Cria um cursor:
    cursor = conexao.cursor()

    # Executa o comando:
    cursor.execute("SELECT * FROM pergunta WHERE resposta1, resposta2, resposta3 NOT NULL")

    # Recupera o resultado:
    resultado = cursor.fetchall()

    # Mostra o resultado:
    print('pergunta: ')

    for linha in resultado :
        print(linha)

    # Finaliza a conexão
    conexao.close()

# Rota Get ID
@app.get("/usuarios/{id_usuario}")
def get_usuario_usando_id(id_usuario: int):
    for usuario in dados:
        if(usuario.id == id_usuario):
            return usuario
    return {"Status": 404, "Mensagem": "Usuário não encontrado"}

# Rota Insere
@app.post("/usuarios")
def insere_usuario(usuario: Usuario):
    # Regras De Negócio
    dados.append(usuario)
    return usuario

# inserir perguntas
@app.post("/perguntas")
def insere_pergunta(input: Pergunta):
    # Regras De Negócio
    # Abrir uma conexão com o banco de dados:
    conexao = pymysql.connect(db='perguntas', user='root', passwd='')

    # Cria um cursor:
    cursor = conexao.cursor()

    # Executa o comando:
    cursor.execute("INSERT INTO pergunta (pergunta) VALUES"(input))

    # Efetua um commit no banco de dados.
    # Por padrão, não é efetuado commit automaticamente. Você deve commitar para salvar
    # suas alterações.
    conexao.commit()

    # Finaliza a conexão
    conexao.close()


#inserir resposta1
@app.post("/perguntas")
def insere_resposta1(input: Pergunta):
    # Regras De Negócio
    # Abrir uma conexão com o banco de dados:
    conexao = pymysql.connect(db='perguntas', user='root', passwd='')

    # Cria um cursor:
    cursor = conexao.cursor()

    # Executa o comando:
    cursor.execute("INSERT INTO pergunta (resposta1) VALUES"(input))

    # Efetua um commit no banco de dados.
    # Por padrão, não é efetuado commit automaticamente. Você deve commitar para salvar
    # suas alterações.
    conexao.commit()

    # Finaliza a conexão
    conexao.close()


#inserir resposta2
@app.post("/perguntas")
def insere_resposta2(input: Pergunta):
    # Regras De Negócio
    # Abrir uma conexão com o banco de dados:
    conexao = pymysql.connect(db='perguntas', user='root', passwd='')

    # Cria um cursor:
    cursor = conexao.cursor()

    # Executa o comando:
    cursor.execute("INSERT INTO pergunta (resposta2) VALUES"(input))

    # Efetua um commit no banco de dados.
    # Por padrão, não é efetuado commit automaticamente. Você deve commitar para salvar
    # suas alterações.
    conexao.commit()

    # Finaliza a conexão
    conexao.close()


#inserir resposta3
@app.post("/perguntas")
def insere_resposta3(input: Pergunta):
    # Regras De Negócio
    # Abrir uma conexão com o banco de dados:
    conexao = pymysql.connect(db='perguntas', user='root', passwd='')

    # Cria um cursor:
    cursor = conexao.cursor()

    # Executa o comando:
    cursor.execute("INSERT INTO pergunta (resposta3) VALUES"(input))

    # Efetua um commit no banco de dados.
    # Por padrão, não é efetuado commit automaticamente. Você deve commitar para salvar
    # suas alterações.
    conexao.commit()

    # Finaliza a conexão
    conexao.close()