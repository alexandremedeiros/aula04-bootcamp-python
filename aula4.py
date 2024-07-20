def sort_list(list_in: list) -> list:
    """
    Ordena uma lista usando o algoritmo de ordenação por seleção.
    """
    # Fazendo uma cópia da lista de entrada
    sorted_list = list_in.copy()

    for i in range(len(sorted_list) - 1):
        # Loop dos elementos após o índice i
        for j in range(i+1, len(sorted_list)):
            # Se o elemento do índice i for maior que algum elemento depois
            # dele, suas posições são trocadas.
            if sorted_list[i] > sorted_list[j]:
                sorted_list[i], sorted_list[j] = \
                    sorted_list[j], sorted_list[i]
    
    return sorted_list

# Lista a ser ordenada
list_to_sort = [64, 34, 25, 12, 22, 11, 90]

# Usando a função
sorted_list = sort_list(list_to_sort)

print(sorted_list)

print()


# Usando soluções prontas ----------------------------------------------------


# Lista a ser ordenada
list_to_sort = [64, 34, 25, 12, 22, 11, 90]

# Ordenar usando a função sorted
sorted_list = sorted(list_to_sort)

print(sorted_list)

# Ordenar usando o método .sort
# Uma cópia da lista original é feita, pois o método .sort faz a
# ordenação in-place
sorted_list = list_to_sort.copy()
sorted_list.sort()

print(sorted_list)

print()


# Normalizando nomes de usuário ----------------------------------------------


def normalize_name(name: str) -> str:
    """
    Normaliza nomes de usuário: Remove espaços no início e fim e
    transforma em minúsculas.
    """
    return name.strip().lower()

# Usando a função
names = [" Alice ", "BOB", "Carlos"]
normalized_names = [normalize_name(name) for name in names]
print(normalized_names)

print()


# Type Hint para Parâmetros --------------------------------------------------


def greeting(name: str, age: int) -> str:
	return f"Olá, {name}, você tem {age} anos."

print(greeting("Kaio", 30))


print()


# Valores Default de Parâmetros ----------------------------------------------


def greeting(name: str, age: int = 30) -> str:
	return f"Olá, {name}, você tem {age} anos."

print(greeting("Kaio"))