from codec import encode, decode, mirror

def test_encode():
    assert encode("hello") == "olleh"

def test_decode():
    assert decode("olleh") == "hello"

def test_mirror():
    assert mirror("hello") == "hello | olleh"

if __name__ == "__main__":
    test_encode()
    test_decode()
    test_mirror()
    print("All tests passed.")
