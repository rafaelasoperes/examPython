# Testes para twist_permutation

TESTS = [
    {
        'name': 'Rotação básica de 2 posições',
        'args': [[1, 2, 3, 4, 5], 2],
        'expected': [4, 5, 1, 2, 3]
    },
    {
        'name': 'Rotação de 1 posição',
        'args': [[1, 2, 3, 4, 5], 1],
        'expected': [5, 1, 2, 3, 4]
    },
    {
        'name': 'Rotação completa (volta ao original)',
        'args': [[1, 2, 3, 4, 5], 5],
        'expected': [1, 2, 3, 4, 5]
    },
    {
        'name': 'Rotação maior que o tamanho',
        'args': [[1, 2, 3, 4, 5], 7],
        'expected': [4, 5, 1, 2, 3]
    },
    {
        'name': 'Rotação de 0 posições',
        'args': [[1, 2, 3, 4, 5], 0],
        'expected': [1, 2, 3, 4, 5]
    }
]
