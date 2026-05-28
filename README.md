# Python Exam

Projeto inspirado no estilo do **ExamShell**, criado para praticar exercícios de Python por nível de dificuldade.

O objetivo é permitir que o usuário escolha um nível, receba uma questão, implemente a solução em um arquivo gerado automaticamente e depois valide a resposta com testes.

---

## Instrução

Para iniciar o projeto, execute:

```bash
make
```

ou:

```bash
make run
```

Também é possível rodar diretamente com Python:

```bash
python3 exam.py
```

Ao iniciar o programa, será exibido um menu com os níveis disponíveis:

```text
[1] Easy
[2] Medium
[3] Hard
[4] Verifier
[5] Sair
```

Escolha o nível desejado e o sistema irá sortear uma questão disponível naquele nível.

Depois que a questão for selecionada, o projeto cria uma pasta dentro de `rendu/` contendo:

```text
question.txt
solution.py
```

O arquivo `question.txt` contém o enunciado da questão.

O arquivo `solution.py` é onde a solução deve ser implementada.

Exemplo:

```text
rendu/py_mirror_matrix/
├── question.txt
└── solution.py
```

Após escrever a solução, volte ao terminal do exam e escolha a opção:

```text
[1] Verificar
```

Se todos os testes passarem, o sistema avança para a próxima questão.

Se algum teste falhar, será exibido o erro para que a solução possa ser corrigida.

---

## Descrição

Este projeto é um sistema simples de exam em Python.

Ele organiza exercícios em três níveis:

```text
Easy
Medium
Hard
```

Cada nível possui suas próprias questões dentro da pasta `questions/`.

A estrutura esperada para uma questão é:

```text
questions/easy/nome_da_questao/
├── question.txt
├── solution.py
└── tests.py
```

Onde:

- `question.txt` contém o enunciado da questão.
- `solution.py` contém a solução de referência usada pelo sistema.
- `tests.py` contém os testes usados para validar a resposta do usuário.

Durante o exam, o usuário não edita os arquivos da pasta `questions/`.

A solução do usuário sempre deve ser feita dentro da pasta `rendu/`, no arquivo `solution.py` gerado automaticamente para a questão atual.

O sistema compara a resposta do usuário com os testes definidos para aquela questão.

---

## Recursos

### Seleção por nível

O usuário pode escolher entre:

```text
Easy
Medium
Hard
```

Cada nível possui uma lista própria de exercícios.

---

### Sorteio de questões

Ao iniciar um nível, o sistema busca as questões disponíveis na pasta correspondente e sorteia a ordem em que elas serão resolvidas.

Exemplo:

```text
questions/easy/
questions/medium/
questions/hard/
```

---

### Geração automática da solução

Para cada questão, o sistema cria automaticamente uma pasta dentro de `rendu/`.

Dentro dela, são criados os arquivos necessários para o aluno resolver a questão:

```text
rendu/nome_da_questao/question.txt
rendu/nome_da_questao/solution.py
```

O arquivo `solution.py` já vem com a assinatura da função esperada.

Exemplo:

```python
def mirror_matrix(matrix: list[list]) -> list[list]:
    # Sua solução aqui
    pass
```

---

### Verificação automática

O sistema executa os testes definidos no arquivo `tests.py` da questão.

Se a saída da função do usuário for igual ao resultado esperado, o teste passa.

Exemplo de resultado:

```text
✓ Teste 1: PASSED
✓ Teste 2: PASSED
✓ Teste 3: PASSED
```

Se a resposta estiver incorreta, o sistema mostra o valor esperado e o valor recebido.

Exemplo:

```text
✗ Teste 1: FAILED
Esperado: [3, 2, 1]
Recebido: [1, 2, 3]
```

---

### Traces de execução

Quando a verificação é executada, o sistema pode salvar arquivos de trace dentro da pasta `traces/`.

Exemplo:

```text
traces/nome_da_questao/trace_ok.txt
traces/nome_da_questao/trace_error.txt
```

Esses arquivos ajudam a entender quais testes passaram ou falharam.

A pasta `traces/` não precisa existir inicialmente. Ela será criada automaticamente quando o sistema precisar salvar um trace.

---

### Comandos do Makefile

O projeto possui um `Makefile` para facilitar o uso.

Comandos disponíveis:

```bash
make
```

Executa o exam.

```bash
make run
```

Executa o arquivo principal `exam.py`.

```bash
make check
```

Verifica se o arquivo `exam.py` possui erros de sintaxe.

```bash
make clean
```

Remove os arquivos gerados em `rendu/`, remove `traces/` e limpa caches do Python.

```bash
make fclean
```

Executa uma limpeza mais completa, removendo também caches de ferramentas como `pytest`, `mypy` e `ruff`, caso existam.

```bash
make re
```

Limpa o projeto e executa o exam novamente.

```bash
make help
```

Mostra a lista de comandos disponíveis.

---

## Estrutura do projeto

```text
.
├── Makefile
├── README.md
├── exam.py
├── questions/
│   ├── easy/
│   ├── medium/
│   └── hard/
├── rendu/
└── traces/
```

> Observação: a pasta `traces/` pode não existir inicialmente. Ela será criada automaticamente quando houver execução de testes com geração de trace.

---

## Exemplo de questão

Uma questão deve seguir este formato:

```text
questions/easy/py_mirror_matrix/
├── question.txt
├── solution.py
└── tests.py
```

Exemplo de `question.txt`:

```text
A matrix is considered mirrored if each of its rows has been reversed from its original order.

Write a function:

def mirror_matrix(matrix: list[list]) -> list[list]

The function should return a new matrix where each row has its elements in reversed order.
```

Exemplo de `solution.py` de referência:

```python
def mirror_matrix(matrix: list[list]) -> list[list]:
    return [row[::-1] for row in matrix]
```

Exemplo de `tests.py`:

```python
TESTS = [
    {
        "args": [[[1, 2, 3], [4, 5, 6]]],
        "expected": [[3, 2, 1], [6, 5, 4]]
    },
    {
        "args": [[["a", "b"], ["c", "d"]]],
        "expected": [["b", "a"], ["d", "c"]]
    },
    {
        "args": [[]],
        "expected": []
    }
]
```

---

## Objetivo

O objetivo do projeto é criar um ambiente simples para treinar lógica de programação com Python, simulando uma experiência de exam.

Ele pode ser usado para:

- praticar exercícios por dificuldade;
- validar soluções automaticamente;
- organizar questões por nível;
- gerar arquivos de resposta para o aluno;
- salvar traces de testes;
- evoluir para um sistema maior de avaliação.