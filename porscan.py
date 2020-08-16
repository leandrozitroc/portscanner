import socket


print("NMAP MEU")
print("==-==" * 2)
host = input('Insira o Ip a ser pesquisado : ')

port1 = range(0,1000)


def portscan(host , port1):
    for c in port1:
        scan(host , c)

def scan(host , porta):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        if s.connect_ex((host, porta)) == 0:
            print("==-==" * 4)
            print(f'A {porta} esta aberta')
            print(banner(host , porta))
            print("==-==" * 4)

    except:
        pass



def banner(host, port1):

    try:
        sock = socket.socket()
        sock.connect((host,port1))
        sock.settimeout(2)
        sock.send(b"hello\n")
        retorno = sock.recv(1024)
        print(retorno.decode().strip())
    except:
        print("Nao consuimos o banner desta porta")



portscan(host, port1)
