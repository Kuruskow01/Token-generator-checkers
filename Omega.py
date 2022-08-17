from concurrent.futures import thread
from string import Template
from time import sleep
from pystyle import Anime , Colors , Colorate , Center , System , Box , Write
from requests import get
import json
import random
import threading

System.Size(140 , 40)
System.Title("Ghost V1")

ghostface = f"""


    !                          :
   !§%::                       &$
  :#§§/§#$!:              !%&##§§!
  :§§§§§§§§/*           $#§§§§§§§$
   $§§§§§§§§@          !§§§§§§§§/!
    *§§§§§§§§#*      :$&§§§§§§§#!
     $§§§§§§§§&:     %§§§§§§§§§:
     :@&&§§§&&%  :!: */#§§§§#/$
         :!:     %/!  ::!**! :
                 &§@
                *§/§%            !:
   *!           :*:*:           */:
   @/%!*@@*             :  :$@*%§/:
   @§§§§§§§&!::*%%*:  !@/$%#§§§§§&
   $§§§//§§§§/§§§§§/&&§§§§§§§§§§§!
   !@@%:!#§§§§§§§§§§§§§§§§§§%%@$!
         :#//&$@/§§§§@*$§/@!
           :    :$&@!   ::

"""

ghost = """

 ██████╗ ███╗   ███╗███████╗ ██████╗  █████╗ 
██╔═══██╗████╗ ████║██╔════╝██╔════╝ ██╔══██╗
██║   ██║██╔████╔██║█████╗  ██║  ███╗███████║
██║   ██║██║╚██╔╝██║██╔══╝  ██║   ██║██╔══██║
╚██████╔╝██║ ╚═╝ ██║███████╗╚██████╔╝██║  ██║
 ╚═════╝ ╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝
                                             
"""

Menu = """1 - Token Checker
2 - Mass Token Checker
3 - Token Informations
4 - Token Generator
5 - Crédits
"""



def TokenInfo(token):

    r = get('https://discord.com/api/v10/users/@me', headers = {'Authorization': token , 'Content-Type': 'application/json'})
    data = r.json()
    
    f = open("info.txt" , 'w')
    f.write(f"{data}")
    f.close()

    print()
    Write.Input(f"[!] Finished Results are in info.txt", Colors.blue_to_cyan, interval=0.0025)

def MassToken(combo):
    System.Clear()
    print(Colorate.Horizontal(Colors.blue_to_cyan , Center.XCenter(ghost)))
    print()
    print()

    with open(combo , 'r') as f:
        content = f.read().split('\n')

    File = open("HIT.txt" , 'w')


    for token in content:
        mass = get("https://discordapp.com/api/v9/users/@me?verified", headers={"authorization": token}).status_code

        if mass == 200:
            Write.Print(f"[+] {token} Valid\n", Colors.blue_to_cyan, interval=0.0025)
            File.write(token+ '\n')
        if mass == 401:
            Write.Print(f"[-] {token} Invalid\n", Colors.red_to_blue, interval=0.0025)
    
    
    print()
    Write.Input(f"[!] Checking Finished Valid Token are in HIT.txt", Colors.blue_to_cyan, interval=0.0025)

def TokenCheck(token):
    checker = get("https://discordapp.com/api/v9/users/@me?verified", headers={"authorization": token}).status_code
    if checker == 200:
        print()
        Write.Input("[+] This Token is Valid !" , Colors.purple_to_blue , interval=0.00025)
        exit()

    if checker == 401:
        print()
        Write.Input("[-] This Token is Invalid !" , Colors.purple_to_blue , interval=0.00025)
        exit()

def TokenGen(gen):

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"

    for i in range(gen):
        premiere_partie = ''.join((random.choice(chars) for i in range(24)))
        deuxieme_partie = ''.join((random.choice(chars) for i in range(6)))
        troisieme_partie = ''.join((random.choice(chars) for i in range(27)))

        resultat = premiere_partie + "." + deuxieme_partie + "." + troisieme_partie

        result = open("resultat.txt", "a")
        result.write(resultat + "\n")
    print("C'est fini.\nLes tokens ce trouves dans resultat.txt")
    sleep(3)
    exit()



def Main():
    Anime.Fade(Center.Center(ghostface), Colors.blue_to_cyan, Colorate.Vertical , enter=True)
    print(Colorate.Horizontal(Colors.blue_to_cyan , Center.XCenter(ghost)))
    print(Colorate.Horizontal(Colors.blue_to_cyan  , Center.XCenter(Box.DoubleCube(Menu))))
    print()
    choice = Write.Input("Select A Number -> " ,  Colors.blue_to_cyan , interval=0.0025)
    if choice == "1" :
        print()
        token1 = Write.Input("Discord Token -> "  , Colors.blue_to_cyan, interval=0.0025)
        TokenCheck(token1)
    if choice == "2":
        print()
        combo = Write.Input("Token Combolist -> "  , Colors.blue_to_cyan , interval=0.0025)
        MassToken(combo)
    if choice == "3":
        print()
        token2 = Write.Input("Discord Token -> "  , Colors.blue_to_cyan , interval=0.0025)
        TokenInfo(token2)
    if choice == "4":
        print()
        gen = int(Write.Input("Combiens de token ->", Colors.blue_to_cyan , interval=0.0025))
        TokenGen(gen)
    if choice == "5":
        print()
        Crédits = int(Write.Input("Crée par matxd291\nhttps://discord.gg/NUcdbT2S\nhttps://discord.gg/XqJvvEbB\net ajouts du gen + credits par Krm#1385\nhttps://discord.gg/5PMGxPsf", Colors.blue_to_cyan , interval=0.0025))
        sleep(5)
        TokenGen(Crédits)
    



Main()
