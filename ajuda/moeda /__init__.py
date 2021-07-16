from ajuda.erros import leiastr

def strtodim (str):
  a = float(str)
  b = str(a)
  c = b.replace('.',',')
  return c
  
  