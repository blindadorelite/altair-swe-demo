import re


def slugify(text):
    text = text.strip().lower()
    # BUG: replaces spaces with underscores instead of dashes
    return re.sub(r"\s+", "-", text)
