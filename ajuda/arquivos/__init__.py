from ajuda.interface import linha, menuaposta, menubin
from ajuda.erros import leiastr, leiadim, leiaint2
from time import sleep
from random import randrange
import os

def aposta():
  nome = leiastr('Nome do Perfil: ')
  linha(2)
  name = nome.upper().strip()
  try:
    a = open(name,'rt')
    a.close
  except:
    print('\033[1;31mAlgo deu errado!\033[m')
  else:
    while True:
      try:
        g = leiadim('Qual valor quer apostar?: K$')
      except:
        linha(2)
        print('\033[1;31mAlgo deu errado!\033[m')
      else:
        a = open(name,'rt')
        n1 = a.read()
        a.close()
        k = float(n1)
        if g > k or g < 0:
          linha(2)
          print(f"\033[1;31mVocê não pode apostar K${g}!\033[m")
        else:
          n2 = menuaposta()
          n3 = randrange(1,3)
          if n3 == 1:
            s1 = '\033[1;34mAzul\033[m'
          elif n3 == 2:
            s1 = '\033[1;31mVermelho\033[m'
          if n2 == n3:
            print(f'\033[1;32m-> A bola caiu no {s1},\033[1;32m Você Ganhou K${2*g:.2f}! ')
            a = open(name,'rt')
            antes = a.read()
            a.close()
            a = open(name, 'wt')
            a.write(f'{float(antes)+g}')
            a.close()
          else:
            print(f'\033[1;31m-> A bola caiu no {s1},\033[1;31m Você Perdeu!\033[m ')
            a = open(name,'rt')
            antes = a.read()
            a.close()
            a = open(name, 'wt')
            a.write(f'{float(antes)-g}')
            a.close()
          s2 = menubin()
          if s2 == 2:
            break



        
    

def strtodim (str):
  a = float(str)
  b = str(f'{a:.2f}')
  c = b.replace('.',',')
  return c

def criarPerfil(nome):
  name = nome.strip().upper()
  try:
    a = open(name, 'rt')
    a.close()
  except:
    try:
      a = open(name, 'wt+')
      a.close()
      a = open(name, 'at')
      a.write('10000')      
    except:
      print('Não foi possível criar Perfil')
    else:
      linha(2)
      print('\033[1;32mPerfil criado com Sucesso - K$10.000 Adicionado à sua conta!\033[m')
      linha(2)
      sleep(2)
  else:
    linha(2)
    print("\033[1;31mEsse perfil ja Existe\033[m")
    linha(2)
    sleep(2)

def apagarPerfil(nome):
  name = nome.strip().upper()
  try:
    a = open(name, 'rt')
    a.close
  except:
    linha(2)
    print("\033[1;31mEsse perfil não Existe\033[m")
    linha(2)
    sleep(2)
  else:
    linha(2)
    os.remove(name)
    print('\033[1;32mPerfil Apagado com Sucesso! \033[m')
    linha(2)
    sleep(2)
  

def mostrarsaldo(nome):
  name = nome.strip().upper()
  try:
    a=open(name,'rt')
    linha(2)
    g = a.read()
    p = float(g)
    h = str(f'{p:.2f}')
    print(f'\033[1;33mVocê está com \033[1;32mK${h.replace(".",",")}\033[m')
    sleep(2)
    a.close
  except:
    linha(2)
    print('\033[1;31mNão foi possível acessar o Saldo! Esse perfil não existe.\033[m')