# Estoque com 8 produtos
estoque_atual = {
    "canetas": 150,
    "cadernos": 95,
    "borrachas": 40,
    "lapis": 60,
    "apontadores": 30,
    "marcadores": 80,
    "régua": 70,
    "agenda": 20
}

# Lista de movimentações do dia com as 15 movimentações
movimentacoes_dia = [
    ("canetas", "saída", 25),
    ("cadernos", "entrada", 10),
    ("borrachas", "saída", 50),
    ("lapis", "entrada", 20),
    ("apontadores", "entrada", 15),
    ("marcadores", "saída", 60),
    ("régua", "saída", 25),
    ("agenda", "entrada", 10),
    ("pastas", "entrada", 40),  #novo
    ("envelopes", "entrada", 60),  #novo
    ("canetas", "entrada", 30),
    ("lapis", "saída", 10),
    ("apontadores", "saída", 5),
    ("marcadores", "entrada", 20),
    ("régua", "entrada", 15)
]

#  movimentações
for produto, tipo, quantidade in movimentacoes_dia:
    if tipo == "entrada":
        if produto in estoque_atual:
            estoque_atual[produto] += quantidade
        else:
            estoque_atual[produto] = quantidade
    elif tipo == "saída":
        if produto in estoque_atual:
            estoque_atual[produto] -= quantidade
        else:
            # esse produto não existe, mas tentaram retirar adiciona como negativo
            estoque_atual[produto] = -quantidade

# Identifica produtos em nível baixo ≤50 unidades
produtos_baixo = [produto for produto, qtd in estoque_atual.items() if qtd <= 50]

# Relatório final
print("=== Estoque Atualizado ===")
for produto, qtd in estoque_atual.items():
    print(f"{produto}: {qtd} unidades")

print("\n=== Produtos que precisam de reposição (≤50) ===")
if produtos_baixo:
    for produto in produtos_baixo:
        print(f"- {produto}")
else:
    print("Nenhum produto em nível baixo.")
