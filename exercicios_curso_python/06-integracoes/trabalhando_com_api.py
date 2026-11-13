import requests #Importa a biblioteca requests, que permite fazer requisições a api's.
from rich.console import Console #Você precisa instalar com pip install requests porque ela não vem por padrão com o Python.
from rich.table import Table #Importa a biblioteca rich, que permite criar tabelas e outros elementos visuais no terminal.
dados = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL").json()

# Console é o "impressor estilizado".

# Table permite criar tabelas com cores e formatação.

console = Console() #console = Console()

table = Table(title="💱 Cotações de Moedas e Criptoativos") #Cria uma tabela com o título acima.

table.add_column("Moeda", style="cyan", no_wrap=True) #Adiciona colunas à tabela, cada uma com um nome e uma cor.no_wrap=True evita que o texto quebre em várias linhas.

table.add_column("Compra", style="green")
table.add_column("Venda", style="green")
table.add_column("Máxima", style="yellow")
table.add_column("Mínima", style="yellow")
table.add_column("Variação (%)", style="red")
table.add_column("Atualização", style="magenta")

print(f"aaaaaaaaaaah {dados.values()}")

for moeda in dados.values():
    table.add_row(
        moeda["name"],
        moeda["bid"],
        moeda["ask"],
        moeda["high"],
        moeda["low"],
        moeda["pctChange"],
        moeda["create_date"]
    )

# Adiciona uma linha à tabela com os dados de cada moeda:

# name: nome da moeda

# bid: valor de compra

# ask: valor de venda

# high: valor máximo do dia

# low: valor mínimo do dia

# pctChange: variação percentual

# create_date: data/hora da última atualização

# A correspondência entre os valores dos campos e as colunas da tabela se dá pela ordem em que você os coloca dentro do método add_row().

console.print(table) #Exibe a tabela no terminal com todas as cores e formatação.
