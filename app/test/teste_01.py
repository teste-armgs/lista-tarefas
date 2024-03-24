import unittest
from main import ListTask

class TestCriarTarefas(unittest.TestCase):
    def setUp(self):
        self.list_task = ListTask()

    def test_criar_tarefa(self):
        self.list_task.limpar_tarefas()
        self.list_task.adicionar("Tarefa de teste", "2", "Pendente")
        tarefas = self.list_task.exibir('4')
        self.assertEqual(len(tarefas), 1)
        self.assertEqual(tarefas[0]['nome'], "Tarefa de teste")
        self.assertEqual(tarefas[0]['prioridade'], 2)
        self.assertEqual(tarefas[0]['status'], "Pendente")

if __name__ == '__main__':
    unittest.main()
