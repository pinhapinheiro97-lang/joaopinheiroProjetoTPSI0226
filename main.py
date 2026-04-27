#Projeto Final Python - Sistema de Gestão de uma Agência Musical

import os as fsos
import json

#Guarda apenas dados das bandas
bands = [
    {
        "id": 1,
        "nome": "Xutos e Pontapés",
        "numeros_membros": 5,
        "genero": "Rock",
        "contacto": "912654789",
        "email": "xutosepontapes@gmail.com",
        "disponivel": True
    }
]
#Guarda apenas dados dos eventos
events=[
    {
        "id": 1,
        "nome_evento": "Festas do Barreiro",
        "local": "Barreiro",
        "data": "2026-05-05",
        "cachet": 2500.50,
        "tipo_evento": "Festas Populares",
        "estado_evento": "planeado"
    }
]

#ligação entre as bandas e eventos geridos
bookings = [
    {
        "id": 1,
        "band_id": 1,
        "event_id": 1,
        "data_marcacao": "2026-04-27",
        "estado_confirmacao": "pendente",
        "observacoes": "A aguardar resposta da banda"
    }
]

