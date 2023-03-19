#5) Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

if __name__ == "__main__":
    # v = str(input("Digite o texto a ser invertido: "))
    v = "Uma string :)"

    # ----------------
    print(v[::-1])
    # ----------------

    vr = ""
    for i in range(len(v))[::-1]: # for (int i = v.Length - 1; i >= 0; i--) { vr = vr + v[i]; }
        vr = vr + v[i]

    print(vr)
