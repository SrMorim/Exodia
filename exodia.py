#!/usr/bin/env python3

#Libs
import os
import sys
import socket
import concurrent.futures


#Start
target = sys.argv[1]
targetip = socket.gethostbyname(target)



#Interfaces
def exodia():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''
███████╗██╗  ██╗ ██████╗ ██████╗ ██╗ █████╗ 
██╔════╝╚██╗██╔╝██╔═══██╗██╔══██╗██║██╔══██╗
█████╗   ╚███╔╝ ██║   ██║██║  ██║██║███████║
██╔══╝   ██╔██╗ ██║   ██║██║  ██║██║██╔══██║
███████╗██╔╝ ██╗╚██████╔╝██████╔╝██║██║  ██║
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝
--------------------------------------------
𝑻𝒂𝒓𝒈𝒆𝒕:{target}
𝑻𝒂𝒓𝒈𝒆𝒕 𝑰𝑷:{targetip}
''')        
        options = str(input('[1]Tools\n[2]Arsenal\n[3]New Target\n[x]exit\n>>> '))

        if options == '1':
            tools()
            break
        elif options == '2':
            arsenal()
            break
        elif options == '3':
            start()
            break
        elif options == 'x':
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print('Select valid option')
            


def tools():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''
░▀█▀░█▀█░█▀█░█░░░█▀▀
░░█░░█░█░█░█░█░░░▀▀█
░░▀░░▀▀▀░▀▀▀░▀▀▀░▀▀▀
--------------------
𝑻𝒂𝒓𝒈𝒆𝒕:{target}
𝑻𝒂𝒓𝒈𝒆𝒕 𝑰𝑷:{targetip}
''')
        options = str(input('[1]Port Scan\n[2]Recon\n[3]Exploits\n[4]Fuzzing\n[5]Brute Force\n[x]Back\n>>> '))

        if options == '1':
            portscan()
            break
        elif options == '2':
            break
        elif options == '3':
            break
        elif options == '4':
            break
        elif options == '5':
            break
        elif options == 'x':
            exodia()
            break
        else:
            print('Select valid option')

def portscan():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''
░█▀█░█▀█░█▀▄░▀█▀░░░█▀▀░█▀▀░█▀█░█▀█
░█▀▀░█░█░█▀▄░░█░░░░▀▀█░█░░░█▀█░█░█
░▀░░░▀▀▀░▀░▀░░▀░░░░▀▀▀░▀▀▀░▀░▀░▀░▀
----------------------------------
𝑻𝒂𝒓𝒈𝒆𝒕: {target}
𝑻𝒂𝒓𝒈𝒆𝒕 𝑰𝑷: {targetip}
''')
        options = str(input('[1]Start or [x]Cancel\n>>> '))

        if options == '1':
            def scan_port(host, port):
                # Número de tentativas para reduzir chances de falso negativo
                retries = 3
                for _ in range(retries):
                    try:
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                            # Timeout um pouco maior para evitar problemas de latência
                            s.settimeout(1.0)
                            if s.connect_ex((host, port)) == 0:
                                return port
                    except socket.timeout:
                        pass
                    except OSError:
                        pass
                    except:
                        pass
                return None

            def port_scanner(host=targetip, start_port=1, end_port=1024):
                open_ports = []
                total_ports = end_port - start_port + 1

                with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
                    futures = [executor.submit(scan_port, host, p) for p in range(start_port, end_port+1)]
                    completed = 0
                    for f in concurrent.futures.as_completed(futures):
                        completed += 1
                        result = f.result()
                        if result:
                            open_ports.append(result)
                        
                        # Exibe o progresso no formato "Progresso: 10/1024 portas testadas"
                        print(f"\rProgresso: {completed}/{total_ports} portas testadas", end="", flush=True)

                # Pula uma linha ao fim do progresso
                print()

                with open('scan_results.txt', 'w') as file:
                    for p in open_ports:
                        file.write(f'Porta {p} aberta\n')

                return open_ports

            results = port_scanner()
            print("Port scan concluído. Verifique o arquivo scan_results.txt.")
            input("Pressione Enter para continuar...")

        elif options == 'x':
            tools()
            break






def start():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
░█▀█░█▀▀░█░█░░░▀█▀░█▀█░█▀▄░█▀▀░█▀▀░▀█▀
░█░█░█▀▀░█▄█░░░░█░░█▀█░█▀▄░█░█░█▀▀░░█░
░▀░▀░▀▀▀░▀░▀░░░░▀░░▀░▀░▀░▀░▀▀▀░▀▀▀░░▀░
--------------------------------------
''')
    global target
    global targetip
    target = str(input('𝑻𝒂𝒓𝒈𝒆𝒕: '))
    targetip = socket.gethostbyname(target)
    exodia()



def arsenal():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''
░█▀█░█▀▄░█▀▀░█▀▀░█▀█░█▀█░█░░
░█▀█░█▀▄░▀▀█░█▀▀░█░█░█▀█░█░░
░▀░▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀▀▀
----------------------------
𝑻𝒂𝒓𝒈𝒆𝒕:{target}
𝑻𝒂𝒓𝒈𝒆𝒕 𝑰𝑷:{targetip}
''')
        options = str(input('[1]Attack\n[2]Defense\n[x]Back\n>>> '))

        if options == 'x':
            exodia()
            break
        else:
            print('Select valid option')

#Run
exodia()