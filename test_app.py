from app import hello

def test_hello():
    #assert hello() == "Hello from CI/CD"
    assert hello() == "Wrong input"
