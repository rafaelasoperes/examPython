# Testes para permutation_checker

TESTS = [
    {
        'name': 'Anagrama simples',
        'args': ["listen", "silent"],
        'expected': True
    },
    {
        'name': 'Não é anagrama',
        'args': ["hello", "world"],
        'expected': False
    },
    {
        'name': 'Strings idênticas',
        'args': ["test", "test"],
        'expected': True
    },
    {
        'name': 'Maiúsculas e minúsculas diferentes',
        'args': ["Listen", "Silent"],
        'expected': True
    },
    {
        'name': 'Comprimentos diferentes',
        'args': ["abc", "abcd"],
        'expected': False
    },
    {
        'name': 'Strings vazias',
        'args': ["", ""],
        'expected': True
    },
    {
        'name': 'Anagrama com espaços',
        'args': ["a b", "b a"],
        'expected': True
    }
]
