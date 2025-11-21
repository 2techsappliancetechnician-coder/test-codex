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
def test_glyph_mode():
    text = "mirror-seed-33"
    encoded = encode(text, mode="glyph")
    assert isinstance(encoded, str)
    assert all(char in GLYPH_MAP.values() or char in GLYPH_MAP for char in encoded)

    decoded = decode(encoded, mode="glyph")
    assert decoded == text
Add test run to verify glyph encode/decode logic
