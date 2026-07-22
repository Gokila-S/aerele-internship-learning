import json
from pathlib import Path
from typing import List, Optional
from .models import Book


class Storage:
    def __init__(self, path: Optional[str] = None):
        self.path = Path(path or "library_data.json")
        if not self.path.exists():
            self._write([])

    def _read(self) -> List[dict]:
        try:
            with self.path.open("r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    def _write(self, data: List[dict]):
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def load_books(self) -> List[Book]:
        raw = self._read()
        return [Book(**r) for r in raw]

    def save_books(self, books: List[Book]):
        self._write([b.to_dict() for b in books])

    def next_id(self) -> int:
        books = self.load_books()
        if not books:
            return 1
        return max(b.id for b in books) + 1

    def find_by_id(self, book_id: int) -> Optional[Book]:
        for b in self.load_books():
            if b.id == book_id:
                return b
        return None
