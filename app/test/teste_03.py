import unittest
from main import ListTask

class TestConcluirTarefa(unittest.TestCase):
    def setUp(self):
        self.list_task = ListTask()

    def test_concluir_tarefa(self):
        self.list_task.limpar_tarefas()
        self.list_task.adicionar("Tarefa de teste", "2", "Pendente")
        self.list_task.finalizar(1)
        tarefas_concluidas = self.list_task.exibir('4')
        self.assertEqual(tarefas_concluidas[0]['status'], "Concluído")

if __name__ == '__main__':
    unittest.main()
