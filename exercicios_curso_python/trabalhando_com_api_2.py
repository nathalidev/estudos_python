from requests import get #Importa a biblioteca requests, que permite fazer requisições a api's.
from rich.console import Console 
from rich.table import Table

response = get("https://pokeapi.co/api/v2/pokemon").json()
# print(f"aaaaaaaaah{response['status_code']}")
print(f"aaaaaaaaah{response['headers']}")
# print(response.headers["Content-Type"]) assim eu vou ver o tipo do conteudo que a api ta me retornando
#devo rodar isso antes de tentar transformar em json
console = Console()
table = Table(title="Pokémon - Primeiros 20")

table.add_column("Nome", style="cyan", no_wrap=True)
table.add_column("URL", style="magenta")


for pokemon in response["results"]:
    table.add_row(
        pokemon["name"],
        pokemon["url"],
    )

console.print(table)