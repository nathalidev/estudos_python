from requests import get
from requests import post
from requests import patch
from rich.console import Console 
from rich.table import Table

response = get("https://jsonplaceholder.typicode.com/posts").json()
# for post in response:
#     for chave, valor in post.items():
#         print(f"{chave}: {valor}")
#     print("-" * 20)

console = Console()
table = Table(title="Posts - JSONPlaceholder")

table.add_column("ID", style="cyan", no_wrap=True)
table.add_column("Título", style="magenta")
table.add_column("Corpo", style="green")

for linha in response:
    table.add_row(
        str(linha["id"]),
        linha["title"],
        linha["body"],
    )

console.print(table)

meu_post = {
    "userId": "10",
    "id": "101",
    "title": "Meu título",
    "body": "Meu corpo do post"
}
response_post = post("https://jsonplaceholder.typicode.com/posts", json=meu_post)
print(response_post.status_code)
print(response_post.json())

url = "https://jsonplaceholder.typicode.com/posts/1"  # atualiza o post com ID 1

atualizacao = {
    "title": "Título atualizado"
}

response = patch(url, json=atualizacao)

print(response.status_code)  # Deve retornar 200
print(response.json())       # Mostra o post com o campo atualizado

# O que significam os códigos HTTP 200 e 201
# Código     Significado	    Quando aparece
# 200        OK	                Requisição bem-sucedida	Quando você faz um GET, PATCH, ou PUT e o servidor responde com sucesso
# 201        Created	        Recurso criado com sucesso	Quando você faz um POST e o servidor cria algo novo (como um post, usuário, etc.)

# GET = pegar/informar dados
# POST = criar dados
# PUT = atualizar dados (substitui o dado todo)
# PATCH = atualizar dados (atualiza só o que você quer)
# DELETE = deletar dados