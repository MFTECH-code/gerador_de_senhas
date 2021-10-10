import os.path
import sys
import random

def gerar_senha(tamanho_senha):
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "1234567890"
    simbolos = "!@#$%&*"

    caracteres = [letras, numeros, simbolos]
    
    senha_list = []

    for i in range(0, tamanho_senha):
        x = random.randint(0, 2)
        y = random.randint(0, len(caracteres[x]) - 1)

        senha_list.append(caracteres[x][y])
    

    senha_str = ""
    
    for i in senha_list:
        senha_str += i

    return senha_str


def salvar_senha(senha):
    file_name = "senhas.txt"
    finalidade = input("Qual é a finalidade dessa senha: ")

    if not os.path.exists(file_name):
        print(f"O arquivo {file_name} não existe...")
        print("Crie o arquivo na mesma pasta que o programa .py")
        sys.exit()

    file_open = open(file_name, "a")
    file_open.write(senha + " -> " + finalidade + "\n")
    file_open.close()
    print("Senha salva com sucesso!")


salvar_senha(gerar_senha(random.randint(8, 12)))

    
    