import re
from typing import Optional

__all__ = ["remove_bracketed"]


def remove_bracketed(s: Optional[str]) -> str:
    """Remove all contents inside (), [], {}, （）, 【】 repeatedly (handles nesting).

    Keeps the rest of the text and collapses extra whitespace.
    """
    if not s:
        return s or ""
    pattern = re.compile(
        r"\([^()]*\)|\[[^\[\]]*\]|\{[^{}]*\}|（[^（）]*）|【[^【】]*】"
    )
    prev = None
    while True:
        if not pattern.search(s):
            break
        new = pattern.sub("", s)
        if new == s or new == prev:
            break
        prev = s
        s = new
    # collapse whitespace
    s = re.sub(r"\s+", " ", s).strip()
    return s
