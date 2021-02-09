# Por trás
funcionario = []
desconto_inss = 0
desconto_irrf = 0
def request_name_salario():
    request_name = str(input('Digite o nome do funcionário: '))
    request_salario = float(input('Digite o salário bruto: '))
    requests = []
    requests.append(request_name)
    requests.append(request_salario)
    requests.append(0)
    requests.append(0)
    funcionario.append(requests[:])
    return funcionario

def calculo_salario_inss():
    #Descontos 'fixos' dependendo do salario
    desconto_minimo = 78.38
    desconto_alicota_2 = 94.01
    desconto_alicota_3 = 125.38

    #Procurando o funcionario desejado
    for indice, detalhes_fun in enumerate(funcionario):
        if indice == indeceParaCalculo:
            #fazendo o calculo
            if detalhes_fun[1] <= 1045.00:
                funcionario[indice][2] = funcionario[indice][1] - desconto_minimo


            elif  detalhes_fun[1] <= 2089.60 :
                desconto2 = (detalhes_fun[1] - 1045.00) * 0.09

                funcionario[indice][2] = round(funcionario[indice][1] - desconto2 - desconto_minimo,2)

            elif detalhes_fun[1] <= 3134.4:
                desconto3 = (detalhes_fun[1] - 2089.61) * 0.12

                funcionario[indice][2] = round(funcionario[indice][1] - desconto_alicota_2 -desconto3 - desconto_minimo, 2)

            elif detalhes_fun[1] <= 6101.06:
                desconto4 = (detalhes_fun[1] - 3134.4) * 0.14

                funcionario[indice][2] = round(funcionario[indice][1] -desconto4 - desconto_minimo - desconto_alicota_2 - desconto_alicota_3, 2)
            return funcionario


def calculo_salario_irff():
    #separando quem vai ser o funcionario
    for indice, detalhes_fun in enumerate(funcionario):
        if indice == indeceParaCalculo:
            #calculo
            if detalhes_fun[1] <= 1903.98:
                break
            elif detalhes_fun[2] <= 2826.65:
                funcionario[indice][3] = round((funcionario[indice][2] * 0.075) - 142.80, 2)

            elif detalhes_fun[2] <= 3751.05:
                funcionario[indice][3] = round((funcionario[indice][2] * 0.15) - 354.80, 2)

            elif detalhes_fun[2] <= 4664.68:
                funcionario[indice][3] = round((funcionario[indice][2] * 0.225) - 636.13, 2)

            elif detalhes_fun[2] > 4664.69:
                funcionario[indice][3] = round((funcionario[indice][2] * 0.275) - 869.36, 2)
            return funcionario

# Primeira Interfaçe

while True:
    pergunta_inicial = int(input("1) Cadastras funcionário novo \n2) Imprir Contracheque\n3) Sair"))


    # Cadastro Funcionario
    if pergunta_inicial == 1:
        request_name_salario()
        print("Anotado")

    # Imprir contra cheque
    if pergunta_inicial == 2:
        #Imprime os indice dos funcionarios
        for ind, func in enumerate(funcionario):
            print(f'Digite: {ind} para calcular os desconto do funcionario: {func[0]}')
        #Indixe desejo
        indeceParaCalculo = int(input(''))

        # Calculo de inss
        calculo_salario_inss()
        calculo_salario_irff()
        salario_liso = funcionario[indeceParaCalculo][2] - funcionario[indeceParaCalculo][3]
        print(f'O funcionario de nome: {funcionario[indeceParaCalculo][0]}\n'
              f'Recebe Bruto: {funcionario[indeceParaCalculo][1]}\n'
              f'Seu desconto de INSS é: {funcionario[indeceParaCalculo][2]}\n'
              f'Seu desconto de IRRF é: {funcionario[indeceParaCalculo][3]}\n'
              f'E seu sálario líquido é: {salario_liso}\n')


    if pergunta_inicial == 3:
        break
