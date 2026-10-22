from app import app


def test_health_endpoint(): #first we test health 
    client = app.test_client() #test_client is a Flask test client test app.py application
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "healthy"} #return these or the tests fails 

def test_without_question():
    client = app.test_client()
    response = client.post("/ask", json= {}) #json = {} sends an empty answer (no question)

    assert response.status_code == 400
    assert response.json == {"error": "Please provide a question"}



def test_with_question():
    client = app.test_client()
    response = client.post("/ask", json = {"question": "What is cloud computing?"})

    assert response.status_code == 200
    assert response.json["question"] == "What is cloud computing?"

    assert response.json["answer"] == "Your question was received successfully!"