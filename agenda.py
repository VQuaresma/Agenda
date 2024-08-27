import sqlite3
from sqlite3 import Error
import os

res =0

def ConexaoBanco():
    caminho = 'C:\\Users\\V\\Desktop\\projetos\\banco\\agenda.db'
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con
vcon = ConexaoBanco()

def menu():
    global res
    os.system("cls")
    print("""1 - Inserir registro 
2 - Deletar registro 
3 - Consultar por ID
4 - Consultar por nome
5 - Mostrar todos cadastros
 - Update de cadastro
6 - Sair """)
    res = int(input("Digite uma das opções acima: "))
    return res

def saida():
    
    res = int(input("""6- Sair
7 - Menu"""))
    return res

def inserir(conexao):

    nome = input('Digite o nome da pessoa: ')
    telefone = input('Digite o telefone da pessoa: ')
    email = input('Digite o email da pessoa: ')

    InserirSql=f"""INSERT INTO tb_contatos (
            T_NOMECONTATO, 
            T_TELEFONECONTATO, 
            T_EMAILCONTATO) 
            VALUES('{nome}', '{telefone}', '{email}')"""


    try:
        c=conexao.cursor()
        c.execute(InserirSql)
        conexao.commit()
        print("Registro inserido")
        
    except Error as ex:
        print(ex)

def DeletarDados(conexao):

    registro= int(input("Digite o número do id que deseja deletar: "))
    DeletarSql = f'DELETE FROM tb_contatos WHERE N_IDCONTATO={registro}'
    
    try:
        c=conexao.cursor()
        c.execute(DeletarSql)
        conexao.commit()
        print("Registro deletado")
    except Error as ex:
        print(ex)

def ConsultarId(conexao):

    InputId = int(input('Digite o numero do Id que desejas consultar: '))
    ConsultaIdSql = f'SELECT * FROM tb_contatos WHERE N_IDCONTATO ={InputId} '

    c=conexao.cursor()
    c.execute(ConsultaIdSql)
    resultado=c.fetchall()
    return resultado

def ConsultarNome(conexao):

    InputNome = str(input('Digite o nome que desejas consultar: '))
    ConsultaNomeSql = f"""SELECT * FROM tb_contatos WHERE T_NOMECONTATO ='{InputNome}' """

    c=conexao.cursor()
    c.execute(ConsultaNomeSql)
    resultado=c.fetchall()
    return resultado

def MostrarTodos(conexao):
    MostrarSql ='SELECT * FROM tb_contatos'
    try:
        c=conexao.cursor()
        c.execute(MostrarSql)

        cadastros =  c.fetchall()
        c.close()
        return cadastros
    except Error as ex:
        print(ex)



while res!=6:
    menu()
    if res==1:
        os.system("cls")
        inserir(vcon)
        res = saida()
    elif res==2:
        os.system("cls")
        DeletarDados(vcon)
        res = saida()
    elif res==3:
        os.system("cls")
        print(ConsultarId(vcon))
        res = saida()
    elif res==4:
        os.system("cls")
        print(ConsultarNome(vcon))
        res = saida()
    elif res==5:
        os.system("cls")
        print(MostrarTodos(vcon))
        res = saida()
    elif res==6:
        break
os.system("cls")
vcon.close()
print("progama finalizado")
