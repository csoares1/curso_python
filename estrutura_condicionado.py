# saldo = 2000.0

# saque = float(input("Informe o valor do saque: "))

# if saldo >= saque:
#     print("Realizado saque!")
# else:
# # if saldo < saque:
#     print("Saldo insuficiente!")    

# opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

# if opcao == 1:
#     saque=float(input("Informe a quantia para saque: "))
#     saldo = 2000.0
#     if saldo >= saque:
#        print("Realizado saque!")
#     else:
#     # if saldo < saque:
#         print("Saldo insuficiente!")   
# elif opcao == 2:
#     print("Exibindo extrato....")
# else:
#     print("Opção inválida")

# MAIOR_IDADE = 18

# idade = int(input("Informe sua idade: "))

# if idade >= MAIOR_IDADE:
#     print("Maior de idade, pode tirar CNH")
# else:
#     print("Ainda não pode tirar CNH")
# conta_normal = False
# conta_universitaria = False
# saldo =2000
# saque = 1500
# cheque_especial = 450

# if conta_normal:
#     if saldo >= saque:
#         print("Saque realizado com sucesso!")
#     elif saque <= (saldo + cheque_especial):
#         print("Saque realizado com cheque especial")
#     else:
#         print("Não foi possível realizar o saque")
# elif conta_universitaria:
#     if saldo >= saque:
#         print("Saque realizado com sucesso!")
#     else:
#         print("Saldo insuficiente")
# else:
#     print("Sistem não reconheceu tipo de conta")
saque = 1000
saldo = 2000
status = "Sucesso" if saldo >= saque else "falha"
print(f"{status} ao realizar o saque")
    