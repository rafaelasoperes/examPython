# Testes para echo_validator (Palindrome Checker)

TESTS = [
    {
        'name': 'Palavra simples',
        'args': ["A man, a plan, a canal: Panama"],
        'expected': True
    },
    {
        'name': 'Não é palíndromo',
        'args': ["race a car"],
        'expected': False
    },
    {
        'name': 'String vazia',
        'args': [" "],
        'expected': True
    },
    {
        'name': 'Palavra normal',
        'args': ["hello"],
        'expected': False
    },
    {
        'name': 'Palíndromo simples',
        'args': ["aba"],
        'expected': True
    }
]
