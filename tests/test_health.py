def test_service_is_alive(client):
    response = client.get("/dermoapp/clinical-history/v1/health")
    print(response)
    data = response.json
    assert "OK" == data['message']

    
