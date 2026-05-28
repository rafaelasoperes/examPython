# Testes para count_consecutive_digit_pairs

TESTS = [
    {
        'name': 'Pares simples consecutivos',
        'args': ["123"],
        'expected': 2
    },
    {
        'name': 'Nenhum par válido',
        'args': ["531"],
        'expected': 0
    },
    {
        'name': 'Um único par',
        'args': ["01"],
        'expected': 1
    },
    {
        'name': 'Múltiplos pares com gaps',
        'args': ["012945"],
        'expected': 3
    },
    {
        'name': 'String vazia',
        'args': [""],
        'expected': 0
    },
    {
        'name': 'Um dígito',
        'args': ["5"],
        'expected': 0
    },
    {
        'name': 'Sequência com 89 e 9 somente',
        'args': ["89"],
        'expected': 1
    }
]
