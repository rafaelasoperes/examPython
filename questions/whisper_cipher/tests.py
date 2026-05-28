# Testes para whisper_cipher

TESTS = [
    {
        'name': 'Deslocamento simples de 1',
        'args': ["abc", 1],
        'expected': "bcd"
    },
    {
        'name': 'Deslocamento com envolvimento (wrap)',
        'args': ["xyz", 1],
        'expected': "yza"
    },
    {
        'name': 'Maiúsculas preservadas',
        'args': ["ABC", 1],
        'expected': "BCD"
    },
    {
        'name': 'Misto de maiúsculas e minúsculas',
        'args': ["AaBbCc", 1],
        'expected': "BbCcDd"
    },
    {
        'name': 'Deslocamento negativo',
        'args': ["bcd", -1],
        'expected': "abc"
    },
    {
        'name': 'Com caracteres especiais (não são deslocados)',
        'args': ["a!b@c", 1],
        'expected': "b!c@d"
    },
    {
        'name': 'Deslocamento de 26 (volta ao original)',
        'args': ["abc", 26],
        'expected': "abc"
    }
]
