import pytest
import sys
import os

# Adiciona o diretório src ao path para importar o app
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from app import app

@pytest.fixture
def client():
    """Fixture para criar um cliente de teste"""
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def reset_tasks():
    """Fixture para resetar as tarefas antes de cada teste"""
    from app import tasks
    tasks.clear()
    yield
    tasks.clear()

def test_index_route(client):
    """Testa se a página inicial carrega corretamente"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Gerenciador de Tarefas' in response.data

def test_add_task_success(client):
    """Testa a adição de uma tarefa com sucesso"""
    response = client.post('/add', data={
        'title': 'Tarefa de Teste',
        'description': 'Descrição de teste',
        'priority': 'high'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    from app import tasks
    assert len(tasks) == 1
    assert tasks[0]['title'] == 'Tarefa de Teste'
    assert tasks[0]['description'] == 'Descrição de teste'
    assert tasks[0]['priority'] == 'high'
    assert tasks[0]['completed'] is False

def test_add_task_empty_title(client):
    """Testa a tentativa de adicionar tarefa com título vazio"""
    from app import tasks
    initial_count = len(tasks)
    
    response = client.post('/add', data={
        'title': '',  # Título vazio
        'description': 'Descrição',
        'priority': 'medium'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    # Não deve adicionar tarefa com título vazio
    assert len(tasks) == initial_count

def test_delete_task(client):
    """Testa a exclusão de uma tarefa"""
    from app import tasks
    # Adiciona uma tarefa primeiro
    tasks.append({
        'id': 1,
        'title': 'Tarefa para excluir',
        'description': '',
        'completed': False,
        'priority': 'medium'
    })
    
    initial_count = len(tasks)
    response = client.get('/delete/1', follow_redirects=True)
    
    assert response.status_code == 200
    assert len(tasks) == initial_count - 1

def test_delete_nonexistent_task(client):
    """Testa a exclusão de uma tarefa que não existe"""
    from app import tasks
    initial_count = len(tasks)
    
    response = client.get('/delete/999', follow_redirects=True)  # ID que não existe
    
    assert response.status_code == 200
    assert len(tasks) == initial_count  # Nenhuma tarefa deve ser removida

def test_toggle_task(client):
    """Testa marcar/desmarcar tarefa como concluída"""
    from app import tasks
    tasks.append({
        'id': 1,
        'title': 'Tarefa para toggle',
        'description': '',
        'completed': False,
        'priority': 'low'
    })
    
    # Primeiro toggle - marca como concluída
    response = client.get('/toggle/1', follow_redirects=True)
    assert response.status_code == 200
    assert tasks[0]['completed'] is True
    
    # Segundo toggle - desmarca
    response = client.get('/toggle/1', follow_redirects=True)
    assert response.status_code == 200
    assert tasks[0]['completed'] is False

def test_toggle_nonexistent_task(client):
    """Testa alternar uma tarefa que não existe"""
    from app import tasks
    initial_count = len(tasks)
    
    response = client.get('/toggle/999', follow_redirects=True)
    
    assert response.status_code == 200
    assert len(tasks) == initial_count  # Nenhuma tarefa deve ser alterada

def test_api_tasks_empty(client):
    """Testa a API de tarefas quando não há tarefas"""
    response = client.get('/api/tasks')
    
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert data == []

def test_api_tasks_with_data(client):
    """Testa a API de tarefas quando há tarefas"""
    from app import tasks
    tasks.append({
        'id': 1,
        'title': 'Tarefa API',
        'description': 'Teste API',
        'completed': False,
        'priority': 'medium'
    })
    
    response = client.get('/api/tasks')
    
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['title'] == 'Tarefa API'

def test_task_id_uniqueness(client):
    """Testa se os IDs das tarefas são únicos"""
    from app import tasks
    
    # Adiciona várias tarefas
    client.post('/add', data={'title': 'Tarefa 1'}, follow_redirects=True)
    client.post('/add', data={'title': 'Tarefa 2'}, follow_redirects=True)
    client.post('/add', data={'title': 'Tarefa 3'}, follow_redirects=True)
    
    # Verifica se todos os IDs são únicos
    task_ids = [task['id'] for task in tasks]
    assert len(task_ids) == len(set(task_ids))  # Todos únicos

def test_task_structure(client):
    """Testa se a estrutura das tarefas está correta"""
    client.post('/add', data={
        'title': 'Tarefa Estruturada',
        'description': 'Descrição completa',
        'priority': 'high'
    }, follow_redirects=True)
    
    from app import tasks
    task = tasks[0]
    
    # Verifica se todas as chaves necessárias existem
    required_keys = ['id', 'title', 'description', 'completed', 'priority']
    for key in required_keys:
        assert key in task
    
    # Verifica tipos de dados
    assert isinstance(task['id'], int)
    assert isinstance(task['title'], str)
    assert isinstance(task['description'], str)
    assert isinstance(task['completed'], bool)
    assert isinstance(task['priority'], str)
    assert task['priority'] in ['low', 'medium', 'high']
