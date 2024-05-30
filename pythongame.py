import operator
import time
import os
import random
import getpass
from IPython.display import clear_output

global players 
players = {'Alan':[30,20,70], 'Gabo':[15,60,30]}#Dicc principal, agregue valores 
reglas = {'pi' :['fu', 'ti', 'es'], 'pa' :['pi', 'ag' 'ai'], 'ti' :['ai', 'pa', 'es'], 'fu' :['ti', 'es', 'pa'], 'ag' :['ti', 'fu', 'pi'], 'ai' :['fu', 'pi', 'ag'], 'es' :['ag', 'ai', 'pa']}
optionsppt = ["Piedra", "Papel", "Tijera", "Fuego", "Agua", "Aire", "Esponja"]

def scores(name): #Función de puntuaciones
  search(name)
  r = name in players
  if r == False:
    print("𝘌𝘭 𝘫𝘶𝘨𝘢𝘥𝘰𝘳 𝘯𝘰 𝘦𝘴𝘵𝘢́ 𝘥𝘢𝘥𝘰 𝘥𝘦 𝘢𝘭𝘵𝘢...\n")
    time.sleep(3)
    clear_output()
    return 0
  if players[name]:
    print("\033[1;37;41m"+"Ｈｏｌａ {} ｔｉｅｎｅｓ ｌａｓ ｓｉｇｕｉｅｎｔｅｓ ｐｕｎｔｕａｃｉｏｎｅｓ： \n".format(name))
    matchescores(name)
    ranking(name)
  else:
    print("\033[1;30;47m"+"Ｅｌ ｊｕｇａｄｏｒ {} ａｕｎ ｎｏ ｔｉｅｎｅ ｐｕｎｔｕａｃｉｏｎｅｓ\n".format(name))
  time.sleep(10)
  clear_output()
  principal_menu()
def ranking(name): # Función que muestra el ranking
    total = {k: sum(v) for k,v in players.items()}
    checkdicc = dict(sorted(total.items(), key= lambda item:item[1], reverse=True),)
    i = 0
    for m in checkdicc:
        i+=1
        if m == name:
            print("\033[1;30;47m"+"{} ｅｓｔá ｅｎ ｌａ ｐｏｓｉｃｉｏｎ： {}\n".format(name,i))
    total_sorted = sorted(total.items(), key= operator.itemgetter(1), reverse=True)
    print("\033[1;37;40m"+"RANKING:\n") 
    for n in enumerate(total_sorted):
        print(n[1][0], ' ｔｉｅｎｅ ',total[n[1][0]], ' ｐｕｎｔｏｓ')
    print("\n")
def matchescores(name): #Función que muestra los puntajes obtenidos en cada partida por el jugador ingresado
    i = 1
    y = 0
    for x in players[name]:
        print("Ｐａｒｔｉｄａ {} = {} ｐｕｎｔｏｓ".format(i,players[name][y]))
        i+=1
        y+=1
    print("\n")
def search(name): #Funcion que busca el nombre dentro del registro de nombres
  r = name in players
  if r == True:
    return name
  else:
    opt = int(input("¿Ｑｕｉｅｒｅ ａｇｒｅｇａｒ ａｌ ｊｕｇａｄｏｒ？\n１． Ｓｉ\n２． Ｎｏ\n\nＲｅｓｐｕｅｓｔａ："))
    if opt == 1:
      register(name)
      return name
    else:
      return 0
    time.sleep(5)
    clear_output()
    principal_menu()
def register(name): #Funcion que registra nombres al diccionario principal
  r = name in players
  if r == True:
    print("\n𝘌𝘭 𝘶𝘴𝘶𝘢𝘳𝘪𝘰 𝘺𝘢 𝘦𝘴𝘵𝘢́ 𝘥𝘢𝘥𝘰 𝘥𝘦 𝘢𝘭𝘵𝘢, 𝘪𝘯𝘵𝘦𝘯𝘵𝘦 𝘥𝘦 𝘯𝘶𝘦𝘷𝘰...\n")
    add()
  else:
    players[name] = []
    print("                              ＥＬ ＪＵＧＡＤＯＲ ＨＡ ＳＩＤＯ ＡＧＲＥＧＡＤＯ \u2713\n")
  time.sleep(5)
  clear_output()
  principal_menu()
def add(): #Funcion que agrega nombres al diccionario principal, esta funcion
    # se usa dentro de la funcion register(), si alguien ingreso un nombre ya existente, intenta poner uno nuevo dentro de la funcion add()
  newname = input("Nᴏᴍʙʀᴇ ᴅᴇ ᴜsᴜᴀʀɪᴏ: ")
  r = newname in players
  if r == True:
    print("\n𝘌𝘭 𝘶𝘴𝘶𝘢𝘳𝘪𝘰 𝘺𝘢 𝘦𝘴𝘵𝘢́ 𝘥𝘢𝘥𝘰 𝘥𝘦 𝘢𝘭𝘵𝘢, 𝘪𝘯𝘵𝘦𝘯𝘵𝘦 𝘥𝘦 𝘯𝘶𝘦𝘷𝘰...\n")
    add()
  else:
    players[newname] = []
    print("                              ＥＬ ＪＵＧＡＤＯＲ ＨＡ ＳＩＤＯ ＡＧＲＥＧＡＤＯ \u2713\n")
  time.sleep(5)
  clear_output()
  principal_menu()

def play(name):
    opt = int(input("Ｓｅｌｅｃｃｉｏｎｅ ｕｎａ ｏｐｃｉｏｎ ｄｅ ｊｕｅｇｏ\n０． Ｒｅｇｌａｓ ｄｅｌ ｊｕｅｇｏ\n１． Ｍｏｄｏ ｓｏｌｉｔａｒｉｏ\n２． Ｄｏｓ ｊｕｇａｄｏｒｅｓ\nＲｅｓｐｕｅｓｔａ： "))
    if opt == 0:
      print("Puedes ver las reglas del juego en el siguiente enlace: \nhttps://prograinternet2trabajos.000webhostapp.com/juego.html")
      time.sleep(8)
      clear_output()
      play(name)
    if opt == 1:
        playsolo(name)
    if opt == 2:
        play2player()
    else:
        print("𝙊𝙥𝙘𝙞𝙤𝙣 𝙣𝙤 𝙫𝙖𝙡𝙞𝙙𝙖, 𝙞𝙣𝙩𝙚𝙣𝙩𝙚 𝙙𝙚 𝙣𝙪𝙚𝙫𝙤...\n")
        play(name)

def playsolo(name):
  lookfor(name)
  print("Ｅｌ ｊｕｅｇｏ ｉｎｉｃｉａｒá")
  election1 = 0
  election2 = 0
  time.sleep(2)
  clear_output()
  wins = 0
  loses = 0
  aleatorio = random.randint(1,2)
  for f in range(5):
    opc2=0
    #while 1> opc2 >7:
    if aleatorio == 1:
      print("Ｉｎｉｃｉａ '{}'\n".format(name))
      opc2 = election(1)#hace elegir una opcion de piedra papel o tijera
      election1 = elections_search(opc2)#hace la traduccion del numero a los keys utilizados en el diccionario
      computer = random.randint(1,7)
      print("Ｌａ ｃｏｍｐｕｔａｄｏｒａ ｅｓｃｏｇｉó {}".format(optionsppt[computer-1]))
      time.sleep(3)
      election2 = elections_search(computer)#hace la eleccion de la computadora
    if aleatorio == 2:
      print("Ｉｎｉｃｉａ Ｌａ Ｃｏｍｐｕｔａｄｏｒａ \n".format(name))
      time.sleep(2)
      print(". . . . .")
      print("Ｌｉｓｔｏ， ｔｕｒｎｏ ｄｅ '{}'\n".format(name))
      opc2 = election(1)#hace elegir una opcion de piedra papel o tijera
      election1 = elections_search(opc2)#hace la traduccion del numero a los keys utilizados en el diccionario
      computer = random.randint(1,7)
      print("Ｌａ ｃｏｍｐｕｔａｄｏｒａ ｅｓｃｏｇｉｏ {}".format(optionsppt[computer-1]))
      time.sleep(3)
      election2 = elections_search(computer)#hace la eleccion de la computador
    if election2 == election1:#caso empate
      print("Ｅｍｐａｔｅ❗❗\n")
    elif election2 in list(reglas[election1]):#caso ganador
      print("Ｇａｎａｓｔｅ\n")
      wins += 1
    else: #caso perder
      print("Ｐｅｒｄｉｓｔｅ\n")
      loses += 1
    time.sleep(2)
    clear_output()
  puntaje = calculo_puntuaciones(wins, loses)#calcula el puntaje obtenido
  if wins >= 3:
    print("\033[1;37;44m" + "Ｆｅｌｉｃｉｄａｄｅｓ， ｅｒｅｓ ｅｌ ｇａｎａｄｏｒ❗❗")
  else:
    print("\033[1;30;47m" + "𝚀𝚞𝚎 𝚕𝚊𝚜𝚝𝚒𝚖𝚊, 𝚙𝚎𝚛𝚍𝚒𝚜𝚝𝚎 :(")
  print("Ｇａｎａｓｔｅ {} ｄｅ ５ ｐａｒｔｉｄａｓ： ｓｅ ｔｅ ｓｕｍａｒａ ｕｎａ ｐｕｎｔｕａｃｉｏｎ ｄｅ {}".format(wins, puntaje))#print cuantos puntos se sumaron
  players[name].append(puntaje)#añade puntaje
  time.sleep(10)
  clear_output()
  principal_menu()

def play2player():
  print("Ａｍｂｏｓ ｊｕｇａｄｏｒｅｓ ｄｅｂｅｎ ｅｓｔａｒ ｒｅｇｉｓｔｒａｄｏｓ ｐａｒａ ｊｕｇａｒ\n")
  p1 = input("Ｉｎｇｒｅｓｅ ｅｌ ｎｏｍｂｒｅ ｄｅｌ ｐｒｉｍｅｒ ｊｕｇａｄｏｒ：")
  p2 = input("Ｉｎｇｒｅｓｅ ｅｌ ｎｏｍｂｒｅ ｄｅｌ ｓｅｇｕｎｄｏ ｊｕｇａｄｏｒ： ")
  lookfor(p1)
  lookfor(p2)
  l1 = []
  l2 = []
  print("\nＥｌ ｊｕｅｇｏ ｉｎｉｃｉａｒａ．．．")
  time.sleep(3)
  clear_output()
  wins1 = 0
  loses1 = 0
  wins2 = 0
  loses2 =0
  draw1 = 0
  draw2 = 0
  aleatorio = random.randint(1,2) #Elige que jugador inciará a jugar
  if aleatorio == 1: 
    print("Ｉｎｉｃｉａｒá {}".format(p1))
  if aleatorio == 2:
    print("Ｉｎｉｃｉａｒá {}".format(p2))
  for f in range(5):
    opc2=0
    opc3=0
    if aleatorio == 1:
      opc2 = election(p1)#eleccion de opciones
      election1 = elections_search(opc2)#traduccion de opciones a los dados en el diccionario
      opc3 = election(p2)  
      election2 = elections_search(opc3)
    else: 
      opc3 = election(p2)  
      election2 = elections_search(opc3)
      opc2 = election(p1)
      election1 = elections_search(opc2)
    if election2 == election1:#caso empate
      print("Ｅｍｐａｔｅ❗❗")
      draw1 +=1
      draw2 += 2
    elif election2 in list(reglas[election1]):#caso gana jugador 1
      print("Ｇａｎａ{}\n".format(p1))
      wins1 += 1
      loses2 += 1
    else: 
      print("Ｇａｎａ {}\n".format(p2))#caso gana jugador 2
      wins2 += 1
      loses1 += 1
    time.sleep(2)
    clear_output()
  puntaje1 = calculo_puntuaciones(wins1, loses1)#calcula puntajes
  puntaje2 = calculo_puntuaciones(wins2, loses2)
  if wins1 >= 3:
    print(("Ｆｅｌｉｃｉｄａｄｅｓ {}， Ｇａｎａｓｔｅ ｌａ ｐａｒｔｉｄａ❗").format(p1))#imprime al ganador
    time.sleep(3)
  elif wins2 >= 2:
    print(("Ｆｅｌｉｃｉｄａｄｅｓ {}， Ｇａｎａｓｔｅ ｌａ ｐａｒｔｉｄａ❗").format(p2))#imprime al ganador
  elif wins1 == wins2:
    print(("Ｆｅｌｉｃｉｄａｄｅｓ  {}, Ｆｅｌｉｃｉｄａｄｅｓ  {}, Ｆｕｅ ｕｎ ｅｍｐａｔｅ❗.").format(p1, p2))#imprime al ganador
  print("𝙹𝚞𝚐𝚊𝚍𝚘𝚛 𝟷, 𝚐𝚊𝚗𝚊𝚜𝚝𝚎 {} 𝚍𝚎 𝟻 𝚙𝚊𝚛𝚝𝚒𝚍𝚊𝚜: 𝚜𝚎 𝚝𝚎 𝚜𝚞𝚖𝚊𝚛𝚊́ 𝚞𝚗𝚊 𝚙𝚞𝚗𝚝𝚞𝚊𝚌𝚒𝚘́𝚗 𝚍𝚎 {}".format(wins1, puntaje1))#imprime puntaje añadido
  print("𝙹𝚞𝚐𝚊𝚍𝚘𝚛 𝟸, 𝚐𝚊𝚗𝚊𝚜𝚝𝚎 {} 𝚍𝚎 𝟻 𝚙𝚊𝚛𝚝𝚒𝚍𝚊𝚜: 𝚜𝚎 𝚝𝚎 𝚜𝚞𝚖𝚊𝚛𝚊́ 𝚞𝚗𝚊 𝚙𝚞𝚗𝚝𝚞𝚊𝚌𝚒𝚘́𝚗 𝚍𝚎 {}\n".format(wins2, puntaje2))
  players[p1].append(puntaje1)#añade los puntajes al diccionario
  players[p2].append(puntaje2)
  print("{}:\t\t\t\t\t\t{}:\n".format(p1,p2))
  print("𝙿𝚊𝚛𝚝𝚒𝚍𝚊𝚜 𝚐𝚊𝚗𝚊𝚍𝚊𝚜: {}\𝚝\𝚝\𝚝\𝚝𝙿𝚊𝚛𝚝𝚒𝚍𝚊𝚜 𝚐𝚊𝚗𝚊𝚍𝚊𝚜: {}\n".format(wins1,wins2))
  print("𝙿𝚊𝚛𝚝𝚒𝚍𝚊𝚜 𝚙𝚎𝚛𝚍𝚒𝚍𝚊𝚜: {}\𝚝\𝚝\𝚝\𝚝𝙿𝚊𝚛𝚝𝚒𝚍𝚊𝚜 𝚐𝚊𝚗𝚊𝚍𝚊𝚜: {}\n".format(loses1,loses2))
  print("𝙿𝚊𝚛𝚝𝚒𝚍𝚊𝚜 𝚎𝚖𝚙𝚊𝚝𝚊𝚍𝚊𝚜: {}\𝚝\𝚝\𝚝\𝚝𝙿𝚊𝚛𝚝𝚒𝚍𝚊𝚜 𝚐𝚊𝚗𝚊𝚍𝚊𝚜: {}\n".format(draw1,draw2))
  time.sleep(10)
  clear_output()
  principal_menu()

def election(numjugador = ""):#eleccion de numero de opcion
    print("Ｅｌｉｇｅ ｕｎａ ｏｐｃｉｏｎ ｊｕｇａｄｏｒ {} ：".format(numjugador))
    eleccionjugador = int(getpass.getpass(" \n║１．  Ｐｉｅｄｒａ║🪨 \n║２．   Ｐａｐｅｌ ║📄 \n║３．  Ｔｉｊｅｒａ ║✂ \n║４     Ｆｕｅｇｏ ║🔥 \n║５．     Ａｇｕａ ║💦 \n║６．     Ａｉｒｅ ║💨 \n║７． Ｅｓｐｏｎｊａ║🧽\n"))
    clear_output()
    while eleccionjugador not in range(1,8):#en caso de seleccionar una opcion no establecida se repite la intruccion para regresar valor valido
        eleccionjugador = int(getpass.getpass("Ｌａ ｒｅｓｐｕｅｓｔａ ｓｅｌｅｃｃｉｏｎａｄａ ｎｏ ｅｘｉｓｔｅ， ｓｅｌｅｃｃｉｏｎａ ｕｎａ ｅｘｉｓｔｅｎｔｅ：\n\n║１．  Ｐｉｅｄｒａ║🪨 \n║２．   Ｐａｐｅｌ ║📄 \n║３．  Ｔｉｊｅｒａ ║✂ \n║４     Ｆｕｅｇｏ ║🔥 \n║５．     Ａｇｕａ ║💦 \n║６．     Ａｉｒｅ ║💨 \n║７． Ｅｓｐｏｎｊａ║🧽\n"))
        clear_output()
    return eleccionjugador

def elections_search(election):#dependiendo de la opcion escogida la pasa a str que concuerde con el diccionario de reglas
    if election == 1:
        return 'pi'
    elif election == 2:
        return 'pa'
    elif election == 3:
        return 'ti'
    elif election == 4:
        return 'fu'
    elif election == 5:
        return 'ag'
    elif election == 6:
        return 'ai'
    elif election == 7:
        return 'es'

def calculo_puntuaciones(ganadas, perdidas):#calcula las puntuaciones
    contador_puntos = 0
    contador_puntos = ganadas * 30
    contador_puntos = contador_puntos + (perdidas * (-5))
    contador_puntos = contador_puntos + ((5 - (ganadas + perdidas)) * 15)
    if ganadas == 5:
        contador_puntos += contador_puntos * 2
    elif ganadas == 4:
        contador_puntos += 100
    elif ganadas == 3: 
        contador_puntos += 50
    return contador_puntos

def lookfor(name):
  r = name in players
  if r == True:
    return name
  else:
    print("Ｅｌ ｊｕｇａｄｏｒ ＇{}＇ ＮＯ ｅｓｔａ ｒｅｇｉｓｔｒａｄｏ， ｎｅｃｅｓｉｔａ ｒｅｇｉｓｔｒａｒｓｅ ｐａｒａ ｊｕｇａｒ".format(name))
    time.sleep(5)
    clear_output()
    principal_menu()


def principal_menu(): #MENU PRINCIPAL xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  print("\033[1;37;40m")
  print(" ╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗ ")
  print(" ║                                  ╔══╗╔══╦═══╦═╗ ╔╦╗  ╔╦═══╦═╗ ╔╦══╦═══╦═══╦═══╗   ╔═══╦╗       ╔╦╗ ╔╦═══╦═══╦═══╗                                  ║ ")
  print(" ║                                  ║╔╗║╚╣╠╣╔══╣║╚╗║║╚╗╔╝║╔══╣║╚╗║╠╣╠╩╗╔╗║╔═╗║╔═╗║   ║╔═╗║║       ║║║ ║║╔══╣╔═╗║╔═╗║         s$$                      ║ ")
  print(" ║                                  ║╚╝╚╗║║║╚══╣╔╗╚╝╠╗║║╔╣╚══╣╔╗╚╝║║║ ║║║║║ ║║╚══╗   ║║ ║║║       ║║║ ║║╚══╣║ ╚╣║ ║║   ,    $$$$.    s$³              ║ ")
  print(" ║                                  ║╔═╗║║║║╔══╣║╚╗║║║╚╝║║╔══╣║╚╗║║║║ ║║║║║ ║╠══╗║   ║╚═╝║║ ╔╗  ╔╗║║║ ║║╔══╣║╔═╣║ ║║  s$   ‘³$$$$   $$$               ║ ")
  print(" ║                                  ║╚═╝╠╣╠╣╚══╣║ ║║║╚╗╔╝║╚══╣║ ║║╠╣╠╦╝╚╝║╚═╝║╚═╝║   ║╔═╗║╚═╝║  ║╚╝║╚═╝║╚══╣╚╩═║╚═╝║  $$    ³$$$$$.  ³$$s             ║ ")
  print(" ║                                  ╚═══╩══╩═══╩╝ ╚═╝ ╚╝ ╚═══╩╝ ╚═╩══╩═══╩═══╩═══╝   ╚╝ ╚╩═══╝  ╚══╩═══╩═══╩═══╩═══╝  ³$.    ³$$$$$$  s$$$    s´      ║ ")
  print(" ║                   ╔══╗                                                                                              ³$$s   ³$$$$$   $$$³  s$’      ║ ")
  print(" ║               ╔═══╝││╚═╗     ╔═══╗                         ╔═╦═╦══╦══╦══╦══╦═╗                                       ³$$s    $$$$$  $$$’  s$$      ║ ")
  print(" ║             ╔═╝│││││╔══╩═╦═══╝│││╚╗                        ║╬║╬╠╗╔╣═╦╣╔╗║╔╗║╦╝                                  `s.  $$$$    s$$$$  $$$³ .s$$³  s  ║ ")
  print(" ║           ╔═╩═╗│╔═══╝││││╚══╗│││││║                        ║╔╣╔╝║║║╔╝║╠╣║╠╣║╩╗                                   s$  $$$$s  $$$$$$$ $$$$$$_s$$     ║ ")
  print(" ║         ╔═╝│╔═╩═╝│││││││││││╚═╗││╔╝                        ╚╝╚╝ ╚╝╚╝ ╚╝╚╩╝╚╩═╝                                   s$$$$$$$$$ $$$$$$$$$$$$$$$$$³     ║ ")
  print(" ║         ╚╗╔═╝│││││││││││││││││╚╦═╝                                                                              s$$$ssss$$$$$$$$$$$$$ssss$$$$$´    ║ ")
  print(" ║          ╚╩╗│││││││││││││││││││╚╗                      1.    Rᴇɢɪsᴛʀᴀʀ ᴊᴜɢᴀᴅᴏʀ                                 ³§§§§§§§§§§§§§§$$$$$$§§§§§§§§§§s    ║ ")
  print(" ║            ╚══╗│││╔══╗│││││││││╔╝                      2.  Vᴇʀɪғɪᴄᴀʀ ᴘᴜɴᴛᴜᴀᴄɪᴏɴᴇs                               ³§§§§§§§§§§$$$$$$§§§§§§§§§§§s      ║ ")
  print(" ║               ╚═══╝  ╚══╗││╔═══╝                       3.          Jugar                                            §§§§§§§§§§§§§§§§§§§§§§         ║ ")
  print(" ║                         ╚══╝                           4.          Sᴀʟɪʀ                                              ³§§§§§§§§§§§§§§§§            ║ ")
  print(" ╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝ ")
  opt =int(input("                                                 Rᴇsᴘᴜᴇsᴛᴀ: "))

  clear_output()
  
  if opt == 1 or opt==2 or opt ==3:
    name = input("                                          Nᴏᴍʙʀᴇ ᴅᴇ ᴜsᴜᴀʀɪᴏ: ").capitalize()
  if opt == 1:
    register(name)
  elif opt == 2:
    scores(name)
  elif opt == 3:
    play(name)
  elif opt == 4:
    print("\033[1;30;47m" + "𝙂𝙍𝘼𝘾𝙄𝘼𝙎 𝙋𝙊𝙍 𝙅𝙐𝙂𝘼𝙍❗❗")
    exit
  else:
    print("\033[1;37;41m" + "𝙊𝙥𝙘𝙞𝙤𝙣 𝙣𝙤 𝙫𝙖𝙡𝙞𝙙𝙖, 𝙞𝙣𝙩𝙚𝙣𝙩𝙚 𝙙𝙚 𝙣𝙪𝙚𝙫𝙤...")
    principal_menu()
  if opt==1 or opt==2 or opt==3:
    principal_menu()
time.sleep(5)
clear_output()
principal_menu()