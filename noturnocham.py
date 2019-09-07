import socket
import sys
alpha = print("vamos registrar uma conta temporaria para sua segurança, (só vale por essa sessão,depois terá que registrar novamente.)")
A = input("digite seu usuario : ")
B = input("Digite sua senha : ")
C = print("Agora vamos Logar")
D = input("digite seu usuário: ")
E = input("digite sua senha : ")
if D != A or E != B:
    print("usuário ou senha incorreta!")
    sys.exit()
else:
    print("logado com sucesso !")
F = print ("*OLÁ BEM VINDO AO NOTURNOCHAM criado por Cetka_1337*")

if len(sys.argv) < 2:
    print('\n Use: python3 noturnocham.py [IP]')
    exit(1)

ports = [21, 22, 80, 8080, 443, 53, 3306, 3389]

for i in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)
    try:
        response = client.connect_ex((sys.argv[1], i))
        if response == 0:
            print('PORT: ' + str(i) + ' OPEN')
    except:
        print('[ERROR] HOST NOT FOUND')
        exit(1)


