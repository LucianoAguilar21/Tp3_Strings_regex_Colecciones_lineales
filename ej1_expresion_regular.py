import re

patron = "^\\(0345\\)\s[154][0-9]{6}|^\\+549345[0-9]{7}|^3454[0-9]{6}|^154[0-9]{6}"


lista_numeros = ["(0345) 154123456","+5493454123456","3454123456",
                "+54011123456","34564123456","154123456","(0345) 154asdasd"]


for numero in lista_numeros:
    if re.findall(patron,numero):
        print("# " + numero + ": ¡VALIDO!")
    else:
        print("# " + numero + ": ¡NO VALIDO!")