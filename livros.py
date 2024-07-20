# Dicionário para armazenar informações de um livro,

livro1: dict = {
    "Título":"Sul",
    "Autor":"Não lembro",
    "Ano":2001
}

livro2: dict = {
    "Título":"Fortaleza digital",
    "Autor":"Dan Brown",
    "Ano":2000
}

livros: list = []
livros.append(livro1)
livros.append(livro2)

print(livros)

lista_de_livros_usando_dict: dict = {
    "livro1": {
        "Título":"Sul",
        "Autor":"Não lembro",
        "Ano":2001
    },
    "livro2": {
        "Título":"Fortaleza digital",
        "Autor":"Dan Brown",
        "Ano":2000
    }
}

print(lista_de_livros_usando_dict["livro2"]["Título"])