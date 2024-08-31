menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques= 3
 
while True:
    
    opcao = input (menu)

    if opcao =="d":
      print ("Deposito")
      valor= float (input ("Informe o valor que será depositado: "))

      if valor >0:
        saldo += valor
        extrato == f"Depósito;  R$ {valor:.2f}\n"
      else:
        print ("Operação falhou! O valor informado é inválido.")
      

    


    
    elif opcao == "s":
      print ("Saque")
      valor= float (input ("Informe o valor do saque: "))
     


      excedeu_saldo = valor > saldo
      excedeu_limite = valor > limite
      excedeu_saques = numero_saques >= limite_saques
      
      if excedeu_saldo:
        print ("Operação falhou! Você não tem saldo suficiente.")
      elif excedeu_limite:
        print ("Operação falhou! O valor do saque excede o limite.")
      elif excedeu_saques:
        print ("Operação falhou! Número máximo de saques excedido.")
      elif valor >0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
      elif valor <=0:
        print ("Operação Falhou! Valor inserido menor ou igual a 0")
     
    
    
    elif opcao == "e":
      print ("\n=========== Extrato ==========")
      print ("Não foram feitas movimentações." if not extrato else extrato)
      print (f"\n Saldo: R$ {saldo:.2f}")
      print ("======================================")

   
   
    elif opcao =="q":
      break
   
    else:
      print ("operação Inválida, por favor selecione novamente a operacao desejada")