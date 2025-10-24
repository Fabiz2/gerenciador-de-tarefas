Construindo um Projeto Ágil no GitHub: Da Gestão ao Controle de Qualidade
Descrição do Projeto
Este projeto foi desenvolvido para a TechFlow Solutions, uma empresa fictícia especializada em soluções de software, contratada por uma startup de logística. O objetivo é criar um sistema de gerenciamento de tarefas baseado em metodologias ágeis, permitindo acompanhar o fluxo de trabalho em tempo real, priorizar tarefas críticas e monitorar o desempenho da equipe. A aplicação web implementada utiliza Flask e oferece funcionalidades básicas de CRUD (Create, Read, Update, Delete) para gerenciamento de tarefas.
Objetivo
Desenvolver um sistema funcional que simule o ciclo de vida de um projeto ágil, utilizando o GitHub para organização, versionamento, controle de qualidade e gestão de mudanças, atendendo às necessidades da startup cliente.
Metodologia Utilizada
Foi adotada a metodologia Kanban, implementada por meio da aba Projects do GitHub. O quadro Kanban organiza as tarefas nas colunas A Fazer, Em Progresso e Concluído, promovendo uma gestão visual e flexível do fluxo de trabalho, com adaptação contínua às mudanças de escopo.
Instruções para Executar o Sistema

Pré-requisitos:

Instale o Python 3.x.
Instale as dependências com pip install flask pytest.


Clonar o Repositório:

Execute git clone <URL_DO_REPOSITÓRIO>.


Executar a Aplicação:

Navegue até o diretório /src e rode python app.py.
Acesse o sistema em http://127.0.0.1:5000/ no navegador.


Testes Automatizados:

Execute pytest no diretório /tests para rodar os testes unitários.



Estrutura do Repositório

/src: Contém o arquivo app.py com a lógica principal.
/tests: Contém os arquivos de testes automatizados.
/docs: Documentação adicional (ex.: diagramas UML).
/static: Arquivos CSS (ex.: style.css).
/templates: Arquivos HTML (ex.: index.html).

Quadro Kanban
O projeto utiliza a aba Projects do GitHub para criar um quadro Kanban com pelo menos 10 cards distribuídos nas colunas A Fazer, Em Progresso e Concluído. Link direto para o quadro Kanban. Exemplo de tarefas:

A Fazer: "Configurar repositório".
Em Progresso: "Implementar testes".
Concluído: "Desenvolver CRUD básico".

Histórico de Commits
Os commits são realizados com mensagens descritivas e estruturadas, como:

"Inicializar projeto com Flask e estrutura básica".
"Adicionar funcionalidade de CRUD para tarefas".
"Configurar pipeline de CI com GitHub Actions".O repositório contém pelo menos 10 commits distribuídos ao longo do desenvolvimento.

Controle de Qualidade
Um pipeline básico foi configurado usando GitHub Actions para executar testes automatizados (PyTest). Os testes validam a criação de tarefas (ex.: título não vazio) e a exclusão de tarefas (ex.: remoção correta da lista), garantindo a funcionalidade básica do sistema e a qualidade do código.
Gestão de Mudanças
Foi simulada uma alteração no escopo com a adição da funcionalidade de notificação de tarefas pendentes por mais de 7 dias, justificada pela necessidade de maior proatividade da equipe. Essa mudança foi simulada como parte do requisito de gestão de mudanças do projeto, registrada no quadro Kanban com um novo card e atualizada neste README.
Licença
Este projeto está sob a licença MIT. Adicione um arquivo chamado LICENSE na raiz do repositório (o GitHub pode gerá-lo automaticamente ao selecionar a licença MIT).
