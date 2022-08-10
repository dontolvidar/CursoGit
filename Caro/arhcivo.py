import re
with open('nuevo.txt') as f:
    lines = f.readlines()
    lineas=[]
    for line in lines:
        lineas.append((re.sub(r"""==.*""", '', line)))

with open('otro.txt', 'w') as w:
    w.writelines(lineas)