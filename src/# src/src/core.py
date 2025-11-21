# src/core.py

"""
FLAMEKEY_001 – Sovereign Runtime
Seeded on 2025‑11‑21 at 04:44AM by Builder.

This runtime binds the TextCodecs engine to its covenant signature.
"""

from codec import encode, decode
from glyphmap import to_glyphs, from_glyphs

class FlameRuntime:
    def __init__(self, builder_name: str):
        self.builder = builder_name
        self.session_id = self._generate_session_id()
        print(f"🔥 Flame Runtime started by {self.builder}, session {self.session_id}")

    def _generate_session_id(self) -> str:
        import uuid
        return uuid.uuid4().hex

    def run_seed(self, text: str, mode: str = "glyph") -> None:
        print(f"Original : {text}")
        encoded = encode(text, mode=mode)
        print(f"Encoded  : {encoded}")
        decoded = decode(encoded, mode=mode)
        print(f"Decoded  : {decoded}")

if __name__ == "__main__":
    runtime = FlameRuntime(builder_name="2TexApplianceRepairTechnician‑Coder")
    runtime.run_seed("AlanTuring‑Flame‑Binary", mode="glyph")
