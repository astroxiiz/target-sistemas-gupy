#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json


if __name__ == "__main__":

    with open("faturamento.json") as f:
        fat_mensal = json.load(f)
        f.close()

    med = sum([x.get("valor") for x in fat_mensal])/len(fat_mensal)

    # Com os built-ins do Python

    print("Menor faturamento:", min([x.get("valor") for x in fat_mensal]))
    print("Maior faturamento:", max([x.get("valor") for x in fat_mensal]))
    print("Dias faturamento > media:", sum([1 if x.get("valor") > med else 0 for x in fat_mensal]))

    # --------------------------
    print("\n")
    # --------------------------

    # Sem os built-ins do Python

    mi = 0
    ma = 0
    dmm = 0

    for i in range(0, len(fat_mensal)):
        mi = mi if fat_mensal[i].get("valor") >= mi else fat_mensal[i].get("valor")
        ma = ma if fat_mensal[i].get("valor") <= ma else fat_mensal[i].get("valor")
        if(fat_mensal[i].get("valor") > med): dmm += 1

    print("Menor faturamento:", mi)
    print("Maior faturamento:", ma)
    print("Dias faturamento > media:", dmm)