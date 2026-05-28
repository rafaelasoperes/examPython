# Testes para number_base_converter

TESTS = [
    {
        'name': 'Decimal para binário',
        'args': ["10", 10, 2],
        'expected': "1010"
    },
    {
        'name': 'Binário para decimal',
        'args': ["1010", 2, 10],
        'expected': "10"
    },
    {
        'name': 'Decimal para hexadecimal',
        'args': ["255", 10, 16],
        'expected': "FF"
    },
    {
        'name': 'Hexadecimal para decimal',
        'args': ["FF", 16, 10],
        'expected': "255"
    },
    {
        'name': 'Bases não-padrão',
        'args': ["120", 8, 5],
        'expected': "441"
    },
    {
        'name': 'Zero em qualquer base',
        'args': ["0", 10, 2],
        'expected': "0"
    },
    {
        'name': 'Número inválido para a base',
        'args': ["18", 8, 10],
        'expected': "ERROR"
    }
]
