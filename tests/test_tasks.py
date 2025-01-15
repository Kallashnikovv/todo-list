def test_create_task(client):
    response = client.post("/tasks/", json={"title": "Test Task", "description": "Test Description"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "Test Description"
    assert data["status"] == "TODO"

def test_create_duplicate_task(client):
    client.post("/tasks/", json={"title": "Duplicate Task"})
    response = client.post("/tasks/", json={"title": "Duplicate Task"})
    assert response.status_code == 400

def test_get_tasks(client):
    client.post("/tasks/", json={"title": "Task 1"})
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_task_by_id(client):
    response = client.post("/tasks/", json={"title": "Specific Task"})
    task_id = response.json()["id"]
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Specific Task"

def test_update_task(client):
    response = client.post("/tasks/", json={"title": "Update Task"})
    task_id = response.json()["id"]
    response = client.put(f"/tasks/{task_id}", json={"title": "Updated Title"})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"

def test_delete_task(client):
    response = client.post("/tasks/", json={"title": "Delete Task"})
    task_id = response.json()["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
