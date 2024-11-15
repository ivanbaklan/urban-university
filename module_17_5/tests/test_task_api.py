def test_crud_task(test_client, user_payload, task_payload):
    # Get task non-existent id
    response = test_client.get(f"/task/task_id?task_id=1")
    assert response.status_code == 404
    response_json = response.json()
    assert response_json == {"detail": "There is no task found"}

    # Created task with non-existent user_id
    response = test_client.post("/task/create", json=task_payload)
    assert response.status_code == 404
    response_json = response.json()
    assert response_json == {"detail": "There is no user found"}

    # Created task
    response = test_client.post("/user/create", json=user_payload)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["status_code"] == 201
    assert response_json["transaction"] == "User create successful"

    response = test_client.post("/task/create", json=task_payload)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["status_code"] == 201
    assert response_json["transaction"] == "Task create successful"

    # Get the created task
    response = test_client.get(f"/task/task_id?task_id=1")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["id"] == 1
    assert response_json["content"] == task_payload["content"]
    assert response_json["title"] == task_payload["title"]
    assert response_json["user_id"] == task_payload["user_id"]

    # Update task
    task_payload["task_id"] = 1
    task_payload["content"] = "Contenti2"
    response = test_client.put(f"/task/update", json=task_payload)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json == {
        "status_code": 200,
        "transaction": "Task update successful",
    }
    response = test_client.get(f"/task/task_id?task_id=1")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["content"] == "Contenti2"

    # Delete task
    response = test_client.delete(f"/task/delete?task_id=1")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json == {
        "status_code": 200,
        "transaction": "Task delete successful",
    }
    response = test_client.delete(f"/task/delete?task_id=1")
    assert response.status_code == 404
    response_json = response.json()
    assert response_json == {"detail": "There is no task found"}

    # Delete user
    response = test_client.post("/task/create", json=task_payload)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["status_code"] == 201
    assert response_json["transaction"] == "Task create successful"
    response = test_client.get(f"/task/task_id?task_id=1")
    assert response.status_code == 200

    response = test_client.delete(f"/user/delete?user_id=1")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json == {
        "status_code": 200,
        "transaction": "User delete successful",
    }

    response = test_client.get(f"/task/task_id?task_id=1")
    assert response.status_code == 404


def test_tasks(test_client):
    user_payload_1 = {
        "username": "user1",
        "firstname": "Pasha",
        "lastname": "Technique",
        "age": 40,
    }
    user_payload_2 = {
        "username": "user2",
        "firstname": "Roza",
        "lastname": "Syabitova",
        "age": 62,
    }
    user_payload_3 = {
        "username": "user3",
        "firstname": "Alex",
        "lastname": "Unknown",
        "age": 25,
    }

    task_payload_1 = {
        "title": "FirstTask",
        "content": "Content1",
        "priority": 0,
        "user_id": 1,
    }

    task_payload_2 = {
        "title": "SecondTask",
        "content": "Content2",
        "priority": 2,
        "user_id": 1,
    }

    task_payload_3 = {
        "title": "ThirdTask",
        "content": "Content3",
        "priority": 4,
        "user_id": 3,
    }

    task_payload_4 = {
        "title": "FourthTask",
        "content": "Content4",
        "priority": 6,
        "user_id": 3,
    }

    # Created users
    response = test_client.post("/user/create", json=user_payload_1)
    assert response.status_code == 200
    response = test_client.post("/user/create", json=user_payload_2)
    assert response.status_code == 200
    response = test_client.post("/user/create", json=user_payload_3)
    assert response.status_code == 200

    response = test_client.post("/task/create", json=task_payload_1)
    assert response.status_code == 200
    response = test_client.post("/task/create", json=task_payload_2)
    assert response.status_code == 200
    response = test_client.post("/task/create", json=task_payload_3)
    assert response.status_code == 200
    response = test_client.post("/task/create", json=task_payload_4)
    assert response.status_code == 200

    # Test get task list
    test_result = [
        {
            "id": 4,
            "priority": 6,
            "user_id": 3,
            "content": "Content4",
            "title": "FourthTask",
            "completed": False,
            "slug": "fourthtask",
        }
    ]

    response = test_client.delete(f"/task/delete?task_id=3")
    assert response.status_code == 200
    response = test_client.delete(f"/user/delete?user_id=1")
    assert response.status_code == 200

    response = test_client.get("/task")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json == test_result

    response = test_client.get("/user/user_id/tasks?user_id=3")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json == test_result
