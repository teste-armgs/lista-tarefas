# Proposta do Projeto: Aplicativo de Tarefas com Prioridades.

   O objetivo deste projeto é desenvolver um aplicativo de lista de tarefas com prioridade que permita aos usuários gerenciarem eficientemente suas atividades diárias. O aplicativo funcionará inteiramente no terminal, permitindo que os usuários adicionem, priorizem e acompanhem o progresso de suas tarefas.

# Funcionalidades Principais
   **Adição de Tarefas:** Os usuários poderão adicionar novas tarefas à lista, fornecendo uma descrição da tarefa.

   **Definição de Prioridades:** Cada tarefa poderá ser atribuída a uma prioridade, como alta, média ou baixa.

   **Marcação de Tarefas Concluídas:** Os usuários poderão marcar as tarefas como concluídas quando forem finalizadas.

   **Filtragem de Tarefas:** Os usuários poderão filtrar as tarefas com base em sua prioridade.

   **Visualização de Progresso:** O aplicativo fornecerá aos usuários um resumo do progresso de suas tarefas, incluindo o número de tarefas concluídas e pendentes.

# Tecnologias Utilizadas
   As tecnologias empregadas neste projeto serão o Visual Studio Code (VS Code) como ambiente de desenvolvimento, linguagem de programação Python para implementar a lógica do aplicativo, a biblioteca padrão de testes unitários do Python “unittest”, Docker para implantar o projeto dentro de containers virtuais, MySQL para armazenar e gerenciar os dados do BD e o GitHub para colaboração entre os membros da equipe e integração do código.

   Com essas ferramentas, criaremos uma solução simples e eficaz para ajudar os usuários a gerenciar suas tarefas diárias de maneira organizada e priorizada. O aplicativo será executado no terminal.

# Lista Preliminar de Casos de Teste
   **Adição de Tarefas:** 
   - Testar se é possível adicionar uma nova tarefa à lista.
   - Verificar se a tarefa adicionada está corretamente registrada no sistema.

   **Definição de Prioridades:**
   - Verificar se é possível definir uma prioridade alta para uma tarefa.
   - Testar se é possível definir uma prioridade média para uma tarefa.
   - Verificar se é possível definir uma prioridade baixa para uma tarefa.

   **Marcação de Tarefas Concluídas:**
   - Testar se é possível marcar uma tarefa como concluída.
   - Verificar se a tarefa marcada como concluída é removida da lista de tarefas pendentes.

   **Filtragem de Tarefas:**
   - Verificar se é possível filtrar as tarefas por prioridade alta.
   - Testar se é possível filtrar as tarefas por prioridade média.
   - Verificar se é possível filtrar as tarefas por prioridade baixa.

   **Visualização de Progresso:**
   - Testar se é possível visualizar o número total de tarefas concluídas.
   - Verificar se é possível visualizar o número total de tarefas pendentes.
   - Testar se é possível visualizar um resumo do progresso das tarefas.

# Abordagem de Desenvolvimento

**Planejamento e Análise:** Inicialmente, dedicamos tempo para entender os requisitos do projeto e definir as funcionalidades essenciais do aplicativo.

**Implementação Básica:** Começamos implementando a funcionalidade básica de adição de tarefas à lista e realizando testes para verificar.

**Testes e Refatoração:** Durante todo o processo de desenvolvimento, dedicamos tempo à escrita de testes automatizados. Realizamos testes unitários e de integração regularmente, identificando e corrigindo problemas à medida que surgiam.

**Estruturação dos Casos de Teste:** Um dos principais desafios enfrentados foi estruturar os casos de teste antes do desenvolvimento do programa. Definir claramente o que queríamos testar e como garantir a cobertura adequada das funcionalidades.