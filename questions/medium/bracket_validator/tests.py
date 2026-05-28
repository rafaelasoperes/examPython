# Testes para bracket_validator

TESTS = [
    {
        'name': 'Parênteses balanceados simples',
        'args': ["()"],
        'expected': True
    },
    {
        'name': 'Múltiplos parênteses balanceados',
        'args': ["()[]{}"],
        'expected': True
    },
    {
        'name': 'Aninhamento correto',
        'args': ["([{}])"],
        'expected': True
    },
    {
        'name': 'Parênteses desbalanceados - falta fechar',
        'args': ["(()"],
        'expected': False
    },
    {
        'name': 'Ordem incorreta',
        'args': ["(]"],
        'expected': False
    },
    {
        'name': 'String vazia',
        'args': [""],
        'expected': True
    },
    {
        'name': 'Só colchetes fechados',
        'args': ["]"],
        'expected': False
    }
]
