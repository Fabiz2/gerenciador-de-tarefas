import pytest

from src.app import app, tasks

@pytest.fixture
def client():
    """Fixture para criar um cliente de teste Flask."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            # Limpa a lista de tarefas antes de cada teste
            tasks.clear()
            yield client

def test_home_route(client):
    """Testa se a página inicial carrega corretamente."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Gerenciador de Tarefas' in response.data

def test_add_task_with_description(client):
    """Testa adicionar uma tarefa com título e descrição."""
    response = client.post('/add_task', data={
        'title': 'Tarefa de Teste',
        'description': 'Descrição da tarefa de teste'
    })
    assert response.status_code == 302  # Redirect após adicionar
    
    # Verifica se a tarefa foi adicionada
    assert len(tasks) == 1
    assert tasks[0]['title'] == 'Tarefa de Teste'
    assert tasks[0]['description'] == 'Descrição da tarefa de teste'
    assert tasks[0]['completed'] == False

def test_add_task_without_description(client):
    """Testa adicionar uma tarefa apenas com título."""
    response = client.post('/add_task', data={
        'title': 'Tarefa Sem Descrição'
    })
    assert response.status_code == 302  # Redirect após adicionar
    
    # Verifica se a tarefa foi adicionada com descrição vazia
    assert len(tasks) == 1
    assert tasks[0]['title'] == 'Tarefa Sem Descrição'
    assert tasks[0]['description'] == ''
    assert tasks[0]['completed'] == False

def test_complete_task_valid_id(client):
    """Testa completar uma tarefa com ID válido."""
    # Adiciona uma tarefa primeiro
    tasks.append({'title': 'Tarefa para Completar', 'description': 'Teste', 'completed': False})
    
    response = client.get('/complete_task/0')
    assert response.status_code == 302  # Redirect após completar
    
    # Verifica se a tarefa foi marcada como completa
    assert tasks[0]['completed'] == True

def test_complete_task_invalid_id(client):
    """Testa completar uma tarefa com ID inválido."""
    response = client.get('/complete_task/999')
    assert response.status_code == 302  # Redirect mesmo com ID inválido
    
    # Lista deve permanecer vazia
    assert len(tasks) == 0

def test_delete_task_valid_id(client):
    """Testa deletar uma tarefa com ID válido."""
    # Adiciona uma tarefa primeiro
    tasks.append({'title': 'Tarefa para Deletar', 'description': 'Teste', 'completed': False})
    
    response = client.get('/delete_task/0')
    assert response.status_code == 302  # Redirect após deletar
    
    # Verifica se a tarefa foi removida
    assert len(tasks) == 0

def test_delete_task_invalid_id(client):
    """Testa deletar uma tarefa com ID inválido."""
    # Adiciona uma tarefa primeiro
    tasks.append({'title': 'Tarefa Existente', 'description': 'Teste', 'completed': False})
    
    response = client.get('/delete_task/999')
    assert response.status_code == 302  # Redirect mesmo com ID inválido
    
    # Tarefa deve permanecer na lista
    assert len(tasks) == 1
    assert tasks[0]['title'] == 'Tarefa Existente'

def test_workflow_multiple_tasks(client):
    """Testa um fluxo completo com múltiplas tarefas."""
    # Adiciona primeira tarefa
    client.post('/add_task', data={
        'title': 'Primeira Tarefa',
        'description': 'Primeira descrição'
    })
    
    # Adiciona segunda tarefa
    client.post('/add_task', data={
        'title': 'Segunda Tarefa',
        'description': 'Segunda descrição'
    })
    
    # Verifica se ambas foram adicionadas
    assert len(tasks) == 2
    
    # Completa a primeira tarefa
    client.get('/complete_task/0')
    assert tasks[0]['completed'] == True
    assert tasks[1]['completed'] == False
    
    # Deleta a segunda tarefa
    client.get('/delete_task/1')
    assert len(tasks) == 1
    assert tasks[0]['title'] == 'Primeira Tarefa'

def test_task_display_on_home_page(client):
    """Testa se as tarefas são exibidas corretamente na página inicial."""
    # Adiciona algumas tarefas
    tasks.append({'title': 'Tarefa Visível 1', 'description': 'Desc 1', 'completed': False})
    tasks.append({'title': 'Tarefa Visível 2', 'description': 'Desc 2', 'completed': True})
    
    response = client.get('/')
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert 'Tarefa Visível 1' in html
    assert 'Tarefa Visível 2' in html
    assert 'Desc 1' in html
    assert 'Desc 2' in html