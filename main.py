### IMPORT ###
import os
import os, sys, time, os.path, ctypes, getpass
from pystyle import Center, Anime, Colors, Colorate, System
from colorama import Fore
from requests import get
#0.0.2
import requests

### Les couleurs ###
VERSIONETOOL = "V1"
c = Fore.LIGHTCYAN_EX
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX
m = Fore.LIGHTMAGENTA_EX


### SCHERMATA ###
def impostatitolo(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} | https://github.com/St3rong/")
    elif system == 'posix':
        sys.stdout.write(f"\x1b]0;{_str} | https://github.com/St3rong/\x07")
    else:
        pass

def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    return

def titolohome():
    print(f"""\n\n
              ____   _         _____                                                 _          __        
 / ___| | |_  _ __|___ /   ___   _ __    __ _   ___   ___  _ __ __   __ (_) _ __   / _|  ___  
 \___ \ | __|| '__| |_ \  / _ \ | '_ \  / _` | / __| / _ \| '__|\ \ / / | || '_ \ | |_  / _ \ 
  ___) || |_ | |   ___) || (_) || | | || (_| | \__ \|  __/| |    \ V /  | || | | ||  _|| (_) |
 |____/  \__||_|  |____/  \___/ |_| |_| \__, | |___/ \___||_|     \_/   |_||_| |_||_|   \___/ 
                                        |___/                                                 
\n""".replace('█', f'{g}█{y}'))

banner = r"""
███████╗████████╗██████╗ ██████╗  ██████╗ ███╗   ██╗ ██████╗        
██╔════╝╚══██╔══╝╚════██╗██╔══██╗██╔═══██╗████╗  ██║██╔════╝        
███████╗   ██║    █████╔╝██████╔╝██║   ██║██╔██╗ ██║██║  ███╗       
╚════██║   ██║    ╚═══██╗██╔══██╗██║   ██║██║╚██╗██║██║   ██║       
███████║   ██║   ██████╔╝██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝██╗    
╚══════╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝    
                                                                    
"""[1:]

def transizione():
    clear()
    caricamento()
    clear()

def caricamento():
	carattere = ['|', '/', '-', '\\']
	for i in carattere+carattere+carattere:
		sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Chargement... {i}""")
		sys.stdout.flush()
		time.sleep(0.2)


#0.0.2
global server
class cercamelo:
    def link():
        global server

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
            "sec-ch-ua": '"Chromium";v="96", "Opera GX";v="82", ";Not A Brand";v="99"',
	    "origin": "https://servers.fivem.net",
	    "referer": "https://servers.fivem.net/",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 OPR/82.0.4227.25"
        }

        data = requests.get(f"https://servers-frontend.fivem.net/api/servers/single/{server['id']}", headers=headers)
        return {
        	"ip": data.json()["Data"]["connectEndPoints"][0],
        	"hostname": data.json()["Data"]["hostname"]
        }
        pass

#0.0.1
global ipserver
ipserver = 'Aucun serveur configuré'
global portaserver
portaserver = '30120'
def main():
    global ipserver
    global portaserver
    impostatitolo(f"Str3ong Server Info {VERSIONETOOL} -")
    #System.Size(160, 40) #120, 30
    Anime.Fade(Center.Center(banner), Colors.green_to_red, Colorate.Vertical, time=1)
    clear()
    impostatitolo(f"Str3ong Server Info {VERSIONETOOL}")
    titolohome()
    print(f"""      {y}[{b}+{y}]{g} Main:                                                                            {y}[{b}+{y}]{c} Settings:
          {y}[{w}1{y}]{g} Info server                                                                      {y}[{w}10{y}]{c} Définir le port du serveur (30120 par défaut)
          {y}[{w}2{y}]{g} Liste des joueurs                                                                   {y}[{w}11{y}]{c} ip server  
          {y}[{w}3{y}]{g} Liste des joueurs avec identifiants      
          {y}[{w}4{y}]{g} Obtenir l'IP à partir du lien (cfx.re/join/679aqj)
          
                                                                                     {m}Made by St3rong. | https://github.com/St3rong/
                                                                                     {m}IP Server     : {b}{ipserver}
                                                                                     {m}Port         : {b}{portaserver}
\t\t\t\t\t\t\t\t\t\t\t\t\t""")
    global scelta
    scelta = input(f"""{y}[{b}#{y}]{w} : """)
    if scelta == '1' or scelta == '01':
        if ipserver != 'Aucun serveur configuré':
            try:
                dynamic = get(f'http://{ipserver}:{portaserver}/dynamic.json', timeout=5)
                print('Attendi...')
                getdynamic = dynamic.json()
                hostname = getdynamic["hostname"]
                online = str(getdynamic["clients"])
                massimi = str(getdynamic["sv_maxclients"])
                iv = str(getdynamic["iv"])
                gametype = str(getdynamic["gametype"])
                mapname = str(getdynamic["mapname"])

                print(f'''
{y}Informations obtenues:{m} https://github.com/St3rong/ {w}

HostName: {hostname}
Players: {online}/{massimi}
IV: {iv}
GameType: {gametype}
MapName: {mapname}''')
                input(f"{y}[{b}#{y}]{w} Appuyez sur Entrée pour revenir à la page d'accueil")
                main()
            except Exception as errore:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Errore [{errore}]!")
                main()
        else:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} IP du serveur manquante [bouton 11 sur la page d'accueil]!")
            main()

    elif scelta == '2' or scelta == '02':
        if ipserver != 'Nessun server impostato':
            try:
                players = get(f'http://{ipserver}:{portaserver}/players.json', timeout=5)
                print('Attendez...')
                getplayers = players.json()
                for player in getplayers:
                    print(f"{y}[{player['id']}] {w}| {g}{player['name']} {w}| {c}Ping:{player['ping']}{w}")

                input(f"{y}[{b}#{y}]{w} Appuyez sur Entrée pour revenir à la page d'accueil")
                main()
            except Exception as errore:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Error [{errore}]!")
                main()
        else:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} IP du serveur manquante !")
            main()

    elif scelta == '3' or scelta == '03':
        if ipserver != 'Aucun serveur configuré':
            try:
                players = get(f'http://{ipserver}:{portaserver}/players.json', timeout=5)
                print('Attendi...')
                getplayers = players.json()
                for player in getplayers:
                    print(f"{y}[{player['id']}] {w}| {g}{player['name']} {w}| {c}{player['identifiers']}{w}")

                input(f"{y}[{b}#{y}]{w} Appuyez sur Entrée pour revenir à la page d'accueil")
                main()
            except Exception as errore:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Error [{errore}]!")
                main()
        else:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} IP du serveur manquante  !")
            main()
    elif scelta == '4' or scelta == '04': #0.0.2
        try:
            diocane = input(f'''{y}[{b}#{y}]{w} Saisissez le lien du serveur (exemple : cfx.re/join/vjarme) :    ''')
            print(F'{y}[{b}#{y}]{w} Chargement... Recherche IP {diocane}')
            global server
            server = {}
            s2 = server['link'] = diocane
            server['id'] = os.path.basename(s2) 
            server['data'] = cercamelo.link()
            print(f"""{g}Opération terminée{w}
{b}URL: {diocane} {w}---> {c}IP: {server['data']['ip']}{w}""")
            input(f"{y}[{b}#{y}]{w} Appuyez sur Entrée pour revenir à la page d'accueil")
            main()
        except Exception as errore:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Error [{errore}]!")
            main()
    elif scelta == '5' or scelta == '05': #0.0.3
        if ipserver != 'Aucun serveur configuré':
            try:
                info = get(f'http://{ipserver}:{portaserver}/info.json', timeout=5)
                print('Attendi...')
                getinfo = info.json()
                risorse = getinfo["resources"]
                print(f"{y}{risorse}{w}")
                input(f"{y}[{b}#{y}]{w} Appuyez sur Entrée pour revenir à la page d'accueil")
                main()
            except Exception as errore:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Errore [{errore}]!")
                main()
        else:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} IP du serveur manquante !")
            main()
    elif scelta == '10' or scelta == '010':
        transizione()
        diocaporta = input(f'''{y}[{b}#{y}]{w} Entrez le port du serveur:    ''')
        portaserver = diocaporta
        main()
    elif scelta == '11' or scelta == '011':
        transizione()
        diocane = input(f'''{y}[{b}#{y}]{w} Entrez l'IP NUMÉRIQUE du serveur:    ''')
        ipserver = diocane
        main()
    elif scelta == 'exit' or scelta == 'close':
        transizione()
        sys.exit()
    else:
        clear()
        main()


main()
