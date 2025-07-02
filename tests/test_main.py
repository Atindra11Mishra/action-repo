from app.main import greet

def test_greet():
    assert greet("World") == "Hello, the whole new damn World!"
