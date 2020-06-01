import os
import sys

if os.name == 'nt':
    direc = sys.path[0] + "\\"
else:
    direc = sys.path[0] + "/"

mal = direc + "prueba_1.txt"
ok = direc + "prueba.txt"

# try:
#f = open(mal)
#var = novar
# except FileNotFoundError as e:
# print(e)
# except NameError:
#print("error de nombre")
# except Exception:
#print("cachador universal")

#x = 10
#
# if(x > 5):
#raise Exception(f'la variable x no puede ser mayor a 5, el valor fue {x}')


try:
    f = open(mal)
except FileNotFoundError:
    print("no existe el archivo")
else:
    print("No hubo excepcion")
finally:
    print("yo siempre corro")
