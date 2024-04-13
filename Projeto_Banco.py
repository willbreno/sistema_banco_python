menu = int(0)

extrato = []

saldo = float(0)

deposito = float(0)

sacar = float(0)

i = int(0)

saques = int(0)

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

    menu = int(input('Por gentileza entre com a operação que deseje realizar \n'))

    if menu == 1:

        print('\n Para prosseguir com o deposito por gentileza insira o valor desejado em R$: \n')

        deposito = float(input())

        if deposito > 0:

            print(f'\n O deposito no valor de RS:{deposito: .2f} foi realizado com sucesso \n')

            extrato.append(deposito)

            saldo += deposito

            print(f'O novo saldo é de RS:{saldo: .2f}\n')

            input('\n Pressione qualquer tecla para continuar')

        else:
            
            print('\n Valor não permitido, por gentileza refaça a operação \n')

            input('\n Pressione qualquer tecla para continuar')
    
    elif menu ==2:

        print(' \n Insira o valor em R$ que deseja sacar \n')
        
        input('\n Pressione qualquer tecla para continuar')
        
        if sacar <= saldo:
            
            if sacar <= 500 and saques < 3:

                saldo -= sacar

                saques +=1
                
                ext_saque = - sacar

                extrato.append(ext_saque)

                print(f'\n Saque no valor de R$:{sacar: .2f} realizado com sucesso o novo saldo é R$:{saldo: .2f}\n')

                input('\n Pressione qualquer tecla para continuar')


            
            else:

                if sacar > 500:

                    print('Valor de saque maior do que o permitido, refaça o saque com limite máximo de R$: 500,00 reais\n')

                    input('\n Pressione qualquer tecla para continuar')

                else:
                    print('\n Quantidade de saques diarios exedida, por gentileza contate seu gerente.\n')

                    input('\n Pressione qualquer tecla para continuar')
        else:

            print(f'A tentativa de saque no valor R$:{sacar: .2f} é maior que o saldo de R$:{saldo: .2f}')

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

        break

        print("Obrigado por usar nosso banco. Até mais!\n")


    