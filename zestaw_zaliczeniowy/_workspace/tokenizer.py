
import re

class Tokenizer:
    """Konfigurowany tokenizator: HTML strip + case + min length filter."""
    def __init__(self, lower: bool = True, strip_html: bool = True, min_length: int = 1):
        self.lower = lower
        self.strip_html = strip_html
        self.min_length = min_length

    def tokenize(self, text: str) -> list[str]:
        # 1. usuń HTML
        if self.strip_html:
            text = re.sub(r"<[^>]+>", " ", text)

        # 2. lowercase
        if self.lower:
            text = text.lower()

        # 3. tokeny (polskie znaki OK)
        tokens = re.findall(r"\w+", text, flags=re.UNICODE)

        # 4. filtr długości
        return [t for t in tokens if len(t) >= self.min_length]

    def vocab(self, texts: list[str]) -> set[str]:
        vocab_set = set()
        for text in texts:
            vocab_set.update(self.tokenize(text))
        return vocab_set
