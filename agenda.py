import sqlite3
from sqlite3 import Error
import os
from time import sleep

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
6 - Update de cadastro
7 - Sair """)
    res = int(input("Digite uma das opções acima: "))
    return res

def saida():
    
    res = int(input("""7 - Sair
8 - Menu
"""))
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
    finally:
        c.close()

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
    finally:
        c.close()

def ConsultarId(conexao):
    try:
        InputId = int(input('Digite o numero do Id que desejas consultar: '))
        ConsultaIdSql = f'SELECT * FROM tb_contatos WHERE N_IDCONTATO ={InputId} '

        c=conexao.cursor()
        c.execute(ConsultaIdSql)
        resultado=c.fetchall()
        return resultado
    except Error as ex:
        print(ex)
    finally:
        c.close()


def ConsultarNome(conexao):
    try:
        InputNome = str(input('Digite o nome que desejas consultar: '))
        ConsultaNomeSql = f"""SELECT * FROM tb_contatos WHERE T_NOMECONTATO ='{InputNome}' """

        c=conexao.cursor()
        c.execute(ConsultaNomeSql)
        resultado=c.fetchall()
        return resultado
    except Error as ex:
        print(ex)
    finally:
        c.close()


def MostrarTodos(conexao):
    MostrarSql ='SELECT * FROM tb_contatos'
    try:
        c=conexao.cursor()
        c.execute(MostrarSql)

        cadastros =  c.fetchall()
        c.close()
        pos = 1
        for cadastro in cadastros:
            print(f"Índice: {pos}, ID: {cadastro[0]}, Nome: {cadastro[1]}, Data: {cadastro[2]}, E-mail: {cadastro[3]}")
            pos+=1

    except Error as ex:
        print(ex)
    finally:
        c.close()

def AtualizarDados(conexao):
    MostrarTodos(vcon)
    try:
        c = conexao.cursor()

        sel = int(input("Selecione o id do cadastro que você deseja alterar: "))
        c.execute(f'SELECT * FROM tb_contatos WHERE N_IDCONTATO ={sel} ')

        resultado = c.fetchall()

        os.system("cls")

        print(f"ID: {resultado[0][0]}, Nome: {resultado[0][1]}, Data: {resultado[0][2]}, E-mail: {resultado[0][3]}")
        opcoes = {
        1: "N_IDCONTATO",
        2: "T_NOMECONTATO",
        3: "T_TELEFONECONTATO",
        4: "T_EMAILCONTATO"
    }
        UpdateRes = int(input("""Selecione o conteudo que deseja alterar: 
    1- ID
    2- Nome
    3- Telefone
    4- Email
    """))
        os.system("cls")
        
        
        DadoNovo = input("Digite o novo valor que ira ser atribuido: ")

        AtualizarSql=F"UPDATE tb_contatos SET {opcoes[UpdateRes]} = '{DadoNovo}' WHERE N_IDCONTATO ={sel}"
        c.execute(AtualizarSql)
        conexao.commit()
        os.system("cls")

        
        cont = 1
        while cont!=4:
            print('.'*cont)
            cont+=1
            sleep(0.5)
            os.system("cls")
        print("Cadastro atualizado")
        sleep(2)
        
    except Error as ex:
        print(ex)
    finally:
        c.close()
        


while res!=7:
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
        MostrarTodos(vcon)
        res = saida()
    elif res==6:
        AtualizarDados(vcon)
    elif res==7:
        break
    else:
        print("Opção inválida, tente novamente! ")
os.system("cls")
vcon.close()
print("progama finalizado")
