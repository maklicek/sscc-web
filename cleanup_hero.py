from pathlib import Path
import re

# složka s webem (aktuální)
root = Path(__file__).parent

# regexy
pattern_empty_hero = re.compile(
    r'<div\s+class="hero-slot">\s*</div>',
    re.DOTALL | re.IGNORECASE
)

pattern_placeholder_hero = re.compile(
    r'<div\s+class="hero">.*?</div>',
    re.DOTALL | re.IGNORECASE
)

pattern_placeholder_img = re.compile(
    r'<div\s+class="img-placeholder">.*?</div>',
    re.DOTALL | re.IGNORECASE
)

def clean_file(path: Path):
    html = path.read_text(encoding="utf-8")

    original = html

    # 1) smazat staré hero placeholdery
    html = pattern_placeholder_hero.sub("", html)

    # 2) smazat img-placeholder bloky
    html = pattern_placeholder_img.sub("", html)

    # 3) smazat prázdné hero-sloty (jen whitespace uvnitř)
    html = pattern_empty_hero.sub("", html)

    if html != original:
        # záloha .bak pro jistotu
        backup = path.with_suffix(path.suffix + ".bak")
        backup.write_text(original, encoding="utf-8")

        path.write_text(html, encoding="utf-8")
        print(f"Upraveno: {path.name} (záloha: {backup.name})")


def main():
    # projít všechny .html v aktuálním adresáři
    for html_file in root.glob("*.html"):
        clean_file(html_file)


if __name__ == "__main__":
    main()
