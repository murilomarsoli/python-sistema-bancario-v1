# DECLARAÇÃO DAS CONSTANTES
LIMITE_DIARIO_QNTD_SAQUE = 3
LIMITE_DINHEIRO_SAQUE = 500.00

# DECLARAÇÃO DAS VARIÁVEIS
deposito = 0.0
saque = 0.0
depositado = 0.0
sacado = 0.0
saldo = 0.0
qntd_saques = 0
extrato = ''

# ENQUANTO O PROGRAMA NÃO FOR INTERROMPIDO
while True:
  # MENU já com um REQUERIMENTO DE ENTRADA DE DADOS
  opcao = input("""
********** SISTEMA BANCÁRIO V1 **********
  A - DEPÓSITO                           
  B - SAQUE                               
  C - EXTRATO
  Q - FINALIZAR PROGRAMA                  
*****************************************
Escolha uma opção: """)
  
  # OPÇÃO DEPÓSITO
  if opcao == 'A' or opcao == 'a':
    # REQUERIMENTO DE ENTRADA DE UM DADO DO TIPO FLOAT
    deposito = float(input("\nInsira o valor a depositar na conta: "))

    if deposito > 0:  # se o valor do depósito for maior que zero
      depositado += deposito  # total depositado será incrementado com valor do depósito atual
      saldo += deposito   # saldo da conta será incrementado com o depósito atual
      extrato += f"Depósito: R${deposito:.2f}\n"
      print("Valor depositado com sucesso!")
    else:
      print("Só serão aceitos valores positivos, maiores que zero!\nTente novamente.")  # caso o usuário insira um valor negativo ou nulo

  # OPÇÃO SAQUE
  elif opcao == 'B' or opcao == 'b':
    saque = float(input("\nInsira o valor a sacar da conta: "))
    
    if qntd_saques < LIMITE_DIARIO_QNTD_SAQUE:  # se a quantidade de saques diários não tiver ultrapassado o limite
      
      if saque <= LIMITE_DINHEIRO_SAQUE:  # se o valor do saque estiver dentro do valor limite permitido
        if saldo >= saque:  # se o saldo total da conta for maior ou igual ao saque requerido
          sacado += saque   # valor total sacado da conta será incrementado com o valor do saque atual requerido
          saldo -= saque    # saldo da conta será decrementado com o valor do saque atual requerido
          extrato += f"Saque: R${saque:.2f}\n"
          qntd_saques += 1  # a cada operação de saque realizado, a var "qntd_saques" será incrementada em 1 (controlar o limite de saques)
          print("Saque realizado com sucesso!")
        else:
          print("Saldo insuficiente para a realização do saque.\n")
      else:
        print(f"Saque NÃO realizado!\nO valor ultrapassa o limite permitido para cada saque, que é de R${LIMITE_DINHEIRO_SAQUE:.2f}.\nTente novamente.")

    else:
      print(f"\nSaque NÃO realizado!\nVocê já alcançou o limite de saques diários permitidos, que são {LIMITE_DIARIO_QNTD_SAQUE}.\nTente novamente amanhã.")  
      
  # OPÇÃO EXTRATO
  elif opcao == 'C' or opcao == 'c':
    # caso a var "extrato" estiver vazia, mostrará a string "Ainda não foram re..." na tela. Caso contrário, se a var "extrato" conter algum conteúdo, o mostrará na tela
    print(f"""
-----------------------------
EXTRATO DA CONTA BANCÁRIA
-----------------------------
HISTÓRICO
-----------------------------""")
    print(f"Ainda não foram realizadas movimentações na conta." if not extrato else extrato)
    print(f"""-----------------------------
INFORMAÇÕES GERAIS DA CONTA
-----------------------------
Depositado = R${depositado:.2f}
Sacado = R${sacado:.2f}
Saldo disponível = R${saldo:.2f}
""")

  # OPÇÃO FINALIZAR PROGRAMA
  elif opcao == 'Q' or opcao == 'q':
    print("\nObrigado por utilizar nosso SISTEMA BANCÁRIO V1!\n")
    break
  else:
    print("\nDigite uma opção válida.\n")