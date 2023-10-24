import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "2525",
    datebase = "bd_youtube",
)

cursor = conexao.cursor()

#CRUD
comando = "INSERT INTO Vendas (nome_produto, valor) VALUES (nome, valor)" #insere informação
cursor.execute(comando)
conexao.comid() #Edita o banco de dados
resultado = cursor.fetchtall() #Ler o banco de dados

cursor.close()
conexao.close()

