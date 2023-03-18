# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def fibs_check_exists(v: int):
    fibs = []
    e = False

    for i in range(0, v+1):
        fibs.append(i) if len(fibs) < 2 else fibs.append(fibs[i-2]+fibs[i-1])

        if v in fibs: 
            e = True
            break
    
    return f"O valor {v} foi encontrado no i = {len(fibs)-1}." if e else f"O valor {v} nao foi encontrado."

if __name__ == "__main__":
    v = int(input("Informe o valor a ser checado: "))

    print(fibs_check_exists(v))