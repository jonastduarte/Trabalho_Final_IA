import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from typing import List, Optional

class Task:
    """Representa uma tarefa individual."""
    def __init__(self, task_id: int, description: str):
        self.task_id: int = task_id
        self.description: str = description
        self.status: str = "Pendente"
        self.created_at: datetime = datetime.now()
        self.completed_at: Optional[datetime] = None

    def mark_completed(self) -> None:
        """Marca a tarefa como concluída."""
        if self.status != "Concluída":
            self.status = "Concluída"
            self.completed_at = datetime.now()

    def __str__(self) -> str:
        """Retorna a representação em string da tarefa."""
        status_text = f"[{self.status}]"
        date_text = self.created_at.strftime('%Y-%m-%d %H:%M')
        return f"{self.task_id} | {status_text} {self.description} (Criada: {date_text})"


class ToDoList:
    """Gerenciador de uma lista de tarefas (ToDo List)."""
    
    def __init__(self):
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, description: str) -> Task:
        """Adiciona uma nova tarefa à lista.
        
        Args:
            description (str): A descrição da tarefa.
            
        Returns:
            Task: O objeto da tarefa criada.
            
        Raises:
            ValueError: Se a descrição for vazia.
        """
        if not description or not description.strip():
            raise ValueError("A descrição da tarefa não pode ser vazia.")
            
        new_task = Task(self._next_id, description.strip())
        self._tasks.append(new_task)
        self._next_id += 1
        return new_task

    def remove_task(self, task_id: int) -> bool:
        """Remove uma tarefa existente pelo seu ID.
        
        Args:
            task_id (int): ID da tarefa a ser removida.
            
        Returns:
            bool: True se removida com sucesso.
            
        Raises:
            KeyError: Se o ID da tarefa não for encontrado.
        """
        for i, task in enumerate(self._tasks):
            if task.task_id == task_id:
                del self._tasks[i]
                return True
        raise KeyError(f"Tarefa com ID {task_id} não encontrada.")

    def mark_task_completed(self, task_id: int) -> bool:
        """Marca uma tarefa como concluída pelo seu ID.
        
        Args:
            task_id (int): ID da tarefa.
            
        Returns:
            bool: True se marcada com sucesso.
            
        Raises:
            KeyError: Se o ID da tarefa não for encontrado.
        """
        for task in self._tasks:
            if task.task_id == task_id:
                task.mark_completed()
                return True
        raise KeyError(f"Tarefa com ID {task_id} não encontrada.")

    def list_all_tasks(self) -> List[Task]:
        """Lista todas as tarefas."""
        return self._tasks.copy()

    def list_completed_tasks(self) -> List[Task]:
        """Lista apenas as tarefas concluídas."""
        return [task for task in self._tasks if task.status == "Concluída"]

    def list_pending_tasks(self) -> List[Task]:
        """Lista apenas as tarefas pendentes."""
        return [task for task in self._tasks if task.status == "Pendente"]


class ToDoApp(tk.Tk):
    """Interface Gráfica do aplicativo ToDoList utilizando Tkinter."""
    
    def __init__(self, todo_list: ToDoList):
        super().__init__()
        self.todo_list = todo_list
        
        self.title("Gerenciador de Tarefas (App ToDoList)")
        self.geometry("600x500")
        self.configure(padx=10, pady=10)
        
        self._create_widgets()
        self._refresh_list()

    def _create_widgets(self) -> None:
        """Cria e organiza os widgets na janela principal."""
        # Top frame for adding tasks
        frame_add = ttk.Frame(self)
        frame_add.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(frame_add, text="Nova Tarefa:").pack(side=tk.LEFT, padx=(0, 5))
        self.entry_desc = ttk.Entry(frame_add)
        self.entry_desc.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.entry_desc.bind("<Return>", lambda e: self._add_task())
        
        ttk.Button(frame_add, text="Adicionar", command=self._add_task).pack(side=tk.LEFT)

        # Filters frame
        frame_filters = ttk.Frame(self)
        frame_filters.pack(fill=tk.X, pady=(0, 5))
        
        self.filter_var = tk.StringVar(value="Todas")
        ttk.Radiobutton(frame_filters, text="Todas", variable=self.filter_var, value="Todas", command=self._refresh_list).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Radiobutton(frame_filters, text="Pendentes", variable=self.filter_var, value="Pendentes", command=self._refresh_list).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Radiobutton(frame_filters, text="Concluídas", variable=self.filter_var, value="Concluídas", command=self._refresh_list).pack(side=tk.LEFT)

        # Listbox for tasks with scrollbar
        frame_list = ttk.Frame(self)
        frame_list.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        scrollbar = ttk.Scrollbar(frame_list)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.listbox = tk.Listbox(frame_list, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set, font=("Consolas", 10))
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox.yview)

        # Bottom frame for actions
        frame_actions = ttk.Frame(self)
        frame_actions.pack(fill=tk.X)
        
        ttk.Button(frame_actions, text="Concluir Selecionada", command=self._complete_task).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(frame_actions, text="Excluir Selecionada", command=self._remove_task).pack(side=tk.LEFT)

    def _add_task(self) -> None:
        """Rotina para adicionar tarefa a partir da interface."""
        desc = self.entry_desc.get()
        try:
            self.todo_list.add_task(desc)
            self.entry_desc.delete(0, tk.END)
            self._refresh_list()
        except ValueError as e:
            messagebox.showwarning("Aviso", str(e))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro inesperado: {e}")

    def _get_selected_task_id(self) -> Optional[int]:
        """Obtém o ID da tarefa atualmente selecionada na listbox."""
        selection = self.listbox.curselection()
        if not selection:
            return None
            
        item_text = self.listbox.get(selection[0])
        # The ID is the first part of the string before the pipe symbol
        try:
            task_id_str = item_text.split(" | ", 1)[0]
            return int(task_id_str)
        except (ValueError, IndexError):
            return None

    def _complete_task(self) -> None:
        """Rota para concluir a tarefa selecionada."""
        task_id = self._get_selected_task_id()
        if task_id is None:
            messagebox.showinfo("Informação", "Por favor, selecione uma tarefa para concluir.")
            return
            
        try:
            self.todo_list.mark_task_completed(task_id)
            self._refresh_list()
        except KeyError as e:
            messagebox.showerror("Erro", str(e))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao concluir: {e}")

    def _remove_task(self) -> None:
        """Rotina para remover a tarefa selecionada."""
        task_id = self._get_selected_task_id()
        if task_id is None:
            messagebox.showinfo("Informação", "Por favor, selecione uma tarefa para excluir.")
            return
            
        if messagebox.askyesno("Confirmação", "Deseja realmente excluir esta tarefa?"):
            try:
                self.todo_list.remove_task(task_id)
                self._refresh_list()
            except KeyError as e:
                messagebox.showerror("Erro", str(e))
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao excluir: {e}")

    def _refresh_list(self) -> None:
        """Atualiza a Listbox com base no filtro selecionado."""
        self.listbox.delete(0, tk.END)
        
        filter_type = self.filter_var.get()
        if filter_type == "Pendentes":
            tasks = self.todo_list.list_pending_tasks()
        elif filter_type == "Concluídas":
            tasks = self.todo_list.list_completed_tasks()
        else:
            tasks = self.todo_list.list_all_tasks()
            
        for task in tasks:
            self.listbox.insert(tk.END, str(task))
            if task.status == "Concluída":
                self.listbox.itemconfig(tk.END, {'fg': 'gray'})


if __name__ == "__main__":
    # Exemplo de uso exigido
    todo_manager = ToDoList()
    
    # Pré-populando para demonstração
    todo_manager.add_task("Estudar IA Generativa e LLMs")
    todo_manager.add_task("Configurar o Antigravity Gemini 3.1 Pro")
    todo_manager.add_task("Escrever o documento de Relatório")
    
    todo_manager.mark_task_completed(2)
    
    app = ToDoApp(todo_manager)
    app.mainloop()
