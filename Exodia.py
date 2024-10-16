#Libs importadas
import os

#Menu Exodia
def ExodiaMenu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
███████╗██╗  ██╗ ██████╗ ██████╗ ██╗ █████╗ 
██╔════╝╚██╗██╔╝██╔═══██╗██╔══██╗██║██╔══██╗
█████╗   ╚███╔╝ ██║   ██║██║  ██║██║███████║
██╔══╝   ██╔██╗ ██║   ██║██║  ██║██║██╔══██║
███████╗██╔╝ ██╗╚██████╔╝██████╔╝██║██║  ██║
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝
____________________________________________
''')
        try:
            choose = int(input('[1]Tools\n[2]Arsenal\n[0]Exit\n>>> '))
            
            #Options
            if choose == 1:
                ToolsMenu()
                break
            elif choose == 2:
                ArsenalMenu()
                break
            elif choose == 0:
                print('Bye Bye...')
                break
            else:
                input('Choose a valid option!')
        except ValueError:
            input('Invalid option! Press Enter to try again...')

#Menu Tools
def ToolsMenu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
░▀█▀░█▀█░█▀█░█░░░█▀▀
░░█░░█░█░█░█░█░░░▀▀█
░░▀░░▀▀▀░▀▀▀░▀▀▀░▀▀▀
____________________
''')
        try:
            choose = int(input('[1]Vulnerability Scanner\n[2]Reconnaissance\n[3]Network Analysis\n[4]Exploits\n[5]Fuzzing\n[0]Exit\n>>> '))
            
            #Options
            if choose == 1:
                VulnerabilityScannerMenu()
                break
            elif choose == 2:
                ReconnaissanceMenu()
                break
            elif choose == 3:
                NetworkAnalysisMenu()
                break
            elif choose == 4:
                ExploitsMenu()
                break
            elif choose == 5:
                FuzzingMenu()
                break
            elif choose == 5:
                BruteForceMenu()
                break
            elif choose == 0:
                print('Bye Bye...')
                break
            else:
                input('Choose a valid option!')
        except ValueError:
            input('Invalid option! Press Enter to try again...')

def VulnerabilityScannerMenu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
░█░█░█░█░█░░░█▀█░█▀▀░█▀▄░█▀█░█▀▄░▀█▀░█░░░▀█▀░▀█▀░█░█
░▀▄▀░█░█░█░░░█░█░█▀▀░█▀▄░█▀█░█▀▄░░█░░█░░░░█░░░█░░░█░
░░▀░░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀░▀░▀▀░░▀▀▀░▀▀▀░▀▀▀░░▀░░░▀░
░█▀▀░█▀▀░█▀█░█▀█░█▀█░█▀▀░█▀▄                        
░▀▀█░█░░░█▀█░█░█░█░█░█▀▀░█▀▄                        
░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░▀░▀▀▀░▀░▀ 
____________________________________________________                       
''')

def ReconnaissanceMenu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
░█▀▄░█▀▀░█▀▀░█▀█░█▀█░█▀█░█▀█░▀█▀░█▀▀░█▀▀░█▀█░█▀█░█▀▀░█▀▀
░█▀▄░█▀▀░█░░░█░█░█░█░█░█░█▀█░░█░░▀▀█░▀▀█░█▀█░█░█░█░░░█▀▀
░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀▀▀
________________________________________________________
''')

def NetworkAnalysisMenu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
░█▀█░█▀▀░▀█▀░█░█░█▀█░█▀▄░█░█░░░█▀█░█▀█░█▀█░█░░░█░█░█▀▀░▀█▀░█▀▀
░█░█░█▀▀░░█░░█▄█░█░█░█▀▄░█▀▄░░░█▀█░█░█░█▀█░█░░░░█░░▀▀█░░█░░▀▀█
░▀░▀░▀▀▀░░▀░░▀░▀░▀▀▀░▀░▀░▀░▀░░░▀░▀░▀░▀░▀░▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀▀
______________________________________________________________
''')

def ExploitsMenu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
░█▀▀░█░█░█▀█░█░░░█▀█░▀█▀░▀█▀░█▀▀
░█▀▀░▄▀▄░█▀▀░█░░░█░█░░█░░░█░░▀▀█
░▀▀▀░▀░▀░▀░░░▀▀▀░▀▀▀░▀▀▀░░▀░░▀▀▀
________________________________
''')

def FuzzingMenu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
░█▀▀░█░█░▀▀█░▀▀█░▀█▀░█▀█░█▀▀
░█▀▀░█░█░▄▀░░▄▀░░░█░░█░█░█░█
░▀░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀
____________________________
''')

def BruteForceMenu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
░█▀▄░█▀▄░█░█░▀█▀░█▀▀░░░█▀▀░█▀█░█▀▄░█▀▀░█▀▀
░█▀▄░█▀▄░█░█░░█░░█▀▀░░░█▀▀░█░█░█▀▄░█░░░█▀▀
░▀▀░░▀░▀░▀▀▀░░▀░░▀▀▀░░░▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀
__________________________________________
''')


#Menu Arsenal        
def ArsenalMenu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
░█▀█░█▀▄░█▀▀░█▀▀░█▀█░█▀█░█░░
░█▀█░█▀▄░▀▀█░█▀▀░█░█░█▀█░█░░
░▀░▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀▀▀
____________________________
''')
        try:
            choose = int(input('[1]Defense\n[2]Attack\n[0]Exit\n>>> '))
            
            #Options
            if choose == 1:
                DefenseMenu()
                break
            elif choose == 2:
                AttackMenu()
                break
            elif choose == 0:
                print('Bye Bye...')
                break
            else:
                input('Choose a valid option!')
        except ValueError:
            input('Invalid option! Press Enter to try again...')

def DefenseMenu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
░█▀▄░█▀▀░█▀▀░█▀▀░█▀█░█▀▀░█▀▀
░█░█░█▀▀░█▀▀░█▀▀░█░█░▀▀█░█▀▀
░▀▀░░▀▀▀░▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀
____________________________
''')

def AttackMenu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
░█▀█░▀█▀░▀█▀░█▀█░█▀▀░█░█
░█▀█░░█░░░█░░█▀█░█░░░█▀▄
░▀░▀░░▀░░░▀░░▀░▀░▀▀▀░▀░▀
''')
























#Run
ExodiaMenu()