# Estudos em Python

Repositório pessoal para estudar Python por meio de aulas, exercícios e
pequenos projetos. Os exemplos são intencionalmente independentes: a ideia é
abrir um arquivo, executar, alterar e observar o resultado.

## Organização

| Caminho | Conteúdo |
| --- | --- |
| [`aulas_do_curso/`](./aulas_do_curso/) | Exemplos curtos, organizados por conceito |
| [`exercicios_curso_python/`](./exercicios_curso_python/) | Prática organizada por tema e complexidade |
| [`exercicio_importacoes/`](./exercicio_importacoes/) | Exercício isolado de módulos e imports |
| [`projeto_teste_importacoes/`](./projeto_teste_importacoes/) | Exemplo de pacotes e importações entre arquivos |
| [`docs/`](./docs/) | Guias de estudo e resumo dos conceitos |

As pastas numeradas sugerem uma sequência, mas não são obrigatórias. Comece
pela [trilha de estudo](./docs/GUIA_DE_ESTUDO.md) e consulte o
[mapa de conceitos](./docs/CONCEITOS.md) quando quiser revisar um assunto.

## Como estudar

1. Leia o objetivo no guia do tema.
2. Execute o exemplo original.
3. Faça uma pequena alteração e preveja o resultado antes de executar.
4. Compare a previsão com a saída e anote o que aprendeu.
5. Resolva um exercício do tema sem consultar a solução imediatamente.

## Como executar

Na raiz do repositório, com Python 3 instalado:

```bash
python caminho/para/o_arquivo.py
```

Alguns exemplos dependem de bibliotecas externas. Consulte
[`requirements.txt`](./requirements.txt) e instale as dependências em um
ambiente virtual quando necessário:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Os arquivos que usam entrada do teclado, rede, interface do sistema ou
bibliotecas opcionais podem exigir configuração adicional. Eles estão
preservados como material de estudo e não como uma aplicação pronta para
produção.
