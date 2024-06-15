def int_to_roman(num):
    # Matriz de Valores Inteiros
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    
    # Matriz com referência em Romanos
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    
    roman_num = ''
    i = 0
    
    # Busca de Valor de Entrada nas Matrizes
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num


def roman_to_int(s):
    
    # Mapa de conversão de números
    roman_to_int_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_value = 0
    
    # Calculo para conversão de Romano para Inteiro
    for char in s:
        current_value = roman_to_int_map[char]
        if current_value > prev_value:
            total += current_value - 2 * prev_value
        else:
            total += current_value
        prev_value = current_value
    return total
