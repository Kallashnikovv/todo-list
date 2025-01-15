from src.storage.memory_storage import MemoryStorage
from src.storage.file_storage import FileStorage

class StorageHandler:
    def __init__(self, storage_type="file", file_path="storage.json"):
        if storage_type == "file":
            self.storage = FileStorage(file_path=file_path)
        elif storage_type == "memory":
            self.storage = MemoryStorage()
            
    def get_storage(self):
        return self.storage

# Singleton dla StorageHandler
_handler_instance = None

def get_storage_handler(storage_type="memory"):
    global _handler_instance
    if _handler_instance is None:
        _handler_instance = StorageHandler(storage_type=storage_type, file_path="storage.json")
    return _handler_instance.get_storage()
