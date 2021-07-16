from ajuda.interface import linha,menu,titulo
from ajuda.arquivos import criarPerfil,mostrarsaldo, aposta, apagarPerfil
from ajuda.erros import leiastr

cor = [
'\033[1;30m', # 0 = Preto
'\033[1;31m', # 1 = Vermelho
'\033[1;32m', # 2 = Verde
'\033[1;33m', # 3 = Amarelo
'\033[1;34m', # 4 = Azul
'\033[1;35m', # 5 = Magenta
'\033[1;36m', # 6 = Ciano
'\033[1;37m'] # 7 = Cinza

#código principal
while True:
  opc = menu()
  if opc == 1:
    mostrarsaldo(leiastr(f'{cor[3]}Digite o nome do Perfil para ver o Saldo: '))
  if opc == 2:
    aposta()
  if opc == 3:
    criarPerfil(leiastr(f'{cor[3]}Digite o Nome do Perfil que Quer Criar: '))
  if opc == 4:
    apagarPerfil(leiastr(f'{cor[3]}Digite o Nome do Perfil que Quer Apagar: '))
  if opc == 5:
    print("\033[1;36mAdios!")
    linha(2)
    break