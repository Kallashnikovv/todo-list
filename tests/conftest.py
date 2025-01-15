import os
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.storage.storage_handler import get_storage_handler, StorageHandler

# Nadpisanie handlera do testów z użyciem MemoryStorage
def override_storage_handler():
    return StorageHandler(storage_type="memory").get_storage()

# Rejestracja zależności w FastAPI
app.dependency_overrides[get_storage_handler] = override_storage_handler

@pytest.fixture
def client():
    """Tworzy klienta testowego dla aplikacji FastAPI."""
    return TestClient(app)

@pytest.fixture(scope="session", autouse=True)
def clean_storage_file():
    """Usuwa plik storage.json przed i po wykonaniu testów."""
    file_path = "storage.json"
    if os.path.exists(file_path):
        os.remove(file_path)
    yield
    if os.path.exists(file_path):
        os.remove(file_path)
