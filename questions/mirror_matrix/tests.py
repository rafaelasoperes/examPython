# Testes para mirror_matrix

TESTS = [
    {
        'name': 'Matriz simples 2x2',
        'args': [[[1, 2], [3, 4]]],
        'expected': [[2, 1], [4, 3]]
    },
    {
        'name': 'Matriz 3x3',
        'args': [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]],
        'expected': [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
    },
    {
        'name': 'Matriz com uma linha',
        'args': [[[1, 2, 3, 4]]],
        'expected': [[4, 3, 2, 1]]
    },
    {
        'name': 'Matriz com uma coluna',
        'args': [[[1], [2], [3]]],
        'expected': [[1], [2], [3]]
    },
    {
        'name': 'Matriz com números negativos',
        'args': [[[-1, -2], [-3, -4]]],
        'expected': [[-2, -1], [-4, -3]]
    }
]
