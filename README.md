# Gestão de Bandas, Eventos e Agendamentos

Este projeto é uma aplicação de consola em Python para gerir bandas, eventos e agendamentos.

Permite:
- Adicionar, editar, eliminar e listar bandas, eventos e agendamentos.
- Pesquisar registos por diferentes campos.
- Ordenar dados manualmente com algoritmos de ordenação, como Bubble Sort e Selection Sort.
- Fazer pesquisa binária por ID em bandas e eventos.

## Funcionalidades

O projeto toma como referência três entidades principais: bandas, eventos e agendamentos. Os agendamentos funcionam como a entidade de associação entre uma banda e um evento. Cada agendamento pertence a uma única banda e a um único evento. O projeto representa, de forma simples, a gestão de bandas em contexto de marcações para atuações.

### Bandas
- Inserir novas bandas.
- Listar bandas existentes.
- Pesquisar bandas por ID, nome ou género.
- Editar bandas.
- Eliminar bandas e respetivos agendamentos associados.

### Eventos
- Inserir novos eventos.
- Listar eventos existentes.
- Pesquisar eventos por ID, nome ou local.
- Editar eventos.
- Eliminar eventos e respetivos agendamentos associados.

### Agendamentos
- Criar agendamentos entre bandas e eventos.
- Listar agendamentos.
- Pesquisar agendamentos por ID, banda, evento ou data.
- Eliminar agendamentos.

### Ordenação
- Ordenação manual dos dados.
- Possibilidade de ordenar por diferentes campos.
- Escolha da ordem crescente ou decrescente.

### Pesquisa
- Pesquisa linear para vários campos.
- Pesquisa binária por ID em bandas e eventos.

## Tecnologias usadas
- Python
- Estruturas de dados: listas e dicionários
- Funções
- Validação de dados com regex e funções auxiliares

## Estrutura do projeto
- `main.py` — ficheiro principal da aplicação.
- `criar.py` — funções para criação de bandas, eventos e agendamentos.
- `editar.py` — funções para edição de bandas, eventos e agendamentos.
- `eliminar.py` — funções para eliminação de bandas, eventos e agendamentos.
- `listar.py` — funções para mostrar os dados.
- `validadores.py` — funções de validação de entrada.
- `pesquisar.py` — funções de pesquisa.
- `ordenar.py` — funções de ordenação.
- `estatistica.py` — funções de estatística.
- `dados.py` — funções para carregar e guardar os dados.

## Objetivo do projeto
Este projeto foi desenvolvido como projeto final da UC 00620. Serve como réplica de um sistema de gestão de uma agência musical, com funcionalidades como registo, validação, armazenamento e manipulação de dados de forma persistente em formato JSON.

## Copyright

© 2026 João Pinheiro. Projeto académico.