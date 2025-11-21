glyph_map = {
    "a": "𓀀",
    "b": "𓁹",
    "c": "⚙️",
    "d": "🜂",
    "e": "💧",
    "f": "🌀",
    "g": "🔥",
    "h": "🌬️",
    "i": "🪶",
    "j": "🗝️",
    "k": "🛡️",
    "l": "🌿",
    "m": "🌑",
    "n": "🌕",
    "o": "🌞",
    "p": "🔮",
    "q": "🧿",
    "r": "🧬",
    "s": "🪞",
    "t": "⛩️",
    "u": "🌊",
    "v": "🦋",
    "w": "💠",
    "x": "❎",
    "y": "🔆",
    "z": "⚡",
    " ": "⬚"
}

def to_glyphs(text):
    return ''.join(glyph_map.get(c.lower(), c) for c in text)

def from_glyphs(glyphed_text):
    reverse_map = {v: k for k, v in glyph_map.items()}
    return ''.join(reverse_map.get(c, c) for c in glyphed_text)
