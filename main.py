import json

produto1: dict = {
    "nome":"Sapato",
    "quantidade":2,
    "preco":44.99,
    "disponibilidade":True
}

produto2: dict = {
    "nome":"TV",
    "quantidade":1,
    "preco":1900,
    "disponibilidade":True
}


carrinho = list = []
carrinho.append(produto1)
carrinho.append(produto2)

carrinho_json = json.dumps(carrinho)

print(carrinho_json)