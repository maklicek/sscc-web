import os
import re

# Složka, kde jsou HTML soubory (např. '.' pro aktuální)
ROOT = "."

def check_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    problems = []

    # Kontrola, jestli nechybí základní značky
    if not re.search(r"</body\s*>", content, re.IGNORECASE):
        problems.append("❌ Chybí </body>")
    if not re.search(r"</html\s*>", content, re.IGNORECASE):
        problems.append("❌ Chybí </html>")
    if "<main" in content and not re.search(r"</main\s*>", content, re.IGNORECASE):
        problems.append("⚠️  Chybí </main>")

    # Detekce utnutí uprostřed
    if re.search(r"Spolu$", content.strip()):
        problems.append("⚠️  Soubor končí neúplnou větou – pravděpodobně se načetl jen částečně")

    # Pokud se našly chyby → vrátíme seznam
    return problems


print("🔍 Kontrola HTML souborů v:", os.path.abspath(ROOT))
print("="*60)

found_errors = False

for file in os.listdir(ROOT):
    if file.endswith(".html"):
        issues = check_html(os.path.join(ROOT, file))
        if issues:
            found_errors = True
            print(f"\n📄 {file}")
            for issue in issues:
                print("   ", issue)

if not found_errors:
    print("\n✅ Všechny stránky vypadají kompletně a správně ukončené!")
else:
    print("\n⚠️  Opravit výše uvedené chyby a znovu spustit.")

