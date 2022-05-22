# TP-Engenharia-Software
Grupo: 

- Eduardo Diniz Mio - 2019006558
- Júlia Stancioli Paiva - 2020006680
- Thaís Andrade Reis Soares - 2020007031
- Lucas Augusto Leone - 2019006892

Funcional:
- Iremos criar um CRM (Sistema de cadastro de clientes)
- O objetivo é criar um ambiente que uma equipe de vendas possa se organizar a partir dos contatos dos clientes
- As principais funções são: 
  - CRUD para cliente, vendedor, administrador e processos; 
  - disposição dos processos em formato de kanban; 
  - listagem de processos através de filtros diversos (data de criação, vendedor responsável, nome do cliente, nome da empresa et cetera); 
  - criação de um modelo fixo de processo que pode ser editado pelo usuário; 
  - criação de tópicos extras e customização nos processos. 

Tecnologias: 
- Backend: Python (Django/Flask)
- Frontend: HTML, CSS e Bootstrap
- Banco de dados: MySQL

Divisão de tarefas:
- Todas as tarefas relacionadas à interface [Júlia e Thaís]
- Todas as tarefas relacionadas ao banco de dados [Lucas]
- Todas as tarefas relacionadas ao backend [Eduardo]

Tarefas técnicas:
- Preparar ambiente de desenvolvimento (VSCode e Dependências)
- Discutir e criar o esquema do banco de dados

História: Cadastrar novo cliente: Como administrador, quero poder cadastrar um novo cliente, a partir de um modelo padrão de campos a serem preenchidos.
Tarefas:
- Projetar e testar interface web
- Implementar interface web
- Criar e testar rota para cadastro de novo cliente
- Criar e testar rota para editar um cliente
- Criar e testar rota para remover um cliente

História: Listagem dos clientes: Como vendedor, quero ter acesso aos clientes cadastrados no crm.
Tarefas:
- Projetar e testar interface web
- Implementar interface web
- Criar e testar rota para listar os clientes existentes

História: Editar status do cliente: Como administrador, quero editar o status do cliente no funil. 
Tarefas:
- Projetar e testar interface web
- Implementar interface web
- Criar e testar rota para editar status do cliente no funil

História: Filtrar clientes: Como vendedor, quero poder filtrar os cards do crm por data de criação, vendedor responsável, nome do cliente e nome da empresa.
Tarefas:
- Projetar e testar interface web
- Implementar interface web
- Criar e testar rota para filtrar clientes por data de criação
- Criar e testar rotar para filtrar clientes por vendedor responsável
- Criar e testar rotar para filtrar clientes por nome do cliente
- Criar e testar rotar para filtrar clientes por nome da empresa
