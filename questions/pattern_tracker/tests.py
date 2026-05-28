# Testes para pattern_tracker

TESTS = [
    {
        'name': 'Padrão simples de dígitos consecutivos',
        'args': ["123"],
        'expected': 2
    },
    {
        'name': 'Dígitos com caracteres não-numéricos',
        'args': ["a1b2c3"],
        'expected': 2
    },
    {
        'name': 'Nenhum padrão válido',
        'args': ["531"],
        'expected': 0
    },
    {
        'name': 'Apenas letras (sem dígitos)',
        'args': ["abc"],
        'expected': 0
    },
    {
        'name': 'String vazia',
        'args': [""],
        'expected': 0
    },
    {
        'name': 'Múltiplos padrões separados',
        'args': ["012_945_678"],
        'expected': 6
    },
    {
        'name': 'Padrão em sequência contínua',
        'args': ["0123456789"],
        'expected': 9
    }
]
