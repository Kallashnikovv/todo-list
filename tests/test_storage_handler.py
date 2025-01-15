from src.storage.storage_handler import StorageHandler
from src.common.models import Task

def test_memory_storage_handler():
    handler = StorageHandler(storage_type="memory").get_storage()
    handler.add_task(Task(id=1, title="Memory Task", description="Test", status="TODO"))
    tasks = handler.get_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "Memory Task"

def test_file_storage_handler(tmp_path):
    file_path = tmp_path / "test_storage.json"
    handler = StorageHandler(storage_type="file", file_path=str(file_path)).get_storage()
    handler.add_task(Task(id=1, title="File Task", description="Test", status="TODO"))
    tasks = handler.get_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "File Task"
