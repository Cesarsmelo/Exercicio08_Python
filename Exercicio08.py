#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram
#para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste seguindo o seguinte critério,
#baseado no salário atual:
#    salários até R$ 280,00 (incluindo) : aumento de 20%
#    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#    o salário antes do reajuste;
#    o percentual de aumento aplicado;
#    o valor do aumento;
#    o novo salário, após o aumento.

salario_in = 0
salario_atual = 0
valor_aumento = 0
aux = 0
#Entrada com o salário atual.
salario_in=float(input("Digite o salário atual R$"))

while True:
    percentual=100
    #Entrada com o valor do aumentado, em seguida já transforma em porcentagem.
    valor_aumento=float(input("Digite o valor do aumento R$"))
    percentual=(valor_aumento*100)/salario_in
    
    #Verifica se salário é R$280,00 e aumento de 20%.
    if salario_in <= 280 and percentual==20.00:
        salario_atual=salario_in+valor_aumento
        #Mostra o salário antes do reajuste.
        print(f"Salário antes do aumento R${salario_in}")
        #Mostra o percentual de aumento aplicado.
        print(f"Percentual aplicado foi de {percentual}%")
        #Mostra o valor do aumento.
        print(f"Aumento recebido foi de R${valor_aumento}")
        #Mostra o salário após o aumento.
        print(f"Salário atual após aumento R${salario_atual}")
        break
    else:
        print(f"Percentual de {percentual}% acima do permitido para o salário R${salario_in}.")