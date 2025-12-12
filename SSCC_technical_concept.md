# SSCC – Technický koncept (odborná část)

## Úvod pro odborníky

Tato část webu je určena odborné veřejnosti – inženýrům, výzkumníkům, technologickým partnerům a výrobcům.
Nejde o marketingový přehled ani popularizační text.

Cílem je popsat **technický rámec systému SSCC (SolarSpace Carbon Cycle)**:
- fyzikální a procesní limity,
- časové škály,
- integrační problémy,
- ekonomická rozhodovací kritéria,
- a otevřené výzkumné směry.

SSCC není prezentováno jako hotový produkt, ale jako **systémová architektura**, která umožňuje řídit energii, teplo a hmotu v čase tam, kde samotné zdroje selhávají kvůli variabilitě, infrastrukturním omezením a dlouhým časovým horizontům.

---

## 1. Obnovitelné zdroje a profil výroby

### Externí dopady OZE v území

Obnovitelné zdroje energie nejsou omezeny pouze fyzikálními parametry výroby, ale také **externími dopady na území**, infrastrukturu a kvalitu života. Tyto faktory jsou často opomíjeny v energetických modelech, přesto v praxi zásadně určují, **kolik OZE lze reálně nasadit**.

Energetický systém není optimalizován pouze fyzikou, ale také **akceptovatelností v území** a **technickými hranicemi infrastruktury**.

---

### Větrná energie – víc než kapacitní faktor

Větrné elektrárny ovlivňují své okolí nejen vizuálně, ale i fyzikálně:
- hluk a nízkofrekvenční vibrace,
- stroboskopický efekt,
- změny proudění v mezní vrstvě atmosféry,
- fragmentace krajiny a biotopů.

Tyto dopady jsou měřitelné a regulované, což:
- omezuje dostupné lokality,
- zvyšuje náklady na povolovací procesy,
- prodlužuje dobu realizace projektů.

Vnitrozemské státy navíc narážejí na **limit vhodných lokalit** a přenosových kapacit.

---

### Fotovoltaika – plošný a síťový problém

Fotovoltaika ve větším měřítku vyžaduje:
- rozsáhlé plochy,
- konkurenci se zemědělstvím a krajinou,
- zásahy do územního plánování.

Z hlediska sítě vytváří:
- krátké, synchronizované výkonové špičky,
- lokální přetížení distribučních soustav,
- rostoucí potřebu okamžité akumulace nebo omezení výroby (curtailment).

---

### Systémový důsledek

Teoretický potenciál OZE je často **výrazně vyšší než potenciál realizovatelný**.
SSCC s těmito limity nebojuje politicky, ale **technicky** – optimalizací využitelné energie místo maximalizace instalovaného výkonu.

---

## 2. Procesní dynamika a řízení SSCC

### Proč je řízení klíčové

SSCC je **časově proměnný, vícevstupový a vícevýstupový systém**, ve kterém se kombinují procesy s velmi rozdílnými časovými konstantami.
Bez pokročilého řízení by docházelo k:
- neefektivnímu cyklování zařízení,
- zrychlené degradaci,
- nestabilnímu provozu,
- bezpečnostním rizikům.

---

### Časové škály v SSCC

**Sekundy až minuty**
- fluktuace OZE,
- regulační zásahy,
- ochrany a interlocky.

**Hodiny až dny**
- řízení elektrolýzy,
- práce se zásobami H₂/NH₃,
- přepínání režimů výroba ↔ dodávka.

**Dny až sezóny**
- strategie dlouhodobé akumulace,
- řízení dostupnosti energie,
- sezónní optimalizace.

SSCC musí tyto vrstvy **oddělit a koordinovat současně**.

---

### Prediktivní řízení

Jednoduché reaktivní řízení nebo pevné scénáře jsou pro SSCC nedostatečné.
Systém přirozeně směřuje k **prediktivnímu řízení (MPC)**, které využívá:
- předpovědi výroby OZE,
- ceny energie,
- stav zásob,
- provozní limity zařízení.

Cílové funkce:
- maximalizace využití přebytků,
- minimalizace degradace,
- stabilita dodávky,
- dlouhodobá ekonomická optimalizace.

---

### Hierarchie řízení

Efektivní SSCC využívá víceúrovňovou strukturu:
- nízká úroveň: bezpečnost, ochrany, rychlé smyčky,
- střední úroveň: výkon, teplo, režimy,
- vysoká úroveň: strategie, optimalizace v čase.

Řízení není doplněk – je **integrální součást technologie**.

---

## 3. Ekonomika SSCC – CAPEX, OPEX a rozhodovací kritéria

### Základní premisa

Ekonomika SSCC není otázkou jedné technologie, ale **hodnoty systémového řešení**.
SSCC je ekonomicky smysluplné pouze tehdy, pokud **řeší reálný problém systému**, nikoli jen ukládání energie.

---

### Co SSCC nahrazuje

SSCC se ekonomicky uplatňuje tam, kde nahrazuje:
- posilování přenosových sítí,
- dlouhodobý curtailment,
- fosilní záložní zdroje,
- náklady na nestabilitu a výpadky.

---

### CAPEX a OPEX

CAPEX zahrnuje:
- výrobní a konverzní část,
- tepelné hospodářství,
- zásobníky,
- bezpečnostní systémy,
- řízení a infrastrukturu.

OPEX zahrnuje:
- údržbu,
- degradaci,
- provozní energii,
- personál a bezpečnost.

Špatně navržené řízení může zvýšit OPEX více než cena elektřiny.

---

### Kdy SSCC dává smysl

- dlouhé bloky nedostatku výroby,
- významný curtailment,
- omezená síť,
- vysoká hodnota dostupnosti energie,
- snaha o regionální autonomii.

---

### Kdy smysl nedává

- silně propojené sítě bez omezení,
- nízká variabilita výroby,
- levný a stabilní fosilní backup.

SSCC **není řešení pro každého**.

---

## 4. Vodík (H₂) v SSCC

### Proč ano

- flexibilní konverze přebytků,
- vysoká gravimetrická hustota,
- klíčový mezistupeň pro chemické procesy.

### Proč ne

- extrémně nízká objemová hustota,
- vysoké nároky na skladování,
- bezpečnostní rizika,
- nevhodnost pro domácí energetiku.

Vodík v SSCC není cílem, ale **procesním médiem**.

---

## 5. Amoniak (NH₃) v SSCC

### Proč ano

- dlouhodobé skladování (týdny až sezóny),
- vyšší objemová energetická hustota než H₂,
- existující průmyslová infrastruktura.

### Proč ne

- toxicita,
- nároky na bezpečnostní zónování,
- NOₓ při využití,
- náročná dynamika syntézy.

NH₃ patří do **průmyslového a infrastrukturního měřítka**, nikoli do domácností.

---

### H₂ vs. NH₃ – systémově

H₂ řeší hodiny až dny, NH₃ týdny až sezóny.
SSCC využívá **kombinaci obou**, nikoli volbu jednoho.

---

## 6. Roadmapa technologií SSCC

### TRL 7–9 (dnes)

- OZE,
- alkalická a PEM elektrolýza,
- klasická syntéza NH₃,
- základní průmyslové řízení.

SSCC lze realizovat dnes v konzervativním návrhu.

---

### TRL 5–7 (5–10 let)

- SOEC,
- částečně flexibilní syntéza NH₃,
- pokročilé MPC,
- tepelné zásobníky.

Zde se SSCC stává plnohodnotným systémovým řešením.

---

### TRL 3–6 (10–20 let)

- alternativní cesty k NH₃,
- pokročilé CO₂-cykly,
- nové materiály a katalyzátory.

---

### TRL 1–3 (výzkum)

- orbitální solární systémy,
- radikální procesní koncepty.

Inspirace, nikoli základ dnešních projektů.

---

## 7. Co SSCC není

SSCC není:
- zázračná technologie,
- univerzální řešení,
- náhrada fyzikálních zákonů,
- vodíková ekonomika,
- politický slogan.

SSCC je:
- technický integrační rámec,
- otevřený kritice,
- vyvíjející se systém.

Pokud hledáte jednoduchá řešení, SSCC není pro vás.
Pokud řešíte **reálné limity energetických systémů**, SSCC nabízí rámec, se kterým má smysl pracovat.

---
