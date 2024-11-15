def test_welcome(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Taskmanager"}


def test_crud_user(test_client, user_payload):
    # Get user non-existent id
    response = test_client.get(f"/user/user_id?user_id=1")
    assert response.status_code == 404
    response_json = response.json()
    assert response_json == {"detail": "There is no user found"}

    # Created user
    response = test_client.post("/user/create", json=user_payload)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["status_code"] == 201
    assert response_json["transaction"] == "User create successful"

    # Get the created user
    response = test_client.get(f"/user/user_id?user_id=1")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["id"] == 1
    assert response_json["username"] == user_payload["username"]
    assert response_json["firstname"] == user_payload["firstname"]
    assert response_json["lastname"] == user_payload["lastname"]
    assert response_json["age"] == user_payload["age"]

    # Update user
    user_payload["user_id"] = 1
    user_payload["firstname"] = "first_name_update"
    response = test_client.put(f"/user/update", json=user_payload)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json == {
        "status_code": 200,
        "transaction": "User update successful",
    }
    response = test_client.get(f"/user/user_id?user_id=1")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["firstname"] == "first_name_update"

    # Delete user
    response = test_client.delete(f"/user/delete?user_id=1")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json == {
        "status_code": 200,
        "transaction": "User delete successful",
    }
    response = test_client.delete(f"/user/delete?user_id=1")
    assert response.status_code == 404
    response_json = response.json()
    assert response_json == {"detail": "There is no user found"}


def test_users(test_client):
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

    # Created users
    response = test_client.post("/user/create", json=user_payload_1)
    assert response.status_code == 200
    response = test_client.post("/user/create", json=user_payload_2)
    assert response.status_code == 200
    response = test_client.post("/user/create", json=user_payload_3)
    assert response.status_code == 200

    # Update user id 3
    user_payload_3["user_id"] = 3
    user_payload_3["firstname"] = "Bear"
    user_payload_3["lastname"] = "Grylls"
    user_payload_3["age"] = 50
    response = test_client.put(f"/user/update", json=user_payload_3)
    assert response.status_code == 200

    # Delete user id 2
    response = test_client.delete(f"/user/delete?user_id=2")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json == {
        "status_code": 200,
        "transaction": "User delete successful",
    }

    # Get user non-existent id
    response = test_client.delete(f"/user/delete?user_id=2")
    assert response.status_code == 404
    response_json = response.json()
    assert response_json == {"detail": "There is no user found"}

    # Test get user list
    test_result = [
        {
            "firstname": "Pasha",
            "id": 1,
            "age": 40,
            "lastname": "Technique",
            "username": "user1",
            "slug": "user1",
        },
        {
            "firstname": "Bear",
            "id": 3,
            "age": 50,
            "lastname": "Grylls",
            "username": "user3",
            "slug": "user3",
        },
    ]
    response = test_client.get(f"/user/")
    response_json = response.json()
    assert response_json == test_result
