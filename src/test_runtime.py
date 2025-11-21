from codec import Codec
from glyphmap import GlyphMap
from core import FlameRuntime

if __name__ == "__main__":
    seed = "FLAMEKEY_330"
    codec = Codec(seed)
    glyphs = GlyphMap(seed)
    runtime = FlameRuntime(seed)

    print("🔹 Encoded:", codec.encode(seed))
    print("🔹 Decoded:", codec.decode(codec.encode(seed)))
    print("🔹 Glyphs:", glyphs.glyphs)
    print("🔹 Runtime Log:", runtime.log)
