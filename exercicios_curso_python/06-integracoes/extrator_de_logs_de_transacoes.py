import re

logs = """
[2026-11-13] TXN-8841 | Cliente: "Ana Silva" | Valor: R$ 1.250,50 | Status: APROVADO
[2026-11-13] DEBUG: Conexao reestabelecida com banco de dados
[2026-11-13] TXN-92 | Cliente: "Carlos Souza" | Valor: R$ 89,90 | Status: RECUSADO
[2026-11-13] TXN-10492 | Cliente: "Mariana Costa" | Valor: R$ 450,00 | Status: APROVADO
[2026-11-13] TXN-7731 | Cliente: "João Pedro" | Valor: R$ 12,00 | Status: PENDENTE
[2026-11-13] ERRO-500 | Falha critica no gateway
"""
print(re.findall(r'(TXN-[0-9]+).*?([A-Z][a-zA-ZÀ-ÿ]+ [A-Z][a-zA-ZÀ-ÿ]+).*?(\b[A-Z][A-Z]{6,})', logs))

