def validador_senha ():
    while True:
        print("Uma senha válida deve ter 8 caracteres, pelo menos 1 letra maiúscula, 1 minúscula e 1 número.")
        erros = captura_erros(senha)
        senha = input("Digite sua senha:\n")
        if erros > 0:
            for erro in erros:
                print(erro)
        else:
            print("Senha criada!")
            break

def captura_erros(senha):
    erros = []
    if len(senha) < 8:
        erros.append("Sua senha deve ter no mínimo 8 caracteres.")
    if not any(c.isupper() for c in senha):
        erros.apend("É necessário ter pelo menos um caracter maiusculo.")
    if not any(c.islower() for c in senha):
        erros.apend("É necessário ter pelo menos um caracter minúsculo.")
    if not any(c.isdigit() for c in senha):
        erros.apend("É necessário ter pelo menos um caracter numérico.")
    return erros

validador_senha()