import os
import sys

if os.name == 'nt':
    direc = sys.path[0] + "\\"
else:
    direc = sys.path[0] + "/"

mal = direc + "prueba_1.txt"
ok = direc + "prueba.txt"
