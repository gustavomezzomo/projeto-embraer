import pymysql

# adicionando pergunta
# Abrir uma conexão com o banco de dados:
conexao = pymysql.connect(db='perguntas', user='root', passwd='')

# Cria um cursor:
cursor = conexao.cursor()

# Executa o comando:
cursor.execute("INSERT INTO pergunta (pergunta, resposta1, resposta2, resposta3) VALUES ('teste', 'Joao', 'Jose', 'Maria')")

# Efetua um commit no banco de dados.
# Por padrão, não é efetuado commit automaticamente. Você deve commitar para salvar
# suas alterações.
conexao.commit()

# Finaliza a conexão
conexao.close()



# atualizando resposta
conexao = pymysql.connect(db='perguntas', user='root', passwd='')

# Cria um cursor:
cursor = conexao.cursor()

# Executa o comando:
cursor.execute("UPDATE pergunta SET resposta1 = 'Joaquim' WHERE pergunta = 'teste'")

# Efetua um commit no banco de dados.
# Por padrão, não é efetuado commit automaticamente. Você deve commitar para salvar
# suas alterações.
conexao.commit()

# Finaliza a conexão
conexao.close()



# buscando respostas
conexao = pymysql.connect(db='perguntas', user='root', passwd='')

# Cria um cursor:
cursor = conexao.cursor()

# Executa o comando:
cursor.execute("SELECT resposta1 FROM pergunta WHERE pergunta = 'teste'")

# Recupera o resultado:
resultado = cursor.fetchall()

# Mostra o resultado:
print('resposta 1: ')

for linha in resultado :
    print(linha)

# Finaliza a conexão
conexao.close()


# deletando dados
conexao = pymysql.connect(db='perguntas', user='root', passwd='')

# Cria um cursor:
cursor = conexao.cursor()

# Executa o comando:
cursor.execute("DELETE FROM pergunta WHERE pergunta = 'teste'")

# Efetua um commit no banco de dados.
# Por padrão, não é efetuado commit automaticamente. Você deve commitar para salvar
# suas alterações.
conexao.commit()

# Finaliza a conexão
conexao.close()