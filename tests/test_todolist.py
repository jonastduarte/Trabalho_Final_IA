import unittest
from datetime import datetime
import sys
import os

# Adiciona o diretório src ao path para os testes enxergarem o todolist.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from todolist import ToDoList, Task

class TestToDoList(unittest.TestCase):
    """Testes unitários para a classe ToDoList."""

    def setUp(self):
        """Prepara o ambiente antes de cada teste."""
        self.todo_list = ToDoList()

    def test_add_task_success(self):
        """Verifica se adiciona uma tarefa corretamente."""
        task = self.todo_list.add_task("Estudar Python")
        self.assertEqual(task.description, "Estudar Python")
        self.assertEqual(task.status, "Pendente")
        self.assertEqual(len(self.todo_list.list_all_tasks()), 1)

    def test_add_task_empty_description(self):
        """Verifica se lança exceção com descrição vazia."""
        with self.assertRaises(ValueError):
            self.todo_list.add_task("")
        with self.assertRaises(ValueError):
            self.todo_list.add_task("   ")

    def test_remove_task_success(self):
        """Verifica se a remoção de tarefa existente funciona."""
        task = self.todo_list.add_task("Teste de remoção")
        self.assertTrue(self.todo_list.remove_task(task.task_id))
        self.assertEqual(len(self.todo_list.list_all_tasks()), 0)

    def test_remove_task_not_found(self):
        """Verifica se a remoção falha com ID inexistente."""
        with self.assertRaises(KeyError):
            self.todo_list.remove_task(999)

    def test_mark_task_completed(self):
        """Verifica se uma tarefa pode ser marcada como concluída."""
        task = self.todo_list.add_task("Teste de conclusão")
        self.assertTrue(self.todo_list.mark_task_completed(task.task_id))
        
        updated_tasks = self.todo_list.list_all_tasks()
        self.assertEqual(updated_tasks[0].status, "Concluída")
        self.assertIsInstance(updated_tasks[0].completed_at, datetime)

    def test_mark_task_completed_not_found(self):
        """Verifica se falha ao concluir tarefa inexistente."""
        with self.assertRaises(KeyError):
            self.todo_list.mark_task_completed(999)

    def test_list_all_tasks(self):
        """Verifica listar todas as tarefas corretamente."""
        self.todo_list.add_task("Tarefa 1")
        self.todo_list.add_task("Tarefa 2")
        self.assertEqual(len(self.todo_list.list_all_tasks()), 2)

    def test_list_completed_and_pending_tasks(self):
        """Verifica filtros de concluídas e pendentes."""
        t1 = self.todo_list.add_task("Tarefa 1")
        t2 = self.todo_list.add_task("Tarefa 2")
        t3 = self.todo_list.add_task("Tarefa 3")
        
        self.todo_list.mark_task_completed(t1.task_id)
        
        completed = self.todo_list.list_completed_tasks()
        pending = self.todo_list.list_pending_tasks()
        
        self.assertEqual(len(completed), 1)
        self.assertEqual(completed[0].task_id, t1.task_id)
        
        self.assertEqual(len(pending), 2)
        self.assertEqual(pending[0].task_id, t2.task_id)
        self.assertEqual(pending[1].task_id, t3.task_id)

    def test_add_task_with_special_characters(self):
        """[Functional] Verifica adição de tarefas com caracteres especiais e longas."""
        desc = "Task@! #123 com chars $ % & * () - e texto longo " * 5
        task = self.todo_list.add_task(desc)
        self.assertEqual(task.description, desc.strip())

    def test_mark_task_completed_twice(self):
        """[Edge Case] Tentar marcar como concluída uma tarefa que já está concluída."""
        task = self.todo_list.add_task("Estudar LLMs")
        self.todo_list.mark_task_completed(task.task_id)
        
        # Guardar tempo da primeira conclusão
        first_completed_at = task.completed_at
        
        # Tentar concluir de novo
        self.todo_list.mark_task_completed(task.task_id)
        
        # A data de conclusão não deve mudar e o status continua "Concluída"
        self.assertEqual(task.status, "Concluída")
        self.assertEqual(task.completed_at, first_completed_at)

    def test_high_volume_and_accuracy(self):
        """[Edge Case] Teste de carga: criar 1000 tarefas sucessivas e verificar integridade."""
        for i in range(1000):
            self.todo_list.add_task(f"Task de carga {i}")
            
        all_tasks = self.todo_list.list_all_tasks()
        self.assertEqual(len(all_tasks), 1000)
        
        # Concluir os múltiplos de 10
        for i in range(0, 1000, 10):
            self.todo_list.mark_task_completed(all_tasks[i].task_id)
            
        completed = self.todo_list.list_completed_tasks()
        self.assertEqual(len(completed), 100)
        self.assertEqual(len(self.todo_list.list_pending_tasks()), 900)

    def test_functional_user_workflow(self):
        """[Functional] Simula um fluxo de usuário longo e complexo na plataforma."""
        # 1. Usuário entra e cria 3 tarefas
        t1 = self.todo_list.add_task("Comprar leite")
        t2 = self.todo_list.add_task("Aprender testes de Mutação com IA")
        t3 = self.todo_list.add_task("Escrever prompt exaustivo do Copilot")
        
        # 2. Conclui as duas primeiras
        self.todo_list.mark_task_completed(t1.task_id)
        self.todo_list.mark_task_completed(t2.task_id)
        
        # 3. Lista verifica se tem 2 concluidas e 1 pendente
        self.assertEqual(len(self.todo_list.list_completed_tasks()), 2)
        self.assertEqual(len(self.todo_list.list_pending_tasks()), 1)
        
        # 4. Remove a tarefa que estava concluida (t1) e a pendente (t3)
        self.todo_list.remove_task(t1.task_id)
        self.todo_list.remove_task(t3.task_id)
        
        # 5. Validação final: deve sobrar apenas a t2 (Concluída)
        final_tasks = self.todo_list.list_all_tasks()
        self.assertEqual(len(final_tasks), 1)
        self.assertEqual(final_tasks[0].task_id, t2.task_id)
        self.assertEqual(final_tasks[0].status, "Concluída")


if __name__ == '__main__':
    print("=" * 70)
    print("Executando Suíte de Testes: ToDoList App")
    print("=" * 70)
    # verbosity=2 gera um relatório detalhado com o nome de cada teste e seu status
    unittest.main(verbosity=2)
