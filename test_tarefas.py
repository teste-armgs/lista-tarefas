import unittest
from main import ListTask

class Test_tarefas(unittest.TestCase):

    def setUp(self):
        self.list_task = ListTask()

    def test_criar_tarefas(self):
        self.list_task.adicionar("Tarefa de teste", "2", "Pendente")
        self.assertEqual(len(self.list_task.tarefas), 1)
        self.assertEqual(self.list_task.tarefas[0]['tarefa'], "Tarefa de teste")
        self.assertEqual(self.list_task.tarefas[0]['prioridade'], "2")
        self.assertEqual(self.list_task.tarefas[0]['status'], "Pendente")

    def test_filtrar_por_prioridade(self):
        self.list_task.adicionar("Tarefa de alta prioridade", "1", "Pendente")
        self.list_task.adicionar("Tarefa de baixa prioridade", "3", "Pendente")
        self.list_task.adicionar("Tarefa de média prioridade", "2", "Pendente")

        alta_prioridade = self.list_task.filtrar('1')
        self.assertEqual(len(alta_prioridade), 1)
        self.assertEqual(alta_prioridade[0]['prioridade'], '1')

        todas_as_prioridades = self.list_task.filtrar('4')
        self.assertEqual(len(todas_as_prioridades), 3)

    def test_concluir_terefa(self):
        self.list_task.adicionar("Tarefa de teste", "2", "Pendente")
        self.list_task.finalizar(0)
        self.assertEqual(self.list_task.tarefas[0]['status'], "Concluído")

    def test_filtrar_por_prioridade_invalida(self):
        self.list_task.adicionar("Tarefa de teste", "2", "Pendente")
        filtradas = self.list_task.filtrar('5')
        self.assertEqual(len(filtradas), 0)
