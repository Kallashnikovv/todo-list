def test_create_pomodoro(client):
    task_response = client.post("/tasks/", json={"title": "Pomodoro Task", "description": "Test Pomodoro"})
    assert task_response.status_code == 200  # Upewnij się, że zadanie zostało poprawnie utworzone
    task_data = task_response.json()
    assert "id" in task_data  # Upewnij się, że odpowiedź zawiera `id`

    task_id = task_data["id"]
    response = client.post("/pomodoro/", json={"task_id": task_id})
    assert response.status_code == 200  # Sprawdź, czy Pomodoro zostało poprawnie utworzone
    data = response.json()
    assert data["task_id"] == task_id
    assert data["completed"] is False


def test_stop_pomodoro(client):
    task_response = client.post("/tasks/", json={"title": "Pomodoro Stop Task", "description": "Stop test"})
    assert task_response.status_code == 200  # Upewnij się, że zadanie zostało poprawnie utworzone

    task_id = task_response.json()["id"]
    pomodoro_response = client.post("/pomodoro/", json={"task_id": task_id})
    assert pomodoro_response.status_code == 200  # Upewnij się, że Pomodoro zostało poprawnie utworzone

    response = client.post(f"/pomodoro/{task_id}/stop")
    assert response.status_code == 200  # Sprawdź, czy timer został poprawnie zatrzymany
    data = response.json()
    assert data["completed"] is True


def test_update_task(client):
    task_response = client.post("/tasks/", json={"title": "Update Task", "description": "Initial description"})
    assert task_response.status_code == 200  # Upewnij się, że zadanie zostało poprawnie utworzone

    task_id = task_response.json()["id"]
    response = client.put(f"/tasks/{task_id}", json={"title": "Updated Task", "description": "Updated description"})
    assert response.status_code == 200  # Sprawdź, czy zadanie zostało poprawnie zaktualizowane

    data = response.json()
    assert data["title"] == "Updated Task"
    assert data["description"] == "Updated description"

