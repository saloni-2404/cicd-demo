from app import hello

def test_hello():
    assert hello() == "Hello from CI/CD"
    print("Test passed: hello() returned the correct message")
    #assert hello() == "Wrong input"
