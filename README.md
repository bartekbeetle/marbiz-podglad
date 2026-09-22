# Marbiz — strona WWW (build lokalny)

Statyczna strona wizytówkowa dla firmy **Marbiz** (Paweł Dzierżanowski, Włocławek) —
transport wywrotką, żuraw HDS, roboty ziemne. Zero frameworków JS, zero zewnętrznych
hostów (fonty systemowe, brak CDN). Zbudowana pod localhost, **nie wdrożona nigdzie**.

## Jak odpalić

```
cd ~/Projects/marbiz-www
python3 serve.py
```

Serwer stoi na **http://localhost:3007**. `Ctrl+C` żeby zatrzymać. `serve.py` to
zwykły `http.server` z jedną poprawką: brakująca ścieżka zwraca treść `404.html`
z realnym kodem HTTP 404 (standardowy `http.server` nie umie tego bez własnego handlera).

Jeśli port jest zajęty: `lsof -i :3007` i `kill <PID>`, albo zmień `PORT` w `serve.py`.

## Struktura

```
index.html                  strona główna (hero, 5 usług, dowód zaufania, realizacje, kontakt)
transport-hds/index.html    podstrona usługowa
roboty-ziemne/index.html    podstrona usługowa
wywoz-ziemi/index.html      podstrona usługowa
transport-materialow/index.html  podstrona usługowa
kontakt/index.html          dane kontaktowe + obszar działania
404.html                    strona błędu (serwowana z kodem 404 przez serve.py)
css/styles.css               jeden plik CSS, wspólny dla wszystkich podstron
img/marbiz-01.png … 07.png  7 zdjęć skopiowanych z profilu FB Marbizu
serve.py                    serwer deweloperski na porcie 3007
```

## Co jest zrobione

- 6 podstron + 404, każda z unikalnym `<title>` (≤60 znaków) i `<meta description>`.
- `LocalBusiness` / `Service` JSON-LD na każdej stronie (bez NIP — patrz luki).
- CTA telefoniczne (`tel:+48602699269`) w headerze, w treści i na sticky call-barze
  mobile; `mailto:` do `marbiz.wloclawek@gmail.com`.
- Wszystkie `<img>` mają `alt`. Kontrast tekstu sprawdzony liczbowo (WCAG AA,
  ≥4,5:1 — accent `#C2410C` na białym = 5,18:1, ciemny grafit `#1F2937` = 14,68:1).
- Responsywne 320px → desktop, zweryfikowane przez CDP na 375px (zero poziomego
  scrolla na wszystkich 6 podstronach).
- **Kadrowanie klatek z filmów FB**: zdjęcia `marbiz-02` … `marbiz-07` mają w prawym
  górnym rogu ciemne kółko „…" (nakładka interfejsu Facebooka). Przycięte przez
  `transform: scale(1.18); transform-origin: bottom left;` na kontenerze z
  `overflow: hidden` — klasa `.photo-frame` (galerie/split) i `.hero-photo.crop-corner`
  (hero na 4 podstronach usługowych). Zweryfikowane wizualnie zrzutami CDP na
  desktopie — nakładka nie jest widoczna na żadnej stronie.
- Zero Google Analytics, pikseli, cookies, formularzy — strona nie zbiera danych
  osobowych, więc nie ma polityki prywatności (brief świadomie to wyklucza na tym etapie).

## Luki — do uzupełnienia przed jakąkolwiek publikacją

1. **NIP firmy nieznany.** Nie ustalony zdalnym researchem (pełny research:
   `firmy/niezalezny-przedsiebiorca/klienci/marbiz/research.md` w vaulcie).
   Do dopisania w stopce każdej podstrony (miejsce oznaczone komentarzem HTML
   `<!-- LUKA: NIP firmy nieznany ... -->` przed `<p>© 2026 Marbiz...`).
2. **Zdjęcia w niskiej rozdzielczości.** Wszystkie 7 plików to klatki wyjęte z filmów
   z profilu FB (~615×329 px), nie oryginały. Wystarczają na localhost, ale hero
   będzie rozmyte na ekranach szerszych niż telefon przy realnej publikacji —
   potrzebne oryginalne zdjęcia/filmy od klienta (Paweł ma ich pewnie znacznie więcej).
3. **Pasek roboczy `#draft-banner`** na górze każdej podstrony (czerwony, tekst
   „WERSJA ROBOCZA") — sygnalizuje luki 1–2. Do usunięcia jednym cięciem: usuń
   `<div id="draft-banner">...</div>` z każdego pliku HTML (jest identyczny wiersz
   na początku `<body>` w każdym z 7 plików) — CSS (`#draft-banner`) można zostawić,
   nieużywana reguła nie szkodzi.

## Czego świadomie NIE ma

Zero deployu, zero DNS, zero domeny, zero kontaktu z klientem, zero Google
Analytics/pikseli/cookies. Ta strona ma zostać na localhoście — publikacja to
bramka Bartka.
