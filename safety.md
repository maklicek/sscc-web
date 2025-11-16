# SSCC — SAFETY.md  
*(Základní zálohové šablony a jistoty)*

Tento soubor obsahuje **ověřené, kanonické a stabilní části webu**, které je možné kdykoli obnovit při chybě, přepisu, nebo úpravách, které se nepovedou.

Je zde uložena:
- jednotná HTML hlavička (včetně DOCTYPE)
- jednotný navigační prvek + motto
- struktura webu
- závěrečné značky stránky
- složková struktura projektu
- zásady jednotnosti

---

## 1️⃣ KANONICKÁ HLAVIČKA (POČÁTEK DOKUMENTU)

```html
<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>… sem název konkrétní stránky …</title>
  <meta name="description" content="SSCC – Solar & Synthetic Carbon Cycle">

  <!-- Favicons -->
  <link rel="icon" href="favicons/favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="favicons/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="favicons/favicon-16x16.png">
  <link rel="apple-touch-icon" href="favicons/apple-touch-icon.png">
  <link rel="manifest" href="favicons/site.webmanifest">

  <!-- JEDINÝ CSS soubor -->
  <link rel="preload" href="assets/style.css?v=p1" as="style" />
  <link rel="stylesheet" href="assets/css/style.css">
</head>

<body>
  <header class="site-header">
    <div class="nav-inner">
      <a href="index.html" class="brand">
        <img src="assets/img/logo-sscc.png"
             alt="SSCC – Solar &amp; Synthetic Carbon Cycle"
             class="brand-logo">

        <div class="brand-text">
          <div class="brand-title">SSCC</div>
          <div class="brand-subtitle">Solar &amp; Synthetic Carbon Cycle</div>
        </div>
      </a>

      <nav class="main-nav">
        <a href="index.html">Úvod</a>
        <a href="projekt-sscc.html">SSCC</a>
        <a href="projekty.html">Projekty</a>
        <a href="napady.html">Nápady</a>
        <a href="edukace.html">Edukace</a>
        <a href="spoluprace.html">Spolupráce</a>
        <a href="konsorcium.html">Konsorcium</a>
      </nav>
    </div>

    <div class="site-tagline">
      Zelenou se naše planeta nestane díky zákazům, ale tím, že ze škodlivého děláme užitečné.
    </div>
  </header>



<main class="page-main">
  <div class="container">

    <!-- ZDE ZAČÍNÁ OBSAH STRÁNKY -->
    
    … sem patří obsah …


  </div>
</main>

</body>
</html>


sscc-web/
│
├─ index.html
├─ projekt-sscc.html
├─ projekty.html
├─ napady.html
├─ edukace.html
├─ spoluprace.html
├─ konsorcium.html
│
├─ /assets
│   ├─ /css
│   │   └─ style.css
│   ├─ /img
│   │   └─ logo-sscc.png
│   └─ /fonts
│
├─ /favicons
│   ├─ favicon.ico
│   ├─ favicon-16x16.png
│   ├─ favicon-32x32.png
│   ├─ apple-touch-icon.png
│   └─ site.webmanifest
│
└─ SAFETY.md


4️⃣ ZÁSADY BEZPEČNÉHO EDITOVÁNÍ

Nikdy neupravujeme přímo v main bez zálohy

Pokud se mění menu → aktualizovat na všech stránkách

CSS smí mít jen jednu hlavní verzi

Logo, favicony a složky — neměnit jména

Nikdy nemažeme </body> a </html>


5️⃣ CO DĚLAT PŘI CHYBĚ NEBO ROZPADU STRÁNKY

Vezmi tuto hlavičku ze SAFETY.md

Vlož ji zpět do poškozené stránky

Zkopíruj obsah <main>…</main> z verze, která fungovala

Znovu nahraj na GitHub Pages

Otestuj ve dvou prohlížečích

Verzování CSS (1-x)
assets/style.css?v=p1

Záložní ZIP
sscc-web-STABLE-2025-xx-xx.zip


---

### Až to budeš mít:
💾 uložíš do rootu webu jako:





