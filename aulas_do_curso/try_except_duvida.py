# qual a diferença de escrever um trecho de código no finally e um trecho na mesma linha do try except sem indentar (ou seja fora deles)?

# --finally:--

# Sempre roda, independente de ter dado erro ou não no try/except.
# Até se você meter um return dentro do try ou except, o finally ainda roda antes de sair.

# --código fora (sem indentar, após o bloco):--

# Só roda se o fluxo chegar ali.

# Ou seja: se o try/except tratou e terminou de boa, ele roda.

# Mas se tiver um return, raise ou crash dentro do bloco → esse trecho externo nunca é executado.

# --Regra de bolso:--

# Se é limpeza obrigatória → use finally.

# Se é só sequência de lógica → põe fora do bloco.

def f():
    try:
        x = 1 / 0
    except ZeroDivisionError:
        print("erro tratado")
        return
    finally:
        print("finally ainda rodou")

    print("fora do bloco") # isso nunca vai rodar porque ele caiu no except com return e só o finally roda independente de qualquer coisa
    # o return para a função e sai dela não retornando nada dela alem de suas ações como o print

f()
