# Testes para merge_sorted_lists

TESTS = [
    {
        'name': 'Listas simples ordenadas',
        'args': [[1, 3, 5], [2, 4, 6]],
        'expected': [1, 2, 3, 4, 5, 6]
    },
    {
        'name': 'Uma lista vazia',
        'args': [[1, 2, 3], []],
        'expected': [1, 2, 3]
    },
    {
        'name': 'Ambas listas vazias',
        'args': [[], []],
        'expected': []
    },
    {
        'name': 'Listas com números negativos',
        'args': [[-5, -1, 0], [-3, 2, 4]],
        'expected': [-5, -3, -1, 0, 2, 4]
    },
    {
        'name': 'Listas com duplicatas',
        'args': [[1, 2, 2, 3], [2, 3, 4]],
        'expected': [1, 2, 2, 2, 3, 3, 4]
    },
    {
        'name': 'Primeira lista maior',
        'args': [[1, 2, 3, 4, 5], [6]],
        'expected': [1, 2, 3, 4, 5, 6]
    }
]
