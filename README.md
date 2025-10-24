Sistema de Gerenciamento de Tarefas Ágil
Sumário

Descrição do Projeto
Objetivo
Metodologia
Instruções para Executar
Estrutura do Repositório
Quadro Kanban
Histórico de Commits
Controle de Qualidade
Gestão de Mudanças
Reflexões
Licença

Descrição do Projeto
Este projeto foi desenvolvido para a TechFlow Solutions, uma empresa fictícia especializada em soluções de software, contratada por uma startup de logística. O objetivo é criar um sistema de gerenciamento de tarefas baseado em metodologias ágeis, permitindo acompanhar o fluxo de trabalho em tempo real, priorizar tarefas críticas e monitorar o desempenho da equipe. A aplicação web utiliza Flask e oferece funcionalidades básicas de CRUD (Create, Read, Update, Delete) para gerenciamento de tarefas.
Objetivo
Desenvolver um sistema funcional que simule o ciclo de vida de um projeto ágil, utilizando o GitHub para organização, versionamento, controle de qualidade e gestão de mudanças, atendendo às necessidades da startup cliente.
Metodologia
Foi adotada a metodologia Kanban, implementada via aba Projects do GitHub. O quadro organiza tarefas nas colunas A Fazer, Em Progresso e Concluído, promovendo uma gestão visual e flexível, com adaptação contínua às mudanças de escopo.
Instruções para Executar
Pré-requisitos

Instale o Python 3.9 ou superior.
Instale as dependências com: pip install -r requirements.txt (crie esse arquivo com flask e pytest).

Clonar o Repositório
git clone https://github.com/Fabiz2/gerenciador-de-tarefas.git

Executar a Aplicação

Navegue até o diretório /src e rode: python app.py.
Acesse em http://127.0.0.1:5000/ no navegador.
Aviso: Certifique-se de que a porta 5000 está livre.



Testes Automatizados
Execute pytest no diretório /tests para rodar os testes unitários.
Estrutura do Repositório

/src: Contém app.py com a lógica principal.
/tests: Arquivos de testes automatizados.
/docs: Documentação adicional (ex.: diagramas UML).
/static: Arquivos CSS (ex.: style.css).
/templates: Arquivos HTML (ex.: index.html).

Quadro Kanban
O projeto utiliza a aba Projects do GitHub para um quadro Kanban com pelo menos 10 cards distribuídos nas colunas A Fazer, Em Progresso e Concluído. Exemplos:

A Fazer: "Configurar repositório".
Em Progresso: "Implementar testes".
Concluído: "Desenvolver CRUD básico".Link direto para o quadro Kanban.

Histórico de Commits
Commits são descritivos e estruturados, com pelo menos 10 ao longo do desenvolvimento, como:

"Inicializar projeto com Flask e estrutura básica".
"Adicionar funcionalidade de CRUD para tarefas".
"Configurar pipeline de CI com GitHub Actions".

Controle de Qualidade
Um pipeline básico foi configurado com GitHub Actions para executar testes automatizados (PyTest), validando criação (título não vazio) e exclusão de tarefas.
Gestão de Mudanças
Foi simulada a adição de uma funcionalidade de notificação para tarefas pendentes por mais de 7 dias, justificada pela necessidade de maior proatividade da equipe. Essa mudança foi registrada no Kanban com um novo card e atualizada aqui.
Reflexões

Causas de falhas em projetos ágeis: Má gestão de tarefas e falhas de comunicação são mitigadas pelo Kanban visual no GitHub, que centraliza o acompanhamento.
Beneficiados: Gerentes e equipes de logística utilizam o CRUD para priorizar e monitorar tarefas em tempo real.
Controle de qualidade: GitHub Actions garante entrega confiável ao rodar testes automatizados.
Desafios de mudanças: Adaptação exige comunicação clara; o Kanban facilita ajustes dinâmicos.
Aplicação de metodologias: O Kanban aqui reflete a flexibilidade ensinada, conectando teoria à prática.

Licença
Este projeto está sob a licença MIT. Adicione um arquivo LICENSE na raiz (gerado automaticamente no GitHub).
Referências
Baseado em Engenharia de Software: Uma Abordagem Profissional (Roger Pressman) e GitHub Docs - Actions.
