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

for i in range(0, 50):
    print(gerar_senha(random.randint(5, 10)))

    
    