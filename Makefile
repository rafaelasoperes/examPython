PYTHON = python3
MAIN = exam.py
RENDU = rendu
TRACES = traces

.PHONY: all run start check clean fclean re help

all: run

run:
	$(PYTHON) $(MAIN)

start: run

check:
	$(PYTHON) -m py_compile $(MAIN)

clean:
	rm -rf $(RENDU)/*
	rm -rf $(TRACES)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

fclean: clean
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache

re: fclean run

help:
	@echo "Comandos disponíveis:"
	@echo "  make          - roda o exam"
	@echo "  make run      - roda o exam.py"
	@echo "  make start    - alias para run"
	@echo "  make check    - verifica erro de sintaxe no exam.py"
	@echo "  make clean    - limpa rendu, traces e caches Python"
	@echo "  make fclean   - limpeza completa"
	@echo "  make re       - limpa tudo e roda o exam"
	@echo "  make help     - mostra esta ajuda"