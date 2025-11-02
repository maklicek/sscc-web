import os
import re
import argparse
from datetime import datetime

CLOSE_TAGS_RE = {
    "body": re.compile(r"</body\s*>", re.I),
    "html": re.compile(r"</html\s*>", re.I),
    "main_close": re.compile(r"</main\s*>", re.I),
    "main_open": re.compile(r"<main(\s|>)", re.I),
}

def analyze(content: str):
    """Return list of issues found in the HTML content."""
    issues = []
    if not CLOSE_TAGS_RE["body"].search(content):
        issues.append("❌ Chybí </body>")
    if not CLOSE_TAGS_RE["html"].search(content):
        issues.append("❌ Chybí </html>")

    open_mains = len(CLOSE_TAGS_RE["main_open"].findall(content))
    close_mains = len(CLOSE_TAGS_RE["main_close"].findall(content))
    if open_mains > close_mains:
        issues.append(f"⚠️  Chybí </main> (otevřeno {open_mains}, zavřeno {close_mains})")

    # Heuristika: utnutá věta na konci souboru
    tail = content.strip()[-40:]
    if not content.strip().endswith((">", "</html>", "</body>")) and len(content) > 0:
        issues.append("⚠️  Soubor pravděpodobně utnutý (nekončí značkou)")

    return issues, open_mains, close_mains


def fix_content(content: str, add_marker: bool):
    """Append missing closing tags in safe order. Return fixed content (or same)."""
    fixed = content

    # Doplň </main>, pokud je počet otevřených větší než zavřených
    open_mains = len(CLOSE_TAGS_RE["main_open"].findall(fixed))
    close_mains = len(CLOSE_TAGS_RE["main_close"].findall(fixed))
    if open_mains > close_mains:
        fixed = fixed.rstrip() + "\n</main>\n"

    # Doplň </body> a </html> v korektním pořadí
    if not CLOSE_TAGS_RE["body"].search(fixed):
        # vlož těsně před </html>, pokud existuje, jinak na konec
        if CLOSE_TAGS_RE["html"].search(fixed):
            fixed = CLOSE_TAGS_RE["html"].sub("</body>\n</html>", fixed, count=1)
        else:
            fixed = fixed.rstrip() + "\n</body>\n"
    if not CLOSE_TAGS_RE["html"].search(fixed):
        fixed = fixed.rstrip() + "\n</html>\n"

    # Volitelný integritní marker
    if add_marker and "SSCC page loaded successfully" not in fixed:
        fixed = fixed.replace("</body>", '  <script>console.log("✅ SSCC page loaded successfully");</script>\n</body>')

    return fixed


def process(root: str, do_fix: bool, recursive: bool, add_marker: bool):
    target_files = []
    if recursive:
        for dirpath, _, files in os.walk(root):
            for f in files:
                if f.lower().endswith(".html"):
                    target_files.append(os.path.join(dirpath, f))
    else:
        for f in os.listdir(root):
            if f.lower().endswith(".html"):
                target_files.append(os.path.join(root, f))

    print(f"🔍 Kontrola HTML v: {os.path.abspath(root)}")
    print("=" * 60)

    any_issues = False
    fixed_count = 0

    for path in sorted(target_files):
        try:
            with open(path, "r", encoding="utf-8") as fh:
                content = fh.read()
        except Exception as e:
            print(f"\n📄 {os.path.basename(path)}")
            print("   ⚠️  Nelze číst soubor:", e)
            any_issues = True
            continue

        issues, open_mains, close_mains = analyze(content)
        if issues:
            any_issues = True
            print(f"\n📄 {os.path.basename(path)}")
            for i in issues:
                print("   ", i)

            if do_fix:
                fixed = fix_content(content, add_marker)
                if fixed != content:
                    # Záloha
                    bak = f"{path}.bak"
                    try:
                        if not os.path.exists(bak):
                            with open(bak, "w", encoding="utf-8") as bfh:
                                bfh.write(content)
                        # Zápis opravy
                        with open(path, "w", encoding="utf-8") as fh:
                            fh.write(fixed)
                        fixed_count += 1
                        print("   ✅ Opraveno a uloženo (záloha: .bak)")
                    except Exception as e:
                        print("   ❌ Chyba při ukládání opravy:", e)
                else:
                    print("   ℹ️  Nebylo co opravit (heuristika nic nedoplnila).")
        # bez issues – nic nevypisujeme, ať je výstup stručný

    if not any_issues:
        print("\n✅ Všechny stránky vypadají kompletně a správně ukončené!")
    else:
        if do_fix:
            print(f"\n🛠️  Dokončeno. Opraveno souborů: {fixed_count}.")
            print("   Zkontroluj případně .bak zálohy a stránku otevři s Ctrl+F5.")
        else:
            print("\n⚠️  Nalezené chyby viz výše. Spusť se --fix pro automatickou opravu.")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="SSCC: kontrola a auto-oprava HTML konců")
    ap.add_argument("--root", default=".", help="Kořenová složka (default .)")
    ap.add_argument("--recursive", action="store_true", help="Prohledat rekurzivně všechny podadresáře")
    ap.add_argument("--fix", action="store_true", help="Automaticky doplnit chybějící </main>, </body>, </html>")
    ap.add_argument("--marker", action="store_true", help="Přidat integritní marker do konzole (volitelné)")
    args = ap.parse_args()

    process(args.root, args.fix, args.recursive, args.marker)

