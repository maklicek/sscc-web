# SSCC — Pracovní rámec (workflow)

Tento soubor shrnuje, jak postupujeme při práci na webu SSCC.  
Cílem je mít pořádek, přehled a klid — krok za krokem, bez zmatku.

---

## 🧭 1. Princip: Jeden krok = jedna věc
Každý úkol řešíme samostatně.  
Např. „opravit projekty.html“ nebo „přidat nový projekt“.  
Nikdy neřešíme víc souborů najednou.  
Teprve když je stránka hotová, jdeme dál.

---

## 📂 2. Struktura projektu

/sscc-web
│
├── index.html
├── projekty.html
├── edukace.html
├── napady.html
├── konsorcium.html
│
├── assets/
│ ├── style.css ← jediný aktivní CSS
│ └── img/
│ ├── logo-sscc.png
│ ├── hero-sun.jpg
│ └── ...
│
└── docs/
└── workflow-sscc.md ← tento dokument


---

## 🎨 3. Pravidla pro soubory

### HTML
- Každá stránka má:
  - 1× `<header>`  
  - 1× `<main>`  
  - 1× `<footer>`
- Žádné duplikáty ani vnořené značky.
- Hlavička a patička jsou **identické** napříč stránkami.
- Každý `<a>` odkaz má funkční cestu.

### CSS
- Používá se **pouze `assets/style.css`**
- Všechny vizuální úpravy se dělají zde.
- Nikdy netvoříme „style.html“ nebo duplicitní CSS.

### Obrázky
- Všechny obrázky jdou do `assets/img/`
- Cesty vždy relativní: `assets/img/nazev.png`
- Názvy beze změn, bez mezer, bez diakritiky.

---

## ⚙️ 4. Jak pracujeme

### Každý denní cyklus má tři fáze:
1. **Zadání** – napíšeš, co se má udělat („přidat projekt, opravit layout“).
2. **Realizace** – já připravím *jen* potřebný kód (ne víc, ne míň).
3. **Potvrzení** – ty vložíš, otestuješ, pošleš screen → uzamykáme do regálu ✅

Teprve pak se posouváme dál.

---

## 🪶 5. Pravidlo názvů a cest

- Cesty a názvy jsou **svaté**.  
  Pokud by se někdy mělo něco změnit, musí to být dohodnuté předem.
- Příklady:
  - `assets/style.css` ✅  
  - `assets/img/logo-sscc.png` ✅  
  - `assets/img/hero-sun.jpg` ✅  

---

## 🧱 6. Verze souborů (verzování)

Když se dělá větší změna:
- vytvoříme kopii se suffixem `_v1`, `_v2`, …  
  např. `projekty_v2.html`
- starší se ukládá do složky `/archive` nebo se smaže po schválení.

To zaručí, že se nikdy neztratí funkční varianta.

---

## 🔍 7. Kontrolní seznam před uložením (checklist)

Před odevzdáním změny:
- [ ] Načítá se správně `assets/style.css`
- [ ] Nejsou duplikované značky `<main>` nebo `<footer>`
- [ ] Všechny odkazy fungují (žádné 404)
- [ ] Cesty k obrázkům jsou relativní a funkční
- [ ] Všechny stránky mají jednotnou hlavičku/patičku
- [ ] Layout vypadá stejně jako předchozí stránky (index, edukace, projekty…)

---

## 🌞 8. Naše zásady

- **Step by step.**  
  Dokončíme jednu stránku, teprve potom přecházíme na další.

- **Bez chaosu.**  
  Každý soubor má jediný účel. Když něco přestane fungovat, hledáme příčinu, ne náhodně opravujeme.

- **Učení se.**  
  Každá oprava je příležitost pochopit, proč se to stalo, a příště to zvládnout rychleji.

---

*SSCC: od neřádu k řádu. Od chaosu k rovnováze.* 🌍  
Společně budujeme systém, který funguje stejně elegantně jako cyklus uhlíku, který popisujeme.
