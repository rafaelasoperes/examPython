#!/usr/bin/env python3
"""
Exam Python Exam System
Author: rafasilv
"""

import os
import random
import shutil
import subprocess
import sys
from pathlib import Path


class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'


class Exam:
    def __init__(self):
        self.base_path = Path(__file__).parent
        self.questions_path = self.base_path / "questions"
        self.rendu_path = self.base_path / "rendu"
        self.traces_path = self.base_path / "traces"
        self.current_level = None
        self.current_question = None
        self.used_questions = []

    def clear_screen(self):
        os.system('clear' if os.name != 'nt' else 'cls')

    def print_banner(self):
        level_display = self.current_level or 'Todas'
        banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║         🎯      PYTHON EXAM     🎯                    ║
║                                                       ║
║         Nível: {Colors.YELLOW}{level_display:<25}{Colors.CYAN}  ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝
{Colors.END}"""
        print(banner)

    def print_menu(self):
        menu = f"""
{Colors.WHITE}Selecione o nível do exam:{Colors.END}
    {Colors.GREEN}[1]{Colors.END} {Colors.GREEN}Start{Colors.END}  - Iniciar o exam (todas as questões)

    {Colors.BLUE}[2]{Colors.END} {Colors.BLUE}Verifier{Colors.END} - Verificar questão atual
    {Colors.MAGENTA}[3]{Colors.END} {Colors.MAGENTA}Sair{Colors.END}
"""
        print(menu)

    def get_questions_by_level(self, level):
        """Retorna todas as questões disponíveis para um nível"""
        questions = []

        if level is None:
            search_paths = [p for p in self.questions_path.iterdir() if p.is_dir()]
        else:
            # Primeiro, tenta o layout antigo: questions/<level>/*
            level_path = self.questions_path / level.lower()
            if level_path.exists():
                search_paths = [p for p in level_path.iterdir() if p.is_dir()]
            else:
                # Novo layout: todas as questões em questions/<question_folder>
                search_paths = [p for p in self.questions_path.iterdir() if p.is_dir()]

        for folder in search_paths:
            question_txt = folder / "question.txt"
            solution_py = folder / "solution.py"
            if question_txt.exists() and solution_py.exists():
                questions.append({
                    'name': folder.name,
                    'path': folder,
                    'question_file': question_txt,
                    'solution_file': solution_py
                })

        return questions

    def select_level(self):
        """Permite ao usuário selecionar o nível do exam"""
        self.clear_screen()
        self.print_banner()
        self.print_menu()

        choice = input(f"{Colors.CYAN}>>> {Colors.END}").strip()

        if choice == '1':
            self.current_level = None
            self.start_exam()
        elif choice == '2':
            self.verify_current()
        elif choice == '3':
            print(f"\n{Colors.YELLOW}Até logo! 👋{Colors.END}\n")
            sys.exit(0)
        else:
            print(f"\n{Colors.RED}Opção inválida!{Colors.END}")
            input(f"\n{Colors.CYAN}Pressione ENTER para continuar...{Colors.END}")
            self.select_level()

    def start_exam(self):
        """Inicia o exam para o nível selecionado"""
        self.clear_screen()
        questions = self.get_questions_by_level(self.current_level)

        if not questions:
            level_display = self.current_level or 'Todas'
            print(f"\n{Colors.RED}✗ Nenhuma questão encontrada para: {level_display}{Colors.END}")
            print(f"{Colors.YELLOW}  Adicione questões na pasta questions/{Colors.END}")
            input(f"\n{Colors.CYAN}Pressione ENTER para voltar...{Colors.END}")
            self.select_level()
            return

        required = len(questions)

        level_display = (self.current_level or 'Todas').upper()
        print(f"\n{Colors.GREEN}{Colors.BOLD}╔═══════════════════════════════════════════════════════╗{Colors.END}")
        print(f"{Colors.GREEN}{Colors.BOLD}║            INICIANDO EXAM - {level_display:^11}             ║{Colors.END}")
        print(f"{Colors.GREEN}{Colors.BOLD}╠═══════════════════════════════════════════════════════╣{Colors.END}")
        print(f"{Colors.GREEN}{Colors.BOLD}║  Você precisará resolver {required} questões!{'':13} ║{Colors.END}")
        print(f"{Colors.GREEN}{Colors.BOLD}║  Questões disponíveis: {len(questions):<21} ║{Colors.END}")
        print(f"{Colors.GREEN}{Colors.BOLD}╚═══════════════════════════════════════════════════════╝{Colors.END}")

        input(f"\n{Colors.CYAN}Pressione ENTER para sortear a primeira questão...{Colors.END}")

        self.used_questions = random.sample(questions, min(required, len(questions)))

        if self.rendu_path.exists():
            shutil.rmtree(self.rendu_path)
        self.rendu_path.mkdir(exist_ok=True)

        self.next_question()

    def next_question(self):
        """Mostra a próxima questão ou заверша o exam"""
        if not self.used_questions:
            print(f"\n{Colors.RED}✗ Nenhuma questão disponível!{Colors.END}")
            return

        self.current_question = self.used_questions.pop(0)
        q_name = self.current_question['name']

        rendu_q_path = self.rendu_path / q_name
        if rendu_q_path.exists():
            shutil.rmtree(rendu_q_path)
        rendu_q_path.mkdir(parents=True)

        shutil.copy(self.current_question['question_file'], rendu_q_path / "question.txt")

        self.create_solution_template(rendu_q_path)

        self.clear_screen()
        self.show_question()

    def create_solution_template(self, path):
        """Cria o template inicial do solution.py com
        a assinatura correta da função"""
        q_name = path.name

        func_name, func_signature = self.extract_function_signature()

        template = f'''# Questão: {q_name}
# Resolva aqui!

{func_signature}:
    # Sua solução aqui
    pass

# Você pode testar aqui:
if __name__ == "__main__":
    # Exemplo de teste:
    # print({func_name}(...))
    pass
'''
        with open(path / "solution.py", 'w') as f:
            f.write(template)

    def extract_function_signature(self):
        """Extrai o nome e a assinatura completa
        da função da solução de referência"""
        try:
            with open(self.current_question['solution_file'], 'r') as f:
                content = f.read()

            import re

            match = re.search(r'(def\s+\w+\s*\([^)]*\)(?:\s*->\s*[^:]*)?)', content)
            if match:
                func_sig = match.group(1).strip()

                name_match = re.search(r'def\s+(\w+)\s*\(', func_sig)
                func_name = name_match.group(1) if name_match else "solution"
                return func_name, func_sig
        except:
            pass
        return "solution", "def solution(*args, **kwargs)"

    def show_question(self):
        """Mostra a questão atual"""
        self.print_banner()

        q_name = self.current_question['name']
        q_path = self.rendu_path / q_name

        with open(q_path / "question.txt", 'r') as f:
            question_text = f.read()

        remaining = len(self.used_questions) + 1

        print(f"{Colors.MAGENTA}{Colors.BOLD}┌───────────────────────────────────────────────────────┐{Colors.END}")
        print(f"{Colors.MAGENTA}{Colors.BOLD}│  Questão: {q_name:<42} │{Colors.END}")
        print(f"{Colors.MAGENTA}{Colors.BOLD}│  Restantes: {remaining} questão(ões){' ' * 31} │{Colors.END}")
        print(f"{Colors.MAGENTA}{Colors.BOLD}└───────────────────────────────────────────────────────┘{Colors.END}")
        print()
        print(question_text)
        print()

        print(f"{Colors.CYAN}📁 Sua solução está em: rendu/{q_name}/solution.py{Colors.END}")

        self.show_actions()

    def show_actions(self):
        """Mostra as ações possíveis"""
        actions = f"""
{Colors.WHITE}Ações:{Colors.END}

  {Colors.GREEN}[1]{Colors.END} {Colors.GREEN}Verificar{Colors.END} - Testar sua solução
  {Colors.BLUE}[2]{Colors.END} {Colors.BLUE}Abrir pasta{Colors.END} - Mostrar caminho da pasta rendu
  {Colors.YELLOW}[3]{Colors.END} {Colors.YELLOW}Ver enunciado{Colors.END} - Mostrar enunciado novamente
    {Colors.MAGENTA}[4]{Colors.END} {Colors.MAGENTA}Menu{Colors.END} - Voltar ao menu principal
    {Colors.CYAN}[5]{Colors.END} {Colors.CYAN}Next{Colors.END} - Pular para a próxima questão

    {Colors.RED}[0]{Colors.END} {Colors.RED}Sair do exam{Colors.END}
"""
        print(actions)

        choice = input(f"{Colors.CYAN}>>> {Colors.END}").strip()

        if choice == '1':
            self.verify_current()
        elif choice == '2':
            self.open_rendu_folder()
        elif choice == '3':
            self.show_question()
        elif choice == '4':
            self.select_level()
        elif choice == '5':
            self.skip_current()
        elif choice == '0':
            print(f"\n{Colors.YELLOW}Saindo do exam...{Colors.END}\n")
            sys.exit(0)
        else:
            self.show_question()

    def skip_current(self):
        """Pula a questão atual e passa para a próxima"""
        if not self.current_question:
            print(f"\n{Colors.RED}✗ Nenhuma questão ativa para pular!{Colors.END}")
            input(f"\n{Colors.CYAN}Pressione ENTER para voltar...{Colors.END}")
            self.show_question()
            return

        # Remove possível pasta rendu da questão atual (opcional)
        rendu_q_path = self.rendu_path / self.current_question['name']
        if rendu_q_path.exists():
            try:
                shutil.rmtree(rendu_q_path)
            except Exception:
                pass

        if self.used_questions:
            self.next_question()
        else:
            self.exam_completed()

    def verify_current(self):
        """Verifica se a solução atual está correta"""
        if not self.current_question:
            print(f"\n{Colors.RED}✗ Nenhuma questão ativa!{Colors.END}")
            input(f"\n{Colors.CYAN}Pressione ENTER para voltar...{Colors.END}")
            self.select_level()
            return

        q_name = self.current_question['name']
        solution_path = self.rendu_path / q_name / "solution.py"

        if not solution_path.exists():
            print(f"\n{Colors.RED}✗ Arquivo solution.py não encontrado!{Colors.END}")
            input(f"\n{Colors.CYAN}Pressione ENTER para voltar...{Colors.END}")
            self.show_question()
            return

        self.clear_screen()
        self.print_banner()

        print(f"\n{Colors.CYAN}🔍 Verificando solução para: {q_name}{Colors.END}")
        print(f"{Colors.CYAN}{'─' * 55}{Colors.END}\n")

        result, trace_ok, trace_error = self.run_tests(q_name, solution_path)
        self.save_trace(q_name, trace_ok, trace_error, result)

        trace_folder = self.traces_path / q_name
        if trace_ok and result:
            print(f"\n{Colors.GREEN}✓ Trace OK salvo em: {trace_folder / 'trace_ok.txt'}{Colors.END}")
        if trace_error and not result:
            print(f"\n{Colors.RED}✗ Trace ERROR salvo em: {trace_folder / 'trace_error.txt'}{Colors.END}")

        if result:
            print(f"\n{Colors.GREEN}{Colors.BOLD}╔═══════════════════════════════════════════════════════╗{Colors.END}")
            print(f"{Colors.GREEN}{Colors.BOLD}║              ✅ PASSED! PARABÉNS!                      ║{Colors.END}")
            print(f"{Colors.GREEN}{Colors.BOLD}╚═══════════════════════════════════════════════════════╝{Colors.END}")
            print(f"\n{Colors.GREEN}Você acertou! Próxima questão...{Colors.END}")
            input(f"\n{Colors.CYAN}Pressione ENTER para continuar...{Colors.END}")

            if self.used_questions:
                self.next_question()
            else:
                self.exam_completed()
        else:
            print(f"\n{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════╗{Colors.END}")
            print(f"{Colors.RED}{Colors.BOLD}║                    ❌ FALHOU!                        ║{Colors.END}")
            print(f"{Colors.RED}{Colors.BOLD}╚═══════════════════════════════════════════════════════╝{Colors.END}")
            print(f"\n{Colors.YELLOW}Revise sua solução e tente novamente.{Colors.END}")
            input(f"\n{Colors.CYAN}Pressione ENTER para voltar...{Colors.END}")
            self.show_question()

    def run_tests(self, q_name, solution_path):
        """Roda os testes para a questão com traces separados"""
        trace_ok = []
        trace_error = []

        trace_error.append(f"Questão: {q_name}")
        trace_error.append(f"Solução: {solution_path}")
        trace_error.append("")

        added_path = str(solution_path.parent)
        sys.path.insert(0, added_path)

        try:
            with open(solution_path, 'r') as f:
                user_code = f.read()

            ref_solution = self.current_question['solution_file']
            with open(ref_solution, 'r') as f:
                ref_code = f.read()

            import re
            func_match = re.search(r'def\s+(\w+)\s*\(', ref_code)
            if not func_match:
                message = "✗ Não consegui encontrar a função de referência!"
                print(f"{Colors.RED}{message}{Colors.END}")
                trace_error.append(message)
                return False, trace_ok, trace_error

            func_name = func_match.group(1)
            trace_error.append(f"Função de referência: {func_name}")
            trace_error.append("")

            ref_namespace = {}
            exec(compile(ref_code, ref_solution, 'exec'), ref_namespace)

            user_namespace = {}
            exec(compile(user_code, solution_path, 'exec'), user_namespace)

            if func_name not in user_namespace:
                message = f"✗ Função '{func_name}' não encontrada na sua solução!"
                print(f"{Colors.RED}{message}{Colors.END}")
                print(f"{Colors.YELLOW}  Certifique-se de definir: def {func_name}(...){Colors.END}")
                trace_error.append(message)
                trace_error.append(f"Esperado: def {func_name}(...)")
                return False, trace_ok, trace_error

            user_func = user_namespace[func_name]

            test_file = self.current_question['path'] / "tests.py"
            if not test_file.exists():
                message = "✗ Arquivo tests.py não encontrado!"
                print(f"{Colors.RED}{message}{Colors.END}")
                trace_error.append(message)
                return False, trace_ok, trace_error

            test_namespace = {}
            exec(compile(open(test_file).read(), test_file, 'exec'), test_namespace)

            tests = test_namespace.get('TESTS', [])
            passed = 0
            failed = 0

            for i, test in enumerate(tests, 1):
                args = test.get('args', [])
                kwargs = test.get('kwargs', {})
                expected = test.get('expected')

                trace_line = f"Teste {i}:"
                trace_ok.append(trace_line)
                trace_error.append(trace_line)

                trace_line = f"  Args: {args}"
                trace_ok.append(trace_line)
                trace_error.append(trace_line)

                trace_line = f"  Kwargs: {kwargs}"
                trace_ok.append(trace_line)
                trace_error.append(trace_line)

                trace_line = f"  Esperado: {expected}"
                trace_ok.append(trace_line)
                trace_error.append(trace_line)

                try:
                    result = user_func(*args, **kwargs)

                    if result == expected:
                        print(f"{Colors.GREEN}✓ Teste {i}: PASSED{Colors.END}")
                        trace_ok.append(f"  Recebido: {result}")
                        trace_ok.append(f"  Status: ✓ PASSED")
                        trace_ok.append("")
                        passed += 1
                    else:
                        print(f"{Colors.RED}✗ Teste {i}: FAILED{Colors.END}")
                        print(f"  {Colors.WHITE}Esperado: {expected}{Colors.END}")
                        print(f"  {Colors.WHITE}Recebido: {result}{Colors.END}")
                        trace_error.append(f"  Recebido: {result}")
                        trace_error.append(f"  Status: ✗ FAILED")
                        trace_error.append("")
                        failed += 1
                except Exception as e:
                    print(f"{Colors.RED}✗ Teste {i}: ERROR - {e}{Colors.END}")
                    trace_error.append(f"  Recebido: ERROR - {e}")
                    trace_error.append(f"  Status: ✗ ERROR")
                    trace_error.append("")
                    failed += 1

            trace_ok.append(f"Resultados: {passed} passed, {failed} failed")
            trace_error.append(f"Resultados: {passed} passed, {failed} failed")

            return failed == 0, trace_ok, trace_error

        except Exception as e:
            message = f"✗ Erro ao executar testes: {e}"
            print(f"{Colors.RED}{message}{Colors.END}")
            import traceback
            traceback.print_exc()
            trace_error.append(message)
            return False, trace_ok, trace_error

        finally:
            if added_path in sys.path:
                try:
                    sys.path.remove(added_path)
                except ValueError:
                    pass

    def save_trace(self, q_name, trace_ok, trace_error, result):
        """Salva traces separados em trace_ok.txt e trace_error.txt"""
        trace_folder = self.traces_path / q_name
        trace_folder.mkdir(parents=True, exist_ok=True)

        if trace_ok and result:
            trace_file_ok = trace_folder / "trace_ok.txt"
            with open(trace_file_ok, 'w') as f:
                f.write("\n".join(trace_ok))

        if trace_error and not result:
            trace_file_error = trace_folder / "trace_error.txt"
            with open(trace_file_error, 'w') as f:
                f.write("\n".join(trace_error))

    def exam_completed(self):
        """Chamado quando todas as questões são completadas"""
        self.clear_screen()

        print(f"""
{Colors.GREEN}{Colors.BOLD}
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║         🎉 PARABÉNS! EXAM COMPLETO! 🎉               ║
║                                                       ║
║         Você completou todas as questões do          ║
║         nível {self.current_level}!                            ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝
{Colors.END}
""")
        print(f"{Colors.CYAN}Suas soluções estão em: rendu/{Colors.END}\n")

        input(f"{Colors.CYAN}Pressione ENTER para voltar ao menu...{Colors.END}")
        self.current_level = None
        self.current_question = None
        self.used_questions = []
        self.select_level()

    def open_rendu_folder(self):
        """Mostra o caminho da pasta rendu"""
        print(f"\n{Colors.CYAN}📁 Pasta rendu:{Colors.END}")
        print(f"   {self.rendu_path}")
        print(f"\n{Colors.YELLOW}Abra outro terminal e edite o arquivo:{Colors.END}")
        print(f"   {self.rendu_path / self.current_question['name'] / 'solution.py'}")
        print()
        input(f"{Colors.CYAN}Pressione ENTER para voltar...{Colors.END}")
        self.show_question()


def main():
    exam = Exam()
    exam.select_level()


if __name__ == "__main__":
    main()
