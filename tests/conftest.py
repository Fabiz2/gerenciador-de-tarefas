import pytest
import sys
import os

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

@pytest.fixture(scope='session')
def app():
    """Fixture da aplicação para todos os testes"""
    from app import app as flask_app
    return flask_app

@pytest.fixture
def client(app):
    """Fixture do cliente de teste"""
    return app.test_client()
