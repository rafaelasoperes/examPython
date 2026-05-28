# Testes para crypto_sorter

TESTS = [
    {
        'name': 'Ordena por comprimento',
        'args': [["apple", "pie", "banana"]],
        'expected': ["pie", "apple", "banana"]
    },
    {
        'name': 'Ordena por ASCII quando comprimentos iguais',
        'args': [["dog", "cat", "bat"]],
        'expected': ["bat", "cat", "dog"]
    },
    {
        'name': 'Ordena por número de vogais',
        'args': [["aeiou", "xyz", "hello"]],
        'expected': ["xyz", "hello", "aeiou"]
    },
    {
        'name': 'Lista com um elemento',
        'args': [["hello"]],
        'expected': ["hello"]
    },
    {
        'name': 'Lista vazia',
        'args': [[]],
        'expected': []
    },
    {
        'name': 'Strings com maiúsculas',
        'args': [["Apple", "apple", "APPLE"]],
        'expected': ["APPLE", "Apple", "apple"]
    }
]
