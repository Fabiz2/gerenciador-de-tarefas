import pytest
import sys
import os

# Adiciona o diretório raiz ao path para importar o app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, tasks

@pytest.fixture
def client():
    """Fixture para criar um cliente de teste"""
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def reset_tasks():
    """Fixture para resetar as tarefas antes de cada teste"""
    tasks.clear()
    yield
    tasks.clear()

def test_index_route(client):
    """Testa se a página inicial carrega corretamente"""
    response = client.get('/')
    assert response.status_code == 200
    # Verifica se contém elementos esperados na página
    assert b'<!DOCTYPE html>' in response.data

def test_add_task_success(client):
    """Testa a adição de uma tarefa com sucesso"""
    response = client.post('/add_task', data={
        'title': 'Nova Tarefa',
        'description': 'Descrição da tarefa'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert len(tasks) == 1
    assert tasks[0]['title'] == 'Nova Tarefa'
    assert tasks[0]['description'] == 'Descrição da tarefa'
    assert tasks[0]['completed'] is False

def test_add_task_empty_description(client):
    """Testa adição de tarefa com descrição vazia"""
    response = client.post('/add_task', data={
        'title': 'Tarefa sem descrição',
        'description': ''
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert len(tasks) == 1
    assert tasks[0]['title'] == 'Tarefa sem descrição'
    assert tasks[0]['description'] == ''

def test_complete_task(client):
    """Testa marcar uma tarefa como concluída"""
    # Primeiro adiciona uma tarefa
    tasks.append({'title': 'Tarefa para completar', 'description': '', 'completed': False})
    
    response = client.get('/complete_task/0', follow_redirects=True)
    assert response.status_code == 200
    assert tasks[0]['completed'] is True

def test_complete_task_invalid_index(client):
    """Testa completar uma tarefa com índice inválido"""
    initial_task_count = len(tasks)
    response = client.get('/complete_task/999', follow_redirects=True)  # Índice inválido
    
    assert response.status_code == 200
    # Nenhuma tarefa deve ser modificada
    assert len(tasks) == initial_task_count

def test_delete_task(client):
    """Testa excluir uma tarefa"""
    # Adiciona uma tarefa primeiro
    tasks.append({'title': 'Tarefa para excluir', 'description': '', 'completed': False})
    
    response = client.get('/delete_task/0', follow_redirects=True)
    assert response.status_code == 200
    assert len(tasks) == 0

def test_delete_task_invalid_index(client):
    """Testa excluir uma tarefa com índice inválido"""
    # Adiciona uma tarefa
    tasks.append({'title': 'Tarefa', 'description': '', 'completed': False})
    initial_task_count = len(tasks)
    
    response = client.get('/delete_task/999', follow_redirects=True)  # Índice inválido
    
    assert response.status_code == 200
    # Nenhuma tarefa deve ser excluída
    assert len(tasks) == initial_task_count

def test_multiple_tasks_operations(client):
    """Testa operações com múltiplas tarefas"""
    # Adiciona várias tarefas
    client.post('/add_task', data={'title': 'Tarefa 1', 'description': 'Desc 1'}, follow_redirects=True)
    client.post('/add_task', data={'title': 'Tarefa 2', 'description': 'Desc 2'}, follow_redirects=True)
    client.post('/add_task', data={'title': 'Tarefa 3', 'description': 'Desc 3'}, follow_redirects=True)
    
    assert len(tasks) == 3
    
    # Completa a segunda tarefa
    client.get('/complete_task/1', follow_redirects=True)
    assert tasks[1]['completed'] is True
    assert tasks[0]['completed'] is False
    assert tasks[2]['completed'] is False
    
    # Exclui a primeira tarefa
    client.get('/delete_task/0', follow_redirects=True)
    assert len(tasks) == 2
    # Após excluir a primeira, as tarefas são reorganizadas
    assert tasks[0]['title'] == 'Tarefa 2'
    assert tasks[1]['title'] == 'Tarefa 3'

def test_task_structure(client):
    """Testa se a estrutura das tarefas está correta"""
    client.post('/add_task', data={
        'title': 'Tarefa Teste',
        'description': 'Descrição Teste'
    }, follow_redirects=True)
    
    task = tasks[0]
    # Verifica se todas as chaves necessárias existem
    assert 'title' in task
    assert 'description' in task
    assert 'completed' in task
    
    # Verifica tipos de dados
    assert isinstance(task['title'], str)
    assert isinstance(task['description'], str)
    assert isinstance(task['completed'], bool)
