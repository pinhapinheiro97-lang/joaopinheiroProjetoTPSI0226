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

#validadores usados em criar, editar, pesquisar
def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("O número inserido tem de ser inteiro.")
def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("O valor tem de ser numérico.")

def ler_email(mensagem):
    while True:
        email = input(mensagem)
        if validar_email(email):
            return email
        print("Email inválido.")

def ler_contacto(mensagem):
    while True:
        contacto = input(mensagem)
        if validar_contacto(contacto):
            return contacto
        print("O número tem que ter 9 digítos.")

def ler_data(mensagem):
    while True:
        data = input(mensagem)
        if validar_data(data):
            return data
        print("Insere a data no formato YYYY-MM-DD .")

