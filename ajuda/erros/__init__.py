def leiaint (msg):
  while True:
    try:
      h = int(input(f'{msg}'))
    except:
      print(f'\033[1;31m~~'*25)
      print(f'\033[1;31mAlgo deu Errado, Tente Novamente!\033[m')
      print('\033[1;31m~~\033[m'*25)
      continue
    else:
      if h > 5 or h < 1:
        print(f'\033[1;31m~~'*25)
        print(f'\033[1;31mAlgo deu Errado, Tente Novamente!\033[m')
        print('\033[1;31m~~\033[m'*25)
        continue
      return h
      break

def leiaint2 (msg):
  while True:
    try:
      h = int(input(f'{msg}'))
    except:
      print(f'\033[1;31m~~'*25)
      print(f'\033[1;31mAlgo deu Errado, Tente Novamente!\033[m')
      print('\033[1;31m~~\033[m'*25)
      continue
    else:
      if h > 2 or h < 1:
        print(f'\033[1;31m~~'*25)
        print(f'\033[1;31mAlgo deu Errado, Tente Novamente!\033[m')
        print('\033[1;31m~~\033[m'*25)
        continue
      return h
      break

def leiadim (msg):
  while True:
    try:
      h = str(input(f'{msg}'))
      g = h.strip().replace(",",".")
      
    except:
      print(f'\033[1;31m~~'*25)
      print(f'\033[1;31mAlgo deu Errado, Tente Novamente!\033[m')
      print('\033[1;31m~~\033[m'*25)
      continue
    else:
      return float(g)
      break

def leiastr (msg):
  while True:
    try:
      h = str(input(f'{msg}'))
    except:
      print(f'\033[1;31m~~'*25)
      print(f'\033[1;31mAlgo deu Errado, Tente Novamente!\033[m')
      print('\033[1;31m~~\033[m'*25)
      continue
    else:
      return h
      break