# Python Exam

Projeto inspirado no estilo do **ExamShell**, criado para praticar exercícios de Python.

Este repositório fornece um sistema simples para gerar questões, implementar soluções e verificar automaticamente usando testes.

- As questões ficam diretamente em `questions/<nome_da_questao>/` (layout plano). Isso facilita adicionar ou reorganizar exercícios.

---

## Como executar

Usando o Makefile:

```bash
make
```

ou:

```bash
make run
```

Diretamente com Python:

```bash
python3 exam.py
```

Ao iniciar, o programa mostra um menu com opções reduzidas:

```text
[1] Start   - Iniciar o exam (todas as questões)
[2] Verifier - Verificar questão atual
[3] Sair
```

Escolha `Start` para iniciar o exam — o sistema carregará todas as pastas dentro de `questions/`, sorteará a ordem e criará uma pasta `rendu/<nome_da_questao>/` para cada questão conforme forem sorteadas.

---

## Estrutura esperada de uma questão (layout plano)

Coloque cada questão como uma pasta em `questions/` com estes arquivos:

```
questions/
├── echo_validator/
│   ├── question.txt
│   ├── solution.py
│   └── tests.py
├── mirror_matrix/
│   ├── question.txt
│   ├── solution.py
│   └── tests.py
└── ... (outras questões)
```

- `question.txt` — enunciado da questão.
- `solution.py` — solução de referência (o sistema lê essa função para obter a assinatura esperada e também para referência).
- `tests.py` — lista `TESTS` com casos usados pelo verificador.

Durante o exam, o usuário edita apenas o arquivo `rendu/<nome_da_questao>/solution.py` criado automaticamente.

---

## Fluxo básico

1. Executar `python3 exam.py` ou `make run`.
2. Escolher `[1] Start` para iniciar — o sistema sorteará as questões e criará `rendu/<questao>/`.
3. Editar `rendu/<questao>/solution.py` com sua implementação.
4. No menu do exam escolher `Verifier` para rodar os testes da questão atual.
5. Se todos os testes passarem, o exam avança para a próxima questão; caso contrário, ajuste a sua solução e verifique novamente.

Observação sobre pular questões (`Next`):

- No menu de ações da questão existe a opção `Next` (atalho `5`). Ao escolher `Next`, o sistema pula para a próxima questão sorteada sem executar os testes da questão atual. Por padrão ele remove a pasta `rendu/<nome_da_questao>/` gerada para a questão pulada. Use esta opção quando quiser ignorar temporariamente uma questão.


---

## Traces e saída

Ao verificar uma questão, o sistema grava traces em `traces/<nome_da_questao>/`:

- `trace_ok.txt` — salvo quando todos os testes passaram.
- `trace_error.txt` — salvo quando houve falha/erro.

Esses arquivos ajudam a diagnosticar problemas de implementação.

---

## Makefile — principais comandos

```bash
make         # Executa o exam
make run     # Executa exam.py
make check   # Verifica sintaxe de exam.py
make clean   # Remove rendu/ e traces/
make fclean  # Limpeza completa
make re      # Limpa e executa novamente
make help    # Mostra os comandos
```

---

## Objetivo

Prover um ambiente leve para praticar problemas de programação em Python, com geração automática de esqueleto de solução, testes e traces.

