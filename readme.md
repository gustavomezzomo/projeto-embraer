projeto desenvolvido no dia 16/02/2022 com o intuito de resolver um problema apresentado pela empresa EMBRAER

projeto consistem em desenvolver um quiz que tenha perguntas vinculadas a 3 respostas, sendo uma verdadeira e 2 falsas, salvas em um banco de dados relacional.
Ao iniciar o quiz o mesmo sorteia 5 perguntas aleatórias do banco de dados, colocando suas respostas de forma também aleatória

devido a falta de familiaridade com mysql o projeto passou um longo período travado na criação de um banco de dados, não sendo assim concluido dentro do prazo.

o desenvolvimento foi focado de forma que a pessoa, tendo instalado fastapi,uvicorn e pymysql possa rodar o projeto atraves do comando python -m uvicorn backend.main:app --reload,
podendo ver as funções criadas e seu funcionamento no localhost erguido em seu navegador/docs e fazer testes nas mesmas.

para a realização de testes é importante que o usuário tenha o mysql instalado e complete as linhas de "passwd" no arquivo main com as senhas do root da maquina em questão,
igualmente, é necessário criar a database e a tabela no mysql workbench, atraves do texto do arquivo tabela.me

apesar de não conseguir concluir o projeto consegui novos conhecimentos e assim melhorar na jornada no mundo da programação, agradeço a oportunidade de melhorar

![image](https://user-images.githubusercontent.com/77406018/154341705-3c417de4-3536-46a3-809f-3964f8008848.png)
