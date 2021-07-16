from ajuda.erros import leiaint, leiaint2
cor = [
'\033[1;30m', # 0 = Preto
'\033[1;31m', # 1 = Vermelho
'\033[1;32m', # 2 = Verde
'\033[1;33m', # 3 = Amarelo
'\033[1;34m', # 4 = Azul
'\033[1;35m', # 5 = Magenta
'\033[1;35m', # 6 = Ciano
'\033[1;37m'] # 7 = Cinza

def linha(color,tam=25):
  print(f'{cor[color]}-=\033[m'*tam)

def titulo(msg,corlin,cormsg):
  linha(corlin)
  print(f'{cor[cormsg]}{msg:^50}\033[m')
  linha(corlin)

def menu():
  titulo('Cassino do Heitor',2,3)
  print(f'{cor[4]}1- Ver Saldo')
  print(f'{cor[4]}2- Apostar')
  print(f'{cor[4]}3- Criar Perfil')
  print(f'{cor[4]}4- Apagar Perfil')
  print(f'{cor[4]}5- Sair do Sistema')
  linha(2)
  h = leiaint('Sua Opção: ')
  linha(2)
  return h

def menuaposta():
  titulo('Em que cor?',2,3)
  print(f'{cor[4]}1- Azul')
  print(f'{cor[1]}2- Vermelho')
  linha(2)
  h = leiaint2('Sua Opção: ')
  linha(2)
  return h

def menubin():
  titulo('Quer Continuar?',2,3)
  print(f'{cor[4]}1- Sim')
  print(f'{cor[1]}2- Não')
  linha(2)
  h = leiaint2('Sua Opção: ')
  linha(2)
  return h