# regex

import re as reg

#sóo valida o padrão joao@gmail.com
def validar_email(email):
    padrao = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return reg.fullmatch(padrao, email) is not None

#Só valida 9 numeros
def validar_contacto(contacto):
    padrao = r"^\d{9}$"
    return reg.fullmatch(padrao, contacto) is not None

#Só valida padrao YY-MM-DD
def validar_data(data):
    padrao = r"^\d{4}-\d{2}-\d{2}$"
    return reg.fullmatch(padrao, data) is not None


print(validar_data("2026-14-12"))