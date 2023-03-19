# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

#SP – R$67.836,43
#RJ – R$36.678,66
#MG – R$29.229,88
#ES – R$27.165,48
#Outros – R$19.849,53

#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.



if __name__ == "__main__":
    fat_mensal = [{"state": "SP", "value": 67836.43},
                  {"state": "RJ", "value": 36678.66},
                  {"state": "MG", "value": 29229.88},
                  {"state": "ES", "value": 27165.48},
                  {"state": "OUTROS", "value": 19849.53}]
    
    for i in range(len(fat_mensal)):
        fat_mensal[i]["perc"] = fat_mensal[i].get("value")*100/sum([v.get("value") for v in fat_mensal])

    [print(f'{x.get("state")} : {x.get("perc"):.2f}%') for x in fat_mensal]