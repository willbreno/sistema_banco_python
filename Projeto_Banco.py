menu = (0)

extrato = []

saldo = (0)

deposito = (0)

sacar = (0)

saques = int(0)

def verificar_float(deposito):
    try:
        float(deposito) 
        return True
    except ValueError:
        try:
            int(deposito)
            return True
        except ValueError:
            return False

def verificar_float(sacar):
    try:
        float(sacar) 
        return True
    except ValueError:
        try:
            int(sacar)
            return True
        except ValueError:
            return False

def verificar_int(menu):
    try:
        int(menu) 
        return True
    except ValueError:
        return False

menu_texto = '''

######## Bem-Vindo ao Banco X-NET ########

Escolha uma opção para realias a operaçao. 

1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair  

'''

while True:

    print(menu_texto)

    menu = (input('Por gentileza entre com a operação que deseje realizar \n'))

    if verificar_int(menu):

        menu = int(menu)

        if menu == 1:

            print('\n Para prosseguir com o deposito por gentileza insira o valor desejado em R$: \n')

            deposito = (input())

            if verificar_float(deposito):
                deposito = float(deposito)
                if deposito > 0:

                    print(f'\n O deposito no valor de RS:{deposito: .2f} foi realizado com sucesso \n')

                    extrato.append(deposito)

                    saldo += deposito

                    print(f'O novo saldo é de RS:{saldo: .2f}\n')

                    input('\n Pressione qualquer tecla para continuar')

                else:
            
                    print('\n Valor não permitido, por gentileza refaça a operação \n')

                    input('\n Pressione qualquer tecla para continuar')

            else:
                print('Valor invalido por gentileza, tentar novamente !')
                input('\n Pressione qualquer tecla para continuar')

    
        elif menu == 2:

            print(' \n Insira o valor em R$ que deseja sacar \n')
        
            sacar = (input())

         
        
        
            if verificar_float(sacar):
                sacar = float(sacar)
                if sacar <= saldo:
            
                    if sacar <= 500 and saques < 3:

                        saldo -= sacar

                        saques += 1
                
                        ext_saque = - sacar

                        extrato.append(ext_saque)

                        print(f'\n Saque no valor de R$:{sacar: .2f} realizado com sucesso o novo saldo é R$:{saldo: .2f}\n')

                        input('\n Pressione qualquer tecla para continuar')

                    else:

                        if sacar > 500:

                            print('Valor de saque maior que o permitido, refaça o saque com limite de R$: 500,00 reais\n')

                            input('\n Pressione qualquer tecla para continuar')

                        else:
                            print('\n Quantidade de saques diarios exedida, por gentileza contate seu gerente.\n')

                            input('\n Pressione qualquer tecla para continuar')
                else:

                    print(f'A tentativa de saque no valor R$:{sacar: .2f} é maior que o saldo de R$:{saldo: .2f}')

                    input('\n Pressione qualquer tecla para continuar')

            else:
                print('Valor invalido, por gentileza refaça a operação')
                input('\n Pressione qualquer tecla para continuar')


        elif menu == 3:

            print('\n Esses são os últimos movimentos realizados em sua conta: \n')

            exibir_extrato = str("")

            for movimento in extrato:

                exibir_extrato += f'### R${movimento: .2f}\n'

            print(exibir_extrato)

            print(f'O saldo total é R$:  {saldo: .2f}')

            input('\n Pressione qualquer tecla para continuar')

        elif menu == 4:

            print("Obrigado por usar nosso banco. Até mais!\n")

            break


    else:
        print('Opçao invalida, tente novamente.')
        input('\n Pressione qualquer tecla para continuar')





    